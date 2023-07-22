#! /usr/bin/python3

import rospy
# from rospy import
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
from std_srvs.srv import Empty
# Literal allows you to input an array of types, while Optional allows you to input only two
# explicit values, so the array will only take one value...
from typing import Literal, Optional

# you can use Literal to act as a type in Python
Switch = Literal["on", "off"]


def switch_lights(_switch: Switch) -> None:
      if _switch not in ["on", "off"]:
        raise ValueError("Switch value must be 'on' or 'off'")
      else:
        print(_switch)


# x: None | int = 0
x: Optional[int] = None
# x: None | or any another thing
# x = None
y = 0
z = 0
yaw = 0

# this callback is meant to update the current position of the turtlesim
# i.e. it listens to the change in the position and updates the position


def pose_callback(msg: Pose):
    global x, y, z, yaw
    x = msg.x
    y = msg.y
    yaw = msg.theta


def move(speed: int, distance: int):
    x0: Optional[int] = None
    if (x):
        x0 = x
    velocity_message = Twist()
    # everytime we will be publishing a constant speed in the publisher
    velocity_message.linear.x = speed
    distance_moved = 0.0
    loop_rate = rospy.Rate(10)
    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    while not rospy.is_shutdown() and x0 != None:
        rospy.loginfo('Turtlesim moves foward')
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

        distance_moved = x - x0
        rospy.loginfo('the distance covered is {}'.format(distance_moved))
        if distance_moved > distance:
            rospy.loginfo('reached')
            break

    # finally, stop i.e. (set the linear speed to 0) the robot when the sitance is moved
    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)


if __name__ == '__main__':
    try:
        rospy.init_node('move_the_turtle_node')

        position_topic = '/turtle1/pose'
        pose_subscriber = rospy.Subscriber(position_topic, Pose, pose_callback)
        # this is an async process so we need to give our node time to recieve the
        # response
        time.sleep(2)

        print('move: ')
        move(1.0, 5.0)
        time.sleep(2)

        # reset the turtle robot back to its initial position
        print('start reset: ')
        rospy.wait_for_service('/reset')
        reset_turtle = rospy.ServiceProxy('/reset', Empty)
        reset_turtle()
        print('end reset: ')

        # keep on listening for any changes in the position
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo('node terminated')
