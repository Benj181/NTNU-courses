#include <iostream>
#include "DynamicMemory.h"
#include "Matrix.h"
#include "Dummy.h"

int main() {
	Matrix m(3);
	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
		std::cout << m.get(i, j) << " ";
		}
		
		std::cout << std::endl;
	}
	return 0;
}