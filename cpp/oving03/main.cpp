#include "std_lib_facilities.h"
#include "cannonball.h"
#include "utilities.h"

void printVector(const vector<double>& vec) {
    cout << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i];
        if (i < vec.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << std::endl;
}

int main()
{	
	playTargetPractice();
	return 0;
}