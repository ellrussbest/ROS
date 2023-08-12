#! /usr/bin/python3

'''
    1. Archimedian spiral
    2. Euler spiral
    3. Logarithmic spiral
    4. Fibonacci spiral
    5. Square Spiral
'''

import rospy
import time
from geometry_msgs.msg import Twist


def fib(count, memo={}):
    if count in memo:
        return memo[count]
    elif count < 2:
        memo[count] = 1
    else:
        memo[count] = fib(count - 1, memo) + fib(count - 2, memo)
    
    return memo[count]


def move_spiral():

    rospy.init_node('fibonacci_spiral', anonymous=True)

    # declare variables
    fib_arr = [0.0, 1.0]
    count = 0
    vel_msg = Twist()
    velocity_publisher = rospy.Publisher(
        '/turtle1/cmd_vel', Twist, queue_size=10)

    scale = 0.1  # Scaling factor for linear velocity
    while not rospy.is_shutdown():
        if count != 0:
            fib_arr.append(fib_arr[count] + fib_arr[count - 1])
        vel_msg.angular.z = 0.5
        vel_msg.linear.x = fib_arr[count] * scale  # Calculate linear velocity using Fibonacci sequence and scaling factor
        velocity_publisher.publish(vel_msg)
        count += 1


if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass
