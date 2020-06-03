import json
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest

from .models import Room

def navigate(request: WSGIRequest):
    paras = request.GET
    source_x = paras['source_x']
    source_y = paras['source_y']
    target_x = paras['target_x']
    target_y = paras['target_y']
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

        move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        move_base.wait_for_server()
        goal = MoveBaseGoal()  
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = room.roomIdx_x
        goal.target_pose.pose.position.y = room.roomIdx_y
        goal.target_pose.pose.orientation.w = 1.0
        move_base.send_goal(goal)
        
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

def fetch_item(request: WSGIRequest):
    pass
