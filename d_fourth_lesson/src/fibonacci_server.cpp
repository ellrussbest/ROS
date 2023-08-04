#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include "d_fourth_lesson/FibonacciAction.h"

/**
 * @brief FibonacciAction -> gives you the Action itself
 * @brief FibonacciFeedback -> gives you the Action feedback
 * @brief FibonacciResult -> gives you the Action result
 *
 */

class FibonacciAction
{
public:
    // action_server and action_name are declared in the protected variable
    FibonacciAction(std::string name) : action_server(name, boost::bind(&FibonacciAction::executeCB, this, boost::placeholders::_1), false),
                                        action_name(name)
    {
        action_server.start();
    }

    ~FibonacciAction(void) {}

    void executeCB(const d_fourth_lesson::FibonacciGoalConstPtr &goal)
    {
        // helper variables
        ros::Rate rate(1);
        bool success = true;

        // push_back the seeds for the fibonacci sequence
        feedback.sequence.clear();
        feedback.sequence.push_back(0);
        feedback.sequence.push_back(1);

        // publish info to the console for the user
        ROS_INFO(
            "%s: Executing, creating fibonacci sequence of order %i with seeds %i, %i",
            action_name.c_str(),
            goal->order,
            feedback.sequence[0],
            feedback.sequence[1]);

        // start executing the action
        for (int i = 1; i <= goal->order; i++)
        {
            // check that preempt has not been requested by the client
            if (action_server.isPreemptRequested() || !ros::ok())
            {
                ROS_INFO("%s: Preempted", action_name.c_str());

                // set the action state to preempted
                action_server.setPreempted();
                success = false;
                break;
            }

            feedback.sequence.push_back(feedback.sequence[i] + feedback.sequence[i - 1]);
            action_server.publishFeedback(feedback);

            // this sleep is not necessary, the sequence is computed at 1 Hz for demonstration purposes
            rate.sleep();

            if (success)
            {
                result.sequence = feedback.sequence;
                ROS_INFO("%s: Succeeded", action_name.c_str());

                // set the action state to succeeded
                action_server.setSucceeded(result);
            }
        }
    }

protected:
    ros::NodeHandle nh;
    actionlib::SimpleActionServer<d_fourth_lesson::FibonacciAction> action_server;

    std::string action_name;

    d_fourth_lesson::FibonacciFeedback feedback;
    d_fourth_lesson::FibonacciResult result;
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "fibonacci");

    FibonacciAction fibonacci("fibonacci");

    ros::spin();

    return 0;
}