#include "Stopwatch.h"
#include <memory>
#include <array>
#include <iostream>


// BEGIN 1a
double measurePerformanceUnique(){
    Stopwatch sw;
    sw.start();
    int n = 200000000;
    for (int i=n; --i;){
        std::unique_ptr<int> temp;
    }
    return sw.stop() / n;
}

double measurePerformanceShared(){
    Stopwatch sw;
    sw.start();
    int n = 300000000;
    for (int i=n; --i;){
        std::shared_ptr<int> temp;
    }
    return sw.stop() / n;
}

double measurePerformanceStack(){
    Stopwatch sw;
    sw.start();
    constexpr int size = 10000;
    int n = 2000000000;
    for (int i=n; --i;){
        std::array<int, size> arr1;
    }
    
    return sw.stop() / n;
}

double measurePerformanceHeap(){
    Stopwatch sw;
    sw.start();
    constexpr int size = 10000;
    int n = 2000000;
    for (int i=n; --i;){
        std::array<int, size>* arr2 = new std::array<int, size>;
        delete arr2;
    }
    return sw.stop() / n;
}
// END 1a