#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv) {
    ros::init(argc, argv, "publisher_node");

    ros::NodeHandle node;
    ros::Publisher publisher = node.advertise<std_msgs::String>("publisher", 1000);
    ros::Rate rate(0.5);

    int count = 0;

    while(ros::ok()) {
        std_msgs::String msg;

        std::stringstream ss;
        ss << "Hello world " << count;

        msg.data = ss.str();

        ROS_INFO("[Publisher] I published %s\n", msg.data.c_str());

        publisher.publish(msg);
        rate.sleep();
        count++;
    }
    
    return 0;
}