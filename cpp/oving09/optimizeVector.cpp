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
    Stopwatch sw;
    std::vector<int> vec;
    sw.start();
    for (int i = 0; i < 1000000; ++i){
        vec.push_back(1);
    }
    std::cout << "Oppgave 2d: " << sw.stop() << std::endl;

    // END 2d

    // BEGIN 2e
    std::vector<int> vec2;
    vec2.reserve(1000000);
    sw.start();
    for (size_t i = 0; i < 1000000; ++i){
        vec2[i] = 1;
    }
    std::cout << "Oppgave 2e: " << sw.stop() << std::endl;
    
    std::vector<int> vec3;
    vec3.resize(1000000);
    sw.start();
    for (size_t i = 0; i < 1000000; ++i){
        vec3[i] = 1;
    }
    std::cout << "Oppgave 2e: " << sw.stop() << std::endl;
    // END 2e   
}