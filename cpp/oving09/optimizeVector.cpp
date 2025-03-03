#include "Stopwatch.h"
#include "optimizeVector.h"
#include <vector>
#include <iostream>


// BEGIN 2a
void testVector() {
    std::vector<int> vec;
    // vec.reserve(20);
    // vec.resize(20);
    std::cout << "Size: " << vec.size() << std::endl;
    std::cout << "Capacity: " << vec.capacity() << std::endl;
    for (int i = 0; i < 19; ++i){
        vec.push_back(i);
        std::cout << "Size: " << vec.size() << std::endl;
        std::cout << "Capacity: " << vec.capacity() << std::endl;
    }
}
// END 2a


void optimizeVector(){
    // BEGIN 2d
    
    // END 2d

    // BEGIN 2e
    
    // END 2e   
}