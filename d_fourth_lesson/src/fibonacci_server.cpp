#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include "d_fourth_lesson/FibonacciAction.h"

/**
 * @brief FibonacciAction -> gives you the Action itself
 * @brief FibonacciFeedback -> gives you the Action feedback
 * @brief FibonacciResult -> gives you the Action result
 * 
 */

class FibonacciAction {
    public:
        // action_server and action_name are declared in the protected variable
        FibonacciAction(std::string name):
            action_server(name, boost::bind(&FibonacciAction::executeCB, this, _1), false),
            action_name(name)
            {
                action_server.start();
            }
        ~FibonacciAction(void){}

        void executeCB(const d_fourth_lesson::FibonacciGoalConstPtr &goal) {

        }

    protected:
        ros::NodeHandle nh;
        actionlib::SimpleActionServer<d_fourth_lesson::FibonacciAction> action_server;

        std::string action_name;

        d_fourth_lesson::FibonacciFeedback feedback;
        d_fourth_lesson::FibonacciResult result;
        
};

int main() {}