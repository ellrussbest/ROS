#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
import math

def publisher():
    publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtlesim_publisher')

    twist_message = Twist()
    twist_message.linear.x = 2.0
    twist_message.angular.z = 1.0

    # radius = linear_velocity / angular_velocity
    radius = 2.0 / 1.0

    '''
        speed = distance_covered / duration
        duration = distance_covered / linear_velocity
        therefore,
        duration = 2pi * radius / linear_velocity
        angular_velocity = 2pi / duration
        linear_velocity = 2pi * radius / duration
        radius = linear_velocity / angular_velocity
    '''
    duration = (2 * math.pi * radius) / 2.0
    start_time = rospy.get_time()

    while not rospy.is_shutdown() and rospy.get_time() - start_time < duration:
        publisher.publish(twist_message)
    
    publisher.unregister()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass