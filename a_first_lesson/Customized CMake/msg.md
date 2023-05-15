## Prepare CMakeLists.txt and package.xml for custom Message compilation
Now you may be wondering... in case I need to publish some data that is not an Int32, which type of message should I use? You can use all ROS defined (**rosmsg list**) messages. But, in case none fit your needs, you can create a new one.
In order to create a new message, you will need to do the following steps:
Create a directory named 'msg' inside your package
Inside this directory, create a file named Name_of_your_message.msg (more information down)
Modify CMakeLists.txt file (more information down)
Modify package.xml file (more information down)
Compile
Use in code
For example, let's create a message that indicates age, with years, months, and days.
1) Create a directory msg in your package.
In [ ]:
roscd <package_name>


In [ ]:
mkdir msg


2) The Age.msg file must contain this:
In [ ]:
float32 years
float32 months
float32 days


3) In CMakeLists.txt
You will have to edit four functions inside CMakeLists.txt:
find_package()
add_message_files()
generate_messages()
catkin_package()
I. find_package()
This is where all the packages required to COMPILE the messages of the topics, services, and actions go. In package.xml, you have to state them as build_depend.
HINT 1: If you open the CMakeLists.txt file in your IDE, you'll see that almost all of the file is commented. This includes some of the lines you will have to modify. Instead of copying and pasting the lines below, find the equivalents in the file and uncomment them, and then add the parts that are missing.
In [ ]:
find_package(catkin REQUIRED COMPONENTS
       rospy
       std_msgs
       message_generation   # Add message_generation here, after the other packages
)


II. add_message_files()
This function includes all of the messages of this package (in the msg folder) to be compiled. The file should look like this.
In [ ]:
add_message_files(
      FILES
      Age.msg
    ) # Dont Forget to UNCOMENT the parenthesis and add_message_files TOO


III. generate_messages()
Here is where the packages needed for the messages compilation are imported.
In [ ]:
generate_messages(
      DEPENDENCIES
      std_msgs
) # Dont Forget to uncoment here TOO


IV. catkin_package()
State here all of the packages that will be needed by someone that executes something from your package. All of the packages stated here must be in the package.xml as exec_depend.
In [ ]:
catkin_package(
      CATKIN_DEPENDS rospy message_runtime   # This will NOT be the only thing here
)


Summarizing, this is the minimum expression of what is needed for the CMakelists.txt file to work:
Note: Keep in mind that the name of the package in the following example is topic_ex, so in your case, the name of the package may be different.
In [ ]:
cmake_minimum_required(VERSION 2.8.3)
project(topic_ex)


find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)

add_message_files(
  FILES
  Age.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)


catkin_package(
  CATKIN_DEPENDS rospy message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)


4) Modify package.xml
Just add these 3 lines to the package.xml file.
In [ ]:
<build_depend>message_generation</build_depend> 

<build_export_depend>message_runtime</build_export_depend>
<exec_depend>message_runtime</exec_depend>


This is the minimum expression of the package.xml
Note: Keep in mind that the name of the package in the following example is topic_ex, so in your case, the name of the package may be different.
   package.xml
In [ ]:
<?xml version="1.0"?>
<package format="2">
  <name>topic_ex</name>
  <version>0.0.0</version>
  <description>The topic_ex package</description>


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


5) Now you have to compile the msgs. To do this, you have to type in a WebShell:
   Execute in Shell #1
In [ ]:
roscd; cd ..


In [ ]:
catkin_make


In [ ]:
source devel/setup.bash
