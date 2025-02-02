#include "utilities.h"

int incrementByValueNumTimes(int startValue, int increment, int numTimes)
{
	for (int i = 0; i < numTimes; i++)
		startValue += increment;

	return startValue;
}

// BEGIN: 1d
void incrementByValueNumTimesRef(int& startValue, int increment, int numTimes)
{
	for (int i = 0; i < numTimes; i++)
		startValue += increment;
}
// END: 1d

// BEGIN: 1e
void swapNumbers(int& a, int& b)
{
	int temp = a;
	a = b;
	b = temp;
}
// END: 1e

// BEGIN: 2b
void printStudent(Student& stud){
	cout << "Name: " << stud.name << ", Age: " << stud.age << ", Study Program: " << stud.studyProgram << endl;
}
// END: 2b

// BEGIN: 2c
bool isInProgram(const Student &stud, const string &program){
	return stud.studyProgram == program;	
}
// END: 2c


// BEGIN: 3a
string randomizeString(const int &stringLength, 
					   const char &upperLimitChar, 
					   const char &lowerLimitChar){
	// A (=65) gives lower number than F (=70)
	string result;
    random_device rd;
    default_random_engine generator(rd());
    uniform_int_distribution<char> distribution(upperLimitChar,
											   lowerLimitChar);

	for (int i = 0; i < stringLength; ++i) {
		char randomLetter = distribution(generator);
		result += randomLetter;
	}
	return result;
}

// END: 3a

// BEGIN: 3c
string readInputToString(const int &n, const char &upperLimitChar, const char &lowerLimitChar) {
	string result;
	char input;
	for (int i=0; i < n; i++){
		while (1) {
			cout << "Type in a character between " << lowerLimitChar << " and " << upperLimitChar << "\n> ";
			cin >> input;
			if (toupper(input) <= lowerLimitChar and
			    toupper(input) >= upperLimitChar) {
				break;
			} else {
				cout << "Not a valid character, try again..." << endl;
			}
		}
		result += toupper(input);
	}
	return result;
}
// END: 3c

// BEGIN: 3d
int countChar(string letters, char letter){
	return count(letters.begin(), letters.end(), letter);
}
// END: 3d
