#include "ros/ros.h"

int main(int argc, char **argv) {
    ros::init(argc, argv, "parameter_node");

    ros::NodeHandle node;

    int _max = node.param<int>("/parameter_node/max", 0);
    // node.getParam("max", _max);

    int count = 0;

    while(count < _max) {
        ROS_INFO("Count %d", count);
        count++;
    }
    
    return 0;
}