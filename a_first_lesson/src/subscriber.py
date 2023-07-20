#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def callback(message: String):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)


def subscriber():
    rospy.init_node("subscriber_node")
    rospy.Subscriber("subscribe", String, callback=callback)
    rospy.spin()


if __name__ == '__main__':
    subscriber()
