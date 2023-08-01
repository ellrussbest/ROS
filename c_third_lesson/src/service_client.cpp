#include "ros/ros.h"
#include "c_third_lesson/Service.h"

int main(int argc, char **argv) {
    ros::init(argc, argv, "service_client_node");

    ros::NodeHandle nh;
    ros::ServiceClient client = nh.serviceClient<c_third_lesson::Service>("add_two_ints");

    int32_t a = nh.param<int32_t>("/service_client_node/a", 0);
    int32_t b = nh.param<int32_t>("/service_client_node/b", 0);

    c_third_lesson::Service service;

    service.request.a = a;
    service.request.b = b;

    if(client.call(service)) {
        ROS_INFO("Sum %ld", (long int)service.response.sum);
    }else {
        ROS_ERROR("Failed to call service add_two_ints");
        return 1;
    }

    return 0;
}