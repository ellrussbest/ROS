#! /usr/bin/python3

import rospy
import sys
from c_third_lesson.srv import Service, ServiceRequest, ServiceResponse

def add(x: int, y: int):
    rospy.wait_for_service('add_two_ints')
    
    try:
        service = rospy.ServiceProxy('add_two_ints', Service)
        response = service(x, y)
        return response.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)

    print("Requesting %s + %s"%(x, y))
    print("%s + %s = %s"%(x, y, add(x, y)))