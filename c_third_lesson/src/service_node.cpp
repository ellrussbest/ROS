#include "ros/ros.h"
#include "c_third_lesson/Service.h"

bool add(
    c_third_lesson::Service::Request &request, 
    c_third_lesson::Service::Response &response
    )
{
    response.sum = request.a + request.b;
    ROS_INFO("request: x=%ld, y=%ld", (long int)request.a, (long int)request.b);
    ROS_INFO("sending back response: [%ld]", (long int)response.sum);
    return true;
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "service_node");

    ros::NodeHandle nh;

    ros::ServiceServer service = nh.advertiseService("add_two_ints", add);
    ROS_INFO("Ready to add two ints.");
    ros::spin();

    return 0;
}