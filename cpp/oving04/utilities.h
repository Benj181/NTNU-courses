#pragma once
#include "std_lib_facilities.h"
#include <random>

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
bool isInProgram(const Student &stud, const string &program);
// END: 2c

// BEGIN: 3a
string randomizeString(const int &stringLength, const char &upperLimitChar, const char &lowerLimitChar);
// END: 3a

// BEGIN: 3c
string readInputToString(const int &n, const char &upperLimitChar, const char &lowerLimitChar);
// END: 3c

// BEGIN: 3d
int countChar(string letters, char letter);
// END: 3d
