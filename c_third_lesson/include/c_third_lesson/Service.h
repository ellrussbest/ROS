#ifndef SERVICE_H
#define SERVICE_H

#include <cstdint>

namespace c_third_lesson
{
  typedef struct _Service
  {
    class Request {
        public:
            int32_t a;
            int32_t b;
    };

    class Response {
        public:
            int32_t sum;
    };

    Request request;
    Response response;
  } Service;
}

#endif