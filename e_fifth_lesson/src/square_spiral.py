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

    rospy.init_node('archimedian_spiral', anonymous=True)

    # declare variables
    vel_msg = Twist()
    duration = 0.0
    temp_duration = 0.5
    start_time: float = rospy.get_time()
    velocity_publisher = rospy.Publisher(
        '/turtle1/cmd_vel', Twist, queue_size=10)
    is_moving_y = True
    count_x: int = 0
    count_y: int = 0

    # rate = rospy.Rate(10)  # Loop rate in Hz
    while not rospy.is_shutdown():
        while duration < temp_duration:
            duration = rospy.get_time() - start_time

            if is_moving_y and count_y % 2 == 0:
                vel_msg.linear.y = 1
            elif is_moving_y and count_y % 2 == 1:
                vel_msg.linear.y = -1
            elif not is_moving_y and count_x % 2 == 1:
                vel_msg.linear.x = -1
            else:
                vel_msg.linear.x = 1

            velocity_publisher.publish(vel_msg)

        if is_moving_y:
            count_y += 1
        else:
            count_x += 1

        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        velocity_publisher.publish(vel_msg)
        is_moving_y = not is_moving_y
        duration = 0.0
        start_time = rospy.get_time()
        temp_duration += 0.1


if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass