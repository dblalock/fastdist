//
//  main.cpp
//  fastdist
//
//  Created by DB on 2/10/18.
//  Copyright © 2018 D Blalock. All rights reserved.
//

//#include <iostream>

// unit tests magic
#define CATCH_CONFIG_RUNNER
#include "catch.hpp"

int main(int argc, char *const argv[]) {
    printf("running tests...\n");
    return Catch::Session().run(argc, argv);
    return 0;
}
//
//int main(int argc, const char * argv[]) {
//    // insert code here...
//    std::cout << "Hello, World!\n";
//    return 0;
//}

