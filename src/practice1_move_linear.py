#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist


# Main program
def main():
    rospy.init_node('myrobot', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    t0 = time.time()    # Get time


    while not rospy.is_shutdown():  # detect CTRL + C
        vel_msg.linear.x = 1
        velocity_publisher.publish(vel_msg)

    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass


