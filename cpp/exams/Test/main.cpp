//
// This is example code from Chapter 2.2 "The classic first program" of
// "Programming -- Principles and Practice Using C++" by Bjarne Stroustrup
//
// This program outputs the message "Hello, World!" to the monitor
#include <Object.h>

void test(){
    std::cout << "Ran function!" << std::endl;
}
template<typename T>
class Point {
    T x = 0;
    T y = 0;
public:
    T getX() {
        return x;
    }
    T getY() {
        return y;
    }
};

//------------------------------------------------------------------------------'

// C++ programs start by executing the function main
int main() {
    Point<int> P;
}

// ------------------------------------------------------------------------------