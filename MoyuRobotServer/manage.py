#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import rospy
from geometry_msgs.msg import Twist

base_cmd = Twist()


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MoyuRobotServer.settings')
    rospy.init_node('commander', anonymous=True)
    
    base_cmd.linear.x = 0
    base_cmd.linear.y = 0
    base_cmd.angular.z = 0
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
