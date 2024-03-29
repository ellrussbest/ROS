#! /usr/bin/python3

import rospy
import actionlib
from d_fourth_lesson.msg import FibonacciFeedback, FibonacciResult, FibonacciAction, FibonacciGoal


class FibonacciAction(object):
    # create messages that are used to publish feedback/result
    _feedback = FibonacciFeedback()
    _result = FibonacciResult()

    def __init__(self, name):
        self._action_name = name
        self._action_server = actionlib.SimpleActionServer(
            self._action_name, FibonacciAction, execute_cb=self.execute_cb, auto_start=False)
        self._action_server.start()

    def execute_cb(self, goal: FibonacciGoal):
        # helper variables
        rate = rospy.Rate(1)
        success = True

        # append the seeds for the fibonacci sequence
        self._feedback.sequence = []
        self._feedback.sequence.append(0)
        self._feedback.sequence.append(1)

        # publish info to the console for the user
        rospy.loginfo("%s: Executing, creating fibonacci sequece of order %i with seeds %i, %i" % (
            self._action_name, goal.order, self._feedback.sequence[0], self._feedback.sequence[1]))
        
        # start executing the action
        for i in range(1, goal.order):
            # check that preempt has not been requested by the client
            if self._action_server.is_preempt_requested():
                rospy.loginfo("%s: Preempted" % self._action_name)
                self._action_server.set_preempted()
                success = False
                break
            self._feedback.sequence.append(self._feedback[i] + self._feedback.sequence)

            # publish the feedback
            self._action_server.publish_feedback(self._feedback)

            #this step is not necessary, the sequece is computed at 1Hz for demonstration purposes
            rate.sleep()

        if success:
            self._result.sequence = self._feedback.sequence
            rospy.loginfo("%s: Succeeded"% self._action_name)
            self._action_server.set_succeeded(self._result)

if __name__ == "__main__":
    rospy.init_node("fibonacii")
    server = FibonacciAction(rospy.get_name())
    rospy.spin()
    