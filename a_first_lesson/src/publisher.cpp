#include "ros/ros.h"
#include "std_msgs/String.h"
#include "../include/a_first_lesson/Age.h"
#include <sstream>

int main(int argc, char **argv) {
    ros::init(argc, argv, "publisher_node");

    ros::NodeHandle node;
    ros::Publisher publisher = node.advertise<std_msgs::String>("publisher", 1000);

    a_first_lesson::Age age_msg;
    age_msg.days.data = 30.0;
    age_msg.months.data = 12.0;
    age_msg.days.data = 21.0;
    ros::Publisher age_publisher = node.advertise<a_first_lesson::Age>("age_publisher", 10);
    ros::Rate rate(0.5);

    int count = 0;

    while(ros::ok()) {
        std_msgs::String msg;

        std::stringstream ss;
        ss << "Hello world " << count;

        msg.data = ss.str();

        ROS_INFO("[Publisher] I published %s\n", msg.data.c_str());
        // ROS_INFO("[Publisher] I p %f\n", age_msg.years.data);

        publisher.publish(msg);
        age_publisher.publish(age_msg);
        rate.sleep();
        count++;
    }
    
    return 0;
}