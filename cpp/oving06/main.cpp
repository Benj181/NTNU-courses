#include "std_lib_facilities.h"
#include "CourseCatalog.h"
#include "FileUtils.h"
#include "bouncingBall.h"

int main()
{
	// Her kan du teste din kode ved å kalle på de ulike funksjonene du har implementert	
	int choice;
	std::cout << "Chose function" << std::endl;
	std::cout << "1. writeUserInputToFile" << std::endl;
	std::cout << "2. addLineNumbers" << std::endl;
	std::cout << "3. testCourseCatalog" << std::endl;
	std::cout << "4. testReadAndWrite" << std::endl;
	std::cin >> choice;

	switch (choice){
		case 1:
			writeUserInputToFile("myFile.txt");
		case 2:
			addLineNumbers("myFile.txt");
		case 3:
			testCourseCatalog();
		case 4:
			testReadAndWrite();
	}

	return 0;
}