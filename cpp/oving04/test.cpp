#include "test.h"

void testCallByValue(){
	int v0 = 5;
	int increment = 2;
	int iterations = 10;
	int result = incrementByValueNumTimes(v0, increment, iterations);
	cout << "v0: " << v0 
		 << " increment: " << increment
		 << " iterations: " << iterations 
		 << " result: " << result << '\n';
}

void testCallByReference(){
	// BEGIN: 1d
	int v0 = 5;
	int temp = v0;
	int increment = 2;
	int iterations = 10;
	incrementByValueNumTimesRef(v0, increment, iterations);
	cout << "v0: " << temp
		 << " increment: " << increment
		 << " iterations: " << iterations 
		 << " result: " << v0 << '\n';
	// END: 1d
}

void testSwapNumbers(){
 int a = 2;
 int b = 4;
 cout << "Before: " << "a: " << a << ", b: " << b << endl;
 swapNumbers(a, b);
 cout << "After: " << "a: " << a << ", b: " << b << endl;
}

void testPrintStudent(){
	Student stud {"Ben", "MTFYMA", 21};
	printStudent(stud);
}

void testIsInProgram(){
	Student s {"Ben", "MTFYMA", 21};
	cout << "Is my program MTFYMA?: " << isInProgram(s, "MFYMA");
}


void testString(){
	// 3b OG 3e gjøres inne i her
	// BEGIN: 3b
	int stringLength = 8;
	char upperChar = 'F';
	char lowerChar = 'A';
	randomizeString(stringLength, upperChar, lowerChar);
	cout << "random string\n> " << randomizeString(stringLength, upperChar, lowerChar) <<endl;
	// END: 3b

	// BEGIN: 3e

	// END: 3e
}