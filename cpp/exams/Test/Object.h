#pragma once
#include <iostream>
#include <vector>


class Test{
private:
    constexpr static int z = 0;
    int x = 1;
    int y = 3;

public:
    Test() = default;
    Test(int a) : x(a) {}
    int sum();
    std::vector<int> get_point();
    static int add();
};


