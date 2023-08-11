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


def move_spiral():

    rospy.init_node('archimedian_spiral', anonymous=True)

    # declare variables
    angular_velocity: float = 2.0
    vel_msg = Twist()
    duration = 0.0
    start_time: float = rospy.get_time()
    velocity_publisher = rospy.Publisher(
        '/turtle1/cmd_vel', Twist, queue_size=10)

    # rate = rospy.Rate(10)  # Loop rate in Hz
    while not rospy.is_shutdown():
        duration = rospy.get_time() - start_time

        vel_msg.linear.x = 0.1 * duration
        vel_msg.angular.z = angular_velocity

        velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass
