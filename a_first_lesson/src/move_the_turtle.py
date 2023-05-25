#! /usr/bin/python3


# We want to create a project that will make the turtlesim_node to move
# For this we have to first run the turtlesim node on our terminal e.g.
# rosrun turtlesim turtlesim_node
# After running the turtlesim_node, we will write the command rosnode list to check
# how many nodes are actively running and to know which node is associated
# with turtlesim
# After knowing the node that was associated with the turtlesim we will run
# rosnode info /turtlesim
# from the information we will realize that the node is actively
# listening to to /turtle1/cmd_vel topic
# then we will run the rostopic info /turtle1/cmd_vel
# for us to know the kind of message we have to send via the 
# /turtle1/cmd_vel topic

# now we want to create our publisher
# based on the information that we have collected

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def print_position_callback(msg):
    print(f'The robot is at postion {msg.x} and {msg.y}')

if __name__ == '__main__':
    publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rospy.init_node('move_turtlesim', anonymous=True)

    rate = rospy.Rate(1) # 1hz
    message = Twist()

    while not rospy.is_shutdown():
        message.angular.z = 1.0
        message.linear.x = 1.0

        publisher.publish(message)
        subscriber = rospy.Subscriber('/turtle1/pose', Pose, print_position_callback)

        rate.sleep();

# The above was my personal implementation
# The below is the implementation from Anis
# He created subscriber for the topic that will show the location
# of the robot
# and a publisher to the topic that will make the robot move
'''
#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x=0
y=0
z=0
yaw=0

def poseCallback(pose_message):
    global x
    global y, z, yaw
    x= pose_message.x
    y= pose_message.y
    yaw = pose_message.theta

    #print "pose callback"
    #print ('x = {}'.format(pose_message.x)) #new in python 3
    #print ('y = %f' %pose_message.y) #used in python 2
    #print ('yaw = {}'.format(pose_message.theta)) #new in python 3


def move(speed, distance):
        #declare a Twist message to send velocity commands
            velocity_message = Twist()
            #get current location 
            x0=x
            y0=y
            #z0=z;
            #yaw0=yaw;
            velocity_message.linear.x =speed
            distance_moved = 0.0
            loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
            cmd_vel_topic='/cmd_vel'
            velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

            while True :
                    rospy.loginfo("Turtlesim moves forwards")
                    velocity_publisher.publish(velocity_message)

                    loop_rate.sleep()
                    
                    #rospy.Duration(1.0)
                    
                    distance_moved = distance_moved+abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
                    print  distance_moved               
                    if  not (distance_moved<distance):
                        rospy.loginfo("reached")
                        break
            
            #finally, stop the robot when the distance is moved
            velocity_message.linear.x =0
            velocity_publisher.publish(velocity_message)
    


if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        #declare velocity publisher
        cmd_vel_topic='/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
        
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback) 
        time.sleep(2)
        print 'move: '
        move (1.0, 5.0)
        time.sleep(2)
        print 'start reset: '
        rospy.wait_for_service('reset')
        reset_turtle = rospy.ServiceProxy('reset', Empty)
        reset_turtle()
        print 'end reset: '
        rospy.spin()
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
'''