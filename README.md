## The basic concepts of ROS lies on Topics

-   This is how ROS works
-   At its most top level, we have topics registered at the ROScore
-   And we have two types of Nodes: Nodes that publish/writes into the topic, and nodes that subscribes/reads from the topic
-   The publishers also happen to be the same nodes that creates the topic.
-   So when we power on the publisher, it will keep on publishing until there is another node that will start listening to it
-   Even after the subscriber has been powered off, the publisher will still keep on publishing
-   This is same for the subscribers, which when powered on will do nothing until they get a message from the topic that they are
-   subscribed to.

## ROS commands

```
    roscore
    roscore -p [port_number]

    catkin_create_pkg [name_of_pkg] [dependencies]

    rosrun [name_of_package] [name_of_executable_file]
    rosrun rqt_graph rqt_graph

    rosnode ping	test connectivity to node
	rosnode list	list active nodes
	rosnode info	print information about node
	rosnode machine	list nodes running on a particular machine or list machines
	rosnode kill	kill a running node
	rosnode cleanup	purge registration information of unreachable nodes

    rostopic bw	    display bandwidth used by topic
	rostopic delay	display delay of topic from timestamp in header
	rostopic echo	print messages to screen
	rostopic find	find topics by type
	rostopic hz	    display publishing rate of topic
	rostopic info	print information about active topic
	rostopic list	list active topics
	rostopic pub	publish data to topic
	rostopic type	print topic or field type

    rosmsg show	    Show message description
	rosmsg info	    Alias for rosmsg show
	rosmsg list	    List all messages
	rosmsg md5	    Display message md5sum
	rosmsg package	List messages in a package
	rosmsg packages	List packages that contain messages

    rospack help
    rospack list

	(
		Parameters that can be used by nodes at runtime and are normally used for static data,
		such as configuration parameters
	)
	rosparam set	set parameter
	rosparam get	get parameter
	rosparam load	load parameters from file
	rosparam dump	dump parameters to file
	rosparam delete	delete parameter
	rosparam list	list parameter names

	export | grep ROS
```
