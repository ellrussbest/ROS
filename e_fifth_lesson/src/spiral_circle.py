#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
import math

def publisher():
    publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtlesim_publisher')

    twist_message = Twist()
    linear_velocity = 2.0
    angular_velocity = 8.0
    twist_message.linear.x = linear_velocity
    twist_message.angular.z = angular_velocity

    radius = linear_velocity / angular_velocity
    radius = linear_velocity / angular_velocity

    '''
        speed = distance_covered / duration
        duration = distance_covered / linear_velocity
        therefore,
        duration = 2pi * radius / linear_velocity
        angular_velocity = 2pi / duration
        linear_velocity = 2pi * radius / duration
        radius = linear_velocity / angular_velocity
    '''
    duration = (2 * math.pi * radius) / linear_velocity
    start_time = rospy.get_time()

    while not rospy.is_shutdown():
        # and rospy.get_time() - start_time < duration:
        if(rospy.get_time() - start_time > duration - 1):
            angular_velocity -= 0.1
            radius = linear_velocity / angular_velocity
            duration = (2 * math.pi * radius) / linear_velocity
            start_time = rospy.get_time()
            twist_message.angular.z = angular_velocity
            twist_message.linear.x = linear_velocity
        publisher.publish(twist_message)
    
    publisher.unregister()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass