## How to create your own service message
So, what if none of the service messages that are available in ROS fit your needs? Then, you create your own message, as you did with the Topic messages.

In order to create a service message, you will have to follow the next steps:
- Example 6.8 -
1) Create a package like this:
   Execute in Shell #1
In [ ]:
roscd


In [ ]:
cd ..


In [ ]:
cd src


In [ ]:
catkin_create_pkg my_custom_srv_msg_pkg rospy


2) Create your own Service message with the following structure. You can put as many variables as you need, of any type supported by ROS: ROS Message Types. Create a srv folder inside your package , as you did with the topics msg folder. Then, inside this srv folder, create a file called MyCustomServiceMessage.srv. You can create with the IDE or the WebShell, as you wish.
   Execute in Shell #1
In [ ]:
roscd my_custom_srv_msg_pkg/


In [ ]:
mkdir srv


In [ ]:
vim srv/MyCustomServiceMessage.srv


You can also create the MyCustomServiceMessage.srv through the IDE, if you don't feel confortable with vim.
The MyCustomServiceMessage.srv could be something like this:
In [ ]:
int32 duration    # The time (in seconds) during which BB-8 will keep moving in circles
---
bool success      # Did it achieve it?


6.2.1   Prepare CMakeLists.txt and package.xml for custom Service compilation
You have to edit two files in the package similarly to how we explained for Topics:
CMakeLists.txt
package.xml
6.2.2   Modification of CMakeLists.txt
You will have to edit four functions inside CMakeLists.txt:
find_package()
add_service_files()
generate_messages()
catkin_package()
I. find_package()
All the packages needed to COMPILE the messages of topics, services, and actions go here. It's only getting its paths, and not really importing them to be used in the compilation.
The same packages you write here will go in package.xml, stating them as build_depend.
In [ ]:
find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)


II. add_service_files()
This function contains a list of all of the service messages defined in this package (defined in the srv folder).
For our example:
In [ ]:
add_service_files(
  FILES
  MyCustomServiceMessage.srv
)


III. generate_messages()
Here is where the packages needed for the service messages compilation are imported.
In [ ]:
generate_messages(
  DEPENDENCIES
  std_msgs
)


IV. catkin_package()
State here all of the packages that will be needed by someone that executes something from your package. All of the packages stated here must be in the package.xml file as <exec_depend>.
In [ ]:
catkin_package(
      CATKIN_DEPENDS
      rospy
)


Once you're done, you should have something similar to this:
   CMakeLists.txt
In [ ]:
cmake_minimum_required(VERSION 2.8.3)
project(my_custom_srv_msg_pkg)


## Here is where all the packages needed to COMPILE the messages of topics, services and actions go.
## It's only getting its paths, and not really importing them to be used in the compilation.
## It's only for further functions in CMakeLists.txt to be able to find those packages.
## In package.xml you have to state them as build
find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)

## Generate services in the 'srv' folder
## In this function will be all the action messages of this package ( in the action folder ) to be compiled.
## You can state that it gets all the actions inside the action directory: DIRECTORY action
## Or just the action messages stated explicitly: FILES my_custom_action.action
## In your case you only need to do one of two things, as you wish.
add_service_files(
  FILES
  MyCustomServiceMessage.srv
)

## Here is where the packages needed for the action messages compilation are imported.
generate_messages(
  DEPENDENCIES
  std_msgs
)

## State here all the packages that will be needed by someone that executes something from your package.
## All the packages stated here must be in the package.xml as exec_depend
catkin_package(
  CATKIN_DEPENDS rospy
)


include_directories(
  ${catkin_INCLUDE_DIRS}
)


6.2.3   Modification of package.xml
Add all of the packages needed to compile the messages.
In this case, you only need to add the message_generation.
You will have to import those packages as <build_depend>.


On the other hand, if you need a package for the execution of the programs inside your package, you will have to import those packages as <exec_depend>.
In this case, you will only need to add these 3 lines to your package.xml file:
In [ ]:
<build_depend>message_generation</build_depend>

<build_export_depend>message_runtime</build_export_depend>
<exec_depend>message_runtime</exec_depend>


So, at the end, you should have something similar to this:
   package.xml
In [ ]:
<?xml version="1.0"?>
<package format="2">
  <name>my_custom_srv_msg_pkg</name>
  <version>0.0.0</version>
  <description>The my_custom_srv_msg_pkg package</description>

  <maintainer email="user@todo.todo">user</maintainer>

  <license>TODO</license>

  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>
  <build_depend>message_generation</build_depend>
  <build_export_depend>rospy</build_export_depend>
  <exec_depend>rospy</exec_depend>
  <build_export_depend>std_msgs</build_export_depend>
  <exec_depend>std_msgs</exec_depend>
  <build_export_depend>message_runtime</build_export_depend>
  <exec_depend>message_runtime</exec_depend>

  <export>
  </export>
</package>


Once you're done, compile your package and source the newly generated messages:
   Execute in Shell #1
In [ ]:
roscd;cd ..


In [ ]:
catkin_make


In [ ]:
source devel/setup.bash
