import json
import os
import threading
import rospy
import actionlib
from sound_play.msg import SoundRequest
from geometry_msgs.msg import Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest

from .models import Room
from manage import base_cmd, cmd_vel_pub

lock = threading.Lock()
pub = rospy.Publisher('/robotsound', SoundRequest, queue_size=20)


def navigate(request: WSGIRequest):
    paras = request.GET
    source_x = float(paras['source_x'])
    source_y = float(paras['source_y'])
    target_x = float(paras['target_x'])
    target_y = float(paras['target_y'])
    move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    move_base.wait_for_server()
    goal = MoveBaseGoal()  
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = source_x
    goal.target_pose.pose.position.y = source_y
    goal.target_pose.pose.orientation.w = 1.0
    move_base.send_goal(goal)
    wait = move_base.wait_for_result(rospy.Duration(120))
    if not wait:
        response = {
            'message': 'Failed!',
            'success': False
        }
        response = json.dumps(response)
        return HttpResponse(response)

    goal = MoveBaseGoal()  
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = target_x
    goal.target_pose.pose.position.y = target_y
    goal.target_pose.pose.orientation.w = 1.0
    move_base.send_goal(goal)
    response = {
        'message': 'Succeed!',
        'success': True
    }
    response = json.dumps(response)
    return HttpResponse(response)

def deliver(request: WSGIRequest):
    paras = request.GET
    room_id = paras['room_id']
    try:
        room = Room.objects.get(roomNo=room_id)

        deliver_thread = threading.Thread(target=run_deliver, args=[room])
        deliver_thread.start()
        
        response = {
            'message': 'Succeed!',
            'success': True
        }
        response = json.dumps(response)
        return HttpResponse(response)
    except Room.DoesNotExist:
        response = {
            'message': 'Room does not exist!',
            'success': False
        }
        response = json.dumps(response)
        return HttpResponse(response)

def move_ctrl(request: WSGIRequest):
    paras = request.GET
    command = paras['command']

    linear_vel = 0.1
    k_vel = 3
    
    lock.acquire()
    if command=='forward':
        base_cmd.linear.x += linear_vel
        if base_cmd.linear.x > linear_vel*k_vel:
            base_cmd.linear.x = linear_vel*k_vel
        cmd_vel_pub.publish(base_cmd)
    elif command=='backward':
        base_cmd.linear.x += -linear_vel
        if base_cmd.linear.x < -linear_vel*k_vel:
            base_cmd.linear.x = -linear_vel*k_vel
        cmd_vel_pub.publish(base_cmd)
    elif command=='left':
        base_cmd.linear.y += linear_vel
        if base_cmd.linear.y > linear_vel*k_vel:
            base_cmd.linear.y = linear_vel*k_vel
        cmd_vel_pub.publish(base_cmd)
    elif command=='right':
        base_cmd.linear.y += -linear_vel
        if base_cmd.linear.y < -linear_vel*k_vel:
            base_cmd.linear.y = -linear_vel*k_vel
        cmd_vel_pub.publish(base_cmd)
    elif command=='stop':
        base_cmd.linear.x = 0
        base_cmd.linear.y = 0
        base_cmd.angular.z = 0
        cmd_vel_pub.publish(base_cmd)
    else:
        lock.release()
        response = {
            'message': 'Command invalid!',
            'success': False
        }
        response = json.dumps(response)
        return HttpResponse(response)

    lock.release()
    response = {
            'message': 'Succeed!',
            'success': True
    }
    response = json.dumps(response)
    return HttpResponse(response)

def hector_mapping(request: WSGIRequest):
    os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials hector_mapping.launch; exec bash\"'")
    response = {
            'message': 'Succeed!',
            'success': True
    }
    response = json.dumps(response)
    return HttpResponse(response)

def voice_reg(request: WSGIRequest):
    os.system("gnome-terminal -e 'bash -c \"roslaunch xfyun_waterplus voice_cmd_wpb_home.launch; exec bash\"'")
    response = {
            'message': 'Succeed!',
            'success': True
    }
    response = json.dumps(response)
    return HttpResponse(response)

def fetch_item(request: WSGIRequest):
    pass

def run_deliver(room: Room):
    move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    move_base.wait_for_server()
    goal = MoveBaseGoal()  
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = room.roomIdx_x
    goal.target_pose.pose.position.y = room.roomIdx_y
    goal.target_pose.pose.orientation.w = 1.0
    move_base.send_goal(goal)
    move_base.wait_for_result()
  
    
    
    sp = SoundRequest()
    sp.sound = SoundRequest.SAY
    sp.command = SoundRequest.PLAY_ONCE
    sp.volume = 1.0
    sp.arg = 'Hello, custom of room {:s}, there\'s a package for you.'.format(room.roomNo)
    pub.publish(sp)
