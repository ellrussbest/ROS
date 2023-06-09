#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    # create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # we need to initialize the node
    # in ROS, nodes are uniquely named. if two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique name
    # for our 'talker' node
    rospy.init_node('talker', anonymous=True)

    # set the loop rate
    rate = rospy.Rate(1) # 1hz

    # keep publishing until a ctr-c is pressed
    i = 0
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % i
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i=i+1


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass