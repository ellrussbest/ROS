#ifndef AGE_H
#define AGE_H

#include "std_msgs/Float32.h"

std_msgs::Float32 years;
std_msgs::Float32 months;
std_msgs::Float32 days;

namespace a_first_lesson
{
  typedef struct _Age
  {
    std_msgs::Float32 years;
    std_msgs::Float32 months;
    std_msgs::Float32 days;
  } Age;
}

#endif