#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include "d_fourth_lesson/FibonacciAction.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "test_fibonacci");

    // create the action client
    // true causes the client to spin its own thred
    actionlib::SimpleActionClient<d_fourth_lesson::FibonacciAction> action_client("fibonacci", true);

    ROS_INFO("Waiting for action server to start.");
    // wait for the action server to start
    action_client.waitForServer(); // will wait for infinite time

    ROS_INFO("Action server started, sending goal");
    // send a goal to the action
    d_fourth_lesson::FibonacciGoal goal;
    goal.order = 20;
    action_client.sendGoal(goal);

    // wait for the action to return
    // we could use this line to our advantage to do asynchronous processes
    // while we still wait for the results from the action see the commented example below
    bool finished_before_timeout = action_client.waitForResult(ros::Duration(30.0));

    /**
     * @brief Example to show how actions can be asynchronous
        while(ros::ok() && !ac.waitForResult(ros::Duration(0.5)))
        {
            ROS_INFO("Still calculating...");
            // Perform other tasks here, such as processing sensor data or planning the next action for the robot.
        }
     */

    if (finished_before_timeout)
    {
        actionlib::SimpleClientGoalState state = action_client.getState();
        ROS_INFO("Action finished: %s", state.toString().c_str());
    }
    else
    {
        ROS_INFO("Action did not finish before the timeout");
        action_client.cancelGoal();
    }

    // exit
    return 0;
}