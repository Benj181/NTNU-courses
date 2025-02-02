
#include "std_lib_facilities.h"
#include "test.h"
#include "utilities.h"

int main(){
	int choice;
	// cout << "Choose function:\n";
	// cout << "0. exit\n";
	// cout << "1. testCallByValue\n";
	// cout << "2. testcallByRefereance\n";
	// cout << "3. testSwapNumbers\n";
	// cout << "4. printStudent\n";
	// cout << "5. isInProgram\n";
	// cout << "6. testString\n";
	// cout << "> ";
	// cin >> choice;
	choice = 6;
	switch (choice) {
		case 0:
			exit(0);
			break;
		case 1:
			testCallByValue();
			break;
		case 2:
			testCallByReference();
			break;
		case 3:
			testSwapNumbers();
			break;
		case 4:
			testPrintStudent();
			break;
		case 5:
			testIsInProgram();
			break;
		case 6:
			testString();
			break;
		case 7:
			testreadInputToString();
			break;
		default:
			cout << "Invalid choice\n";
			break;
	}


	return 0;
}
