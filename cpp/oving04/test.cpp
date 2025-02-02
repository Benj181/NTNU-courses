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


	// BEGIN: 3e
	int stringLength = 8;
	string grades = randomizeString(stringLength, 'A', 'F');
	cout << grades << endl;
	vector<int> gradeCount(6);
	string possibleGrades = "ABCDEF";
	double GPA = 0.0;

	for (size_t i = 0; i < 6; i++) {

		gradeCount.at(i) = countChar(grades, static_cast<char>(possibleGrades.at(i)));
		GPA += gradeCount.at(i) * (6-static_cast<int>(i));
	}

	GPA = GPA / stringLength;
	cout << "Your GPA (6) is " << GPA << endl;
	// END: 3e
}

void testreadInputToString() {
	string result = readInputToString(4, 'A', 'F');
	cout << "Your string is " << result;
}