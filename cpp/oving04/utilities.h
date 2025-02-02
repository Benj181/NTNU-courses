#pragma once
#include "std_lib_facilities.h"

// BEGIN: 1b
int incrementByValueNumTimes(int startValue, int increment, int numTimes);
// END: 1b

// BEGIN: 1d
void incrementByValueNumTimesRef(int& startValue, int increment, int numTimes);
// END: 1d

// BEGIN: 1e
void swapNumbers(int& a, int& b);

// END: 1e

// BEGIN: 2a
struct Student
{
    string name;
    string studyProgram;
    int age;
};

// END: 2a

// BEGIN: 2b
void printStudent(Student& stud);
// END: 2b

// BEGIN: 2c
// deklarerer funksjonen isInProgram her
// END: 2c

// BEGIN: 3a
 // deklarerer funksjonen randomizeString her
// END: 3a

// BEGIN: 3c
 // deklarerer funksjonen readInputToString her
// END: 3c

// BEGIN: 3d
 // deklarerer funksjonen countChar her
// END: 3d
