#! /usr/bin/python3

'''
    1. Archimedian spiral
    2. Euler spiral
    3. Logarithmic spiral
    4. Fibonacci spiral
    5. Square Spiral
'''

import rospy
import math
from geometry_msgs.msg import Twist


def move_spiral():

    rospy.init_node('logarithmic_spiral', anonymous=True)

    # declare variables
    angular_velocity: float = 2.0
    vel_msg = Twist()
    duration = 0.0
    start_time: float = rospy.get_time() # constant
    velocity_publisher = rospy.Publisher(
        '/turtle1/cmd_vel', Twist, queue_size=10)
    
    i = 0.000000000000001
    

    # rate = rospy.Rate(10)  # Loop rate in Hz
    while not rospy.is_shutdown():
        duration = rospy.get_time() - start_time

        vel_msg.linear.x = math.log(i) * math.log(duration)
        vel_msg.angular.z = angular_velocity

        velocity_publisher.publish(vel_msg)
        i+= 0.0000000000000001


if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass
