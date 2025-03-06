#pragma once
#include <random>
#include <iostream>
#include <string>
#include <vector>

// BEGIN 4a
template<typename T>
T maximum(T a, T b){
    if (a > b){
        return a;
    } else {
        return b;
    }
}
// END 4a

// BEGIN 4b
template<typename T>
void shuffle(std::vector<T>& vec) {
    std::vector<T> newVec;
    newVec.resize(vec.size());
    std::vector<bool> taken(vec.size(), false);
    static std::random_device rd;
    static std::mt19937 g(rd());
    std::uniform_int_distribution<> dis(0, vec.size() - 1);
    int randomIndex;
    for (T val : vec){
        do {
            randomIndex = dis(g);
        } while (taken[randomIndex]);
        newVec[randomIndex] = val;
        taken[randomIndex] = true;
    }
    vec = newVec;
}
// END 4b

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& vec) {
    os << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        os << vec[i];
        if (i != vec.size() - 1) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

void testTemplateFunctions();