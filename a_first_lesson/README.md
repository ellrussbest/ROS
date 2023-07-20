## The basic concepts of ROS lies on Topics
- This is how ROS works
- At its most top level, we have topics registered at the ROScore
- And we have two types of Nodes: Nodes that publish/writes into the topic, and nodes that subscribes/reads from the topic
- The publishers also happen to be the same nodes that creates the topic.
- So when we power on the publisher, it will keep on publishing until there is another node that will start listening to it
- Even after the subscriber has been powered off, the publisher will still keep on publishing
- This is same for the subscribers, which when powered on will do nothing until they get a message from the topic that they are 
- subscribed to.

## ROS commands
```
    roscore
    roscore -p [port_number]
```