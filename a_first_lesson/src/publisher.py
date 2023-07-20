#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def publisher():
    publisher = rospy.Publisher('publisher', String, queue_size=10)
    rospy.init_node('publisher_node')
    rate = rospy.Rate(1)

    i = 0
    while not rospy.is_shutdown():
        hello_str = "hello world %d" % (i)
        rospy.loginfo(hello_str)
        publisher.publish(hello_str)
        rate.sleep()
        i += 1


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
