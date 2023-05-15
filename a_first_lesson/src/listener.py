#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def chatter_callback(message):
    # get_caller_id(): Get fully resolved name of local node
    rospy.loginfo(rospy.get_caller_id() + "I hear %s", message.data)


def listener():
    # In ROS, nodes are uniquely named. if two nodes with the same
    # name are launched, the previous one is kicked off. the
    # anonymous=True flag means that rospy will choose a unique
    # name for oru 'listener' node so that multiple listeners can
    # run simultaneously
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, chatter_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
