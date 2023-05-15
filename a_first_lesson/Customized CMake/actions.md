## How to create your own action server message
It is always recommended that you use the action messages already provided by ROS. These can be found in the following ROS packages:
actionlib
Test.action
TestRequest.action
TwoInts.action
actionlib_tutorials
Fibonacci.action
Averaging.action
However, it may happen that you need to create your own type. Let's learn how to do it.
To create your own custom action message you have to:
1.- Create an action directory within your package.
2.- Create your Name.action action message file.
The Name of the action message file will determine later the name of the classes to be used in the action server and/or action client. ROS convention indicates that the name has to be camel-case.
Remember the Name.action file has to contain three parts, each part separated by three hyphens.
In [ ]:
#goal
package_where_message_is/message_type goal_var_name
---
#result
package_where_message_is/message_type result_var_name
---
#feedback
package_where_message_is/message_type feedback_var_name


If you do not need one part of the message (for example, you don't need to provide feedback), then you can leave that part empty. But you must always specify the hyphen separtors.
3.- Modify the file CMakeLists.txt and the package.xml to include action message compilation. Read the detailed description below.
9.3   Prepare CMakeLists.txt and package.xml files for custom action messages compilation
You have to edit two files in the package, in the same way that we explained for topics and services:
CMakeLists.txt
package.xml
9.3.1   Modification of CMakeLists.txt
You will have to edit four functions inside CMakeLists.txt:
find_package()
add_action_files()
generate_messages()
catkin_package()
I. find_package()
All of the packages needed to COMPILE the messages of topic, services, and actions go here.
In package.xml, you have to state them as built.
In [ ]:
find_package(catkin REQUIRED COMPONENTS
      # your packages are listed here
      actionlib_msgs
)


II. add_action_files()
This function will contain all of the action messages from this package (which are stored in the action folder) that need to be compiled.
Place them beneath the FILES tag.
In [ ]:
add_action_files(
      FILES
      Name.action
)


III. generate_messages()
The packages needed for the action messages compilation are imported here. Write the same here as you wrote in the find_package.
In [ ]:
generate_messages(
      DEPENDENCIES
      actionlib_msgs 
      # Your packages go here
)


IV. catkin_package()
State here all of the packages that will be needed by someone that executes something from your package.
All of the packages stated here must be in the package.xml file as <exec_depend>.
In [ ]:
catkin_package(
      CATKIN_DEPENDS
      rospy
      # Your package dependencies go here
)


Summarizing, You should end with a CMakeLists.txt file similar to this:
   CMakeLists.txt
In [ ]:
cmake_minimum_required(VERSION 2.8.3)
project(my_custom_action_msg_pkg)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  std_msgs 
  actionlib_msgs
)

## Generate actions in the 'action' folder
add_action_files(
   FILES
   Name.action
 )

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs actionlib_msgs
 )

catkin_package(
 CATKIN_DEPENDS rospy
)

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)


9.3.2   Modification of package.xml
1.- Add all of the packages needed to compile the messages.
If, for example, one of your variables in the .action file uses a message defined outside the std_msgs package, let's say nav_msgs/Odometry, you will need to import it. To do so, you would have to add as <build_depend> the nav_msgs package, adding the following line:
In [ ]:
<build_depend>nav_msgs<build_depend>


2.- On the other hand, if you need a package for the execution of the programs inside your package, you will have to import those packages as <exec_depend>, adding the following line:
In [ ]:
<build_export_depend>nav_msgs<build_export_depend>
<exec_depend>nav_msgs<exec_depend>


When you compile custom action messages, it's mandatory to add the actionlib_msgs as build_dependency.
In [ ]:
<build_depend>actionlib_msgs</build_depend>


When you use Python, it's mandatory to add the rospy as run_dependency.
In [ ]:
<build_export_depend>rospy<build_export_depend>
<exec_depend>rospy<exec_depend>


This is due to the fact that the rospy python module is needed in order to run all of your python ROS code.
Summarizing, you should end with a package.xml file similar to this:
   package.xml
In [ ]:
<?xml version="1.0"?>
<package format="2">
  <name>my_custom_action_msg_pkg</name>
  <version>0.0.0</version>
  <description>The my_custom_action_msg_pkg package</description>
  <maintainer email="user@todo.todo">user</maintainer>
  <license>TODO</license>

  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>actionlib</build_depend>
  <build_depend>actionlib_msgs</build_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>
  <build_export_depend>actionlib</build_export_depend>
  <build_export_depend>actionlib_msgs</build_export_depend>
  <build_export_depend>rospy</build_export_depend>
  <exec_depend>actionlib</exec_depend>
  <exec_depend>actionlib_msgs</exec_depend>
  <exec_depend>rospy</exec_depend>

  <export>
  </export>
</package>


Finally, when everything is correctly set up, you just have to compile:
   Execute in Shell #1
In [ ]:
roscd; cd ..


In [ ]:
catkin_make


In [ ]:
source devel/setup.bash


In [ ]:
rosmsg list | grep Name


You will get an output to the last command, similar to this:
  Output in Shell #1
my_custom_action_msg_pkg/NameAction
my_custom_action_msg_pkg/NameActionFeedback
my_custom_action_msg_pkg/NameActionGoal
my_custom_action_msg_pkg/NameActionResult
my_custom_action_msg_pkg/NameFeedback
my_custom_action_msg_pkg/NameGoal
my_custom_action_msg_pkg/NameResult

- Notes -
Note that you haven't imported the std_msgs package anywhere. But you can use the messages declared there in your custom .actions. That's because this package forms part of the roscore file systems, so therefore, it's embedded in the compilation protocols, and no declaration of use is needed.
