#include <Object.h>

int Test::sum(){
    return x + y;
} 

std::vector<int> Test::get_point(){
    return std::vector<int>{x, y};
}

