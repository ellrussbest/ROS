#include "ros/ros.h"
#include <iostream>
#include <string>
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv) {
    ros::init(argc, argv, "parameter_node");

    ros::NodeHandle node;

    int _max;
    node.getParam("max", _max);

    int count = 0;

    while(count < _max) {
        ROS_INFO("Count %d", count);
        count++;
    }
    
    return 0;
}