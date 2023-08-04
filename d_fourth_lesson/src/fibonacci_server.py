#! /usr/bin/python3

import rospy
import actionlib
import sys
from d_fourth_lesson.msg import FibonacciAction, FibonacciGoal


def fibonacci_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor
    client = actionlib.SimpleActionClient("fibonacci", FibonacciAction)

    # waits until the action server has started up and started listening for goals
    client.wait_for_server()

    # creates a goal to send to the action server
    goal = FibonacciGoal(order=20)

    # sends the goal to thea ction server
    client.send_goal(goal)

    # waits for the server to finish performing the action
    client.wait_for_result()

    # prints out the result of executing the action
    return client.get_result()  # A FibonacciResult


if __name__ == "__main__":
    try:
        rospy.init_node("fibonacci_client_py")
        result = fibonacci_client()
        print("Result:", ', '.join([str(n) for n in result.sequence]))
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
