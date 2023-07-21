#include "ros/ros.h"
#include "std_msgs/String.h"

void callback(const std_msgs::String::ConstPtr &msg) {
    ROS_INFO("[subscriber] I heard [%s]\n", msg->data.c_str());
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "subscriber_node");
    ros::NodeHandle node;

    ros::Subscriber subscriber = node.subscribe("publisher", 1000, callback);

    ros::spin();

    return 0;
}