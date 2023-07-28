#include <ros/ros.h>
#include <string>

int main(int argc, char** argv) {
  // Initialize the node
  ros::init(argc, argv, "talker");

  // Create a node handle
  ros::NodeHandle nh;

  // Get the message from the parameter server
  std::string message = nh.param<std::string>("/message/value", "default");

  // Print the message
  ROS_INFO("%s", message.c_str());

  // Spin the node
  ros::spin();
}