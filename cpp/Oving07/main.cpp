#include <iostream>
#include "DynamicMemory.h"
#include "Matrix.h"
#include "Dummy.h"

int main() {
	Matrix A(2, 3);
	Matrix C(2, 3);

	A.set(1, 1, 3);
	C.set(1, 2, 4);

	std::cout << A << std::endl;
	std::cout << C << std::endl;
	
	C = A;

	std::cout << A << std::endl;
	std::cout << C << std::endl;
	return 0;
}	