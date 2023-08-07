#! /usr/bin/python3

'''
    1. Archimedian spiral
    2. Euler spiral
    3. Logarithmic spiral
    4. Fibonacci spiral
    5. Square Spiral
'''

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math


def move_spiral():

    # declare variables
    flag: bool = False
    x0: float
    y0: float
    x: float
    y: float
    theta: float
    sampling_time: float = 0.1
    linear_velocity: float = 2.0

    # position subscriber callback
    def callback(message: Pose):
        nonlocal x, y, theta, flag, x0, y0

        if (not flag):
            x0 = message.x
            y0 = message.y
            flag = True
        x = message.x
        y = message.y
        theta = message.theta

    rospy.init_node('spiral_movement', anonymous=True)
    rospy.Subscriber("/turtle1/pose", Pose, callback=callback)
    velocity_publisher = rospy.Publisher(
        '/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    rospy.wait_for_message("/turtle1/pose", Pose)

    # rate = rospy.Rate(10)  # Loop rate in Hz
    while not rospy.is_shutdown():
        a = math.sqrt(x0**2 + y0**2)
        r = math.sqrt((x-x0)**2 + (y-y0)**2)
        theta = r / (r-a)

        vel_msg.linear.x = linear_velocity
        vel_msg.angular.z = theta
        print("%s %s %s", a, r, theta)

        velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass
