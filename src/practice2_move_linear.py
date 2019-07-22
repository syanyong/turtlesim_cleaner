#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

position_x = 0
position_y = 0


# Called when the position of turtle is changed.
def poseReceived(position_data):
    global position_x, position_y  # When we want to change global variable from function
    position_x = position_data.x
    position_y = position_data.y


def get_distance(self, goal_x, goal_y):
    distance = sqrt(pow((goal_x - position_x), 2) + pow((goal_y - position_y), 2))
    return distance


# Main program
def main():
    rospy.init_node('myrobot', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, poseReceived)
    vel_msg = Twist()
    t0 = time.time()    # Get time

    while not rospy.is_shutdown():  # detect CTRL + C
        print("%d, %d" % (position_x, position_y))
        vel_msg.linear.x = 1
        velocity_publisher.publish(vel_msg)

    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass


