
%module fastdist
%{
#define SWIG_FILE_WITH_INIT
#include <vector>
#include <sys/types.h>
#include "../cpp/src/include/dig.hpp"
#include "../cpp/src/include/dist.hpp"
#include "../cpp/src/include/neighbors.hpp"
%}

%include <config.i>

// ================================================================
// actually have swig parse + wrap the files
// ================================================================
%include "../cpp/src/include/dig.hpp"
%include "../cpp/src/include/dist.hpp"
%include "../cpp/src/include/neighbors.hpp"

