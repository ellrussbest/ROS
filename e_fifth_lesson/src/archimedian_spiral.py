#! /usr/bin/python3

'''
    1. Archimedian spiral
    2. Euler spiral
    3. Logarithmic spiral
    4. Fibonacci spiral
'''

import rospy
from geometry_msgs.msg import Twist

def move_spiral():
    rospy.init_node('spiral_movement', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Set the desired linear velocity
    vel_msg.linear.x = 0.5  # Adjust the value to control the speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0

    # Set the desired angular velocity (for rotation)
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.2  # Adjust the value to set the angular speed

    radius = 0.1  # Adjust the value to set the radius of the spiral
    distance = 0
    angle = 0

    rate = rospy.Rate(10)  # Loop rate in Hz
    while not rospy.is_shutdown():
        # Calculate the current distance and angle traveled
        distance += vel_msg.linear.x / 10.0
        angle += vel_msg.angular.z / 10.0

        # Use Archimedean spiral equation to set x and y position
        vel_msg.linear.x = radius * angle * rospy.get_time()
        vel_msg.linear.y = radius * angle * rospy.get_time()

        # Keep moving in the spiral until a desired distance is covered
        if distance >= 5.0:  # Adjust the value to set the desired distance
            break

        # Publish the velocity message
        velocity_publisher.publish(vel_msg)
        rate.sleep()

    # Stop the robot when the desired distance is covered
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass