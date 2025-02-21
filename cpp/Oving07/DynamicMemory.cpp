#include <cassert>
#include <iostream>

#include "DynamicMemory.h"

// BEGIN: 1a
void fillInFibonacciNumbers(int* result, int length) {
    if (length <= 0) return;
    result[0] = 0;
    if (length > 1) {
        result[1] = 1;
        for (int i = 2; i < length; i++) {
            result[i] = result[i - 1] + result[i - 2];
        }
    }
}
// END: 1a

// BEGIN: 1b
void printArray(int* array, int length){
    for (int i = 0; i < length; i++) {
        std::cout << array[i] << " ";
    }
    std::cout << std::endl;
}
// END: 1b

// BEGIN: 1c
void createFibonacci(){
    int n;
    std::cout << "Hvor mange tall i Fib rekka?\n> ";
    std::cin >> n;

    int* FibNums = new int[n];

    fillInFibonacciNumbers(FibNums, n);
    printArray(FibNums, n);
    delete[] FibNums;
    exit(0);
}
// END: 1c