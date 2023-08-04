## Exaplanation

- The Fibonacci sequence is a good example to illustrate how actions work because it is a computation that can take a long time to complete for larger numbers. 
- It's a good example because it demonstrates how actions can provide feedback while the computation is in progress and how they can be preempted if necessary.

- In ROS, services are used when you need to perform a one-time request/response operation, whereas actions are used when you need to perform a task that may take a long time to complete and you need to get feedback on the progress of the task. 

- For example, let's say you have a robot that needs to move from one location to another. You could use a service to request that the robot move to the new location, but if the robot needs to navigate around obstacles or the path is very long, it may take a long time to complete. In this case, you could use an action to move the robot to the new location, which would provide feedback on the progress of the movement and allow the action to be preempted if necessary.