#! /usr/bin/python3

import rospy
from c_third_lesson.srv import Service, ServiceResponse, ServiceRequest


def add_callback(req: ServiceRequest):
    print("Returning [%s + %s = %s]" % (req.a, req.b, (req.a + req.b)))
    return ServiceResponse(req.a + req.b)


def add():
    rospy.init_node('add_two_ints')
    service = rospy.Service('add_two_ints', Service, add_callback)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add()