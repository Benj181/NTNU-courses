#pragma once
#include <utility>

class Dummy {
public:
    int *num;

    Dummy() {
        num = new int{0};
    }
    // BEGIN: 3c
    
    // END: 3c

	// Copy-Swap: Tar inn rhs som kopi, bytter medlemsvariable
    // BEGIN: 3d
	
    // END: 3d
    
    ~Dummy() {
        delete num;
    }
};

void dummyTest();
