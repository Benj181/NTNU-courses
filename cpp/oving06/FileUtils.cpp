#include "FileUtils.h"



void writeUserInputToFile(const std::string &path)
{
	// BEGIN: 1a
	std::ofstream opStream{path};

	std::string inputFromUser;
	std::cout << "Write something to a file" << std::endl;
	while (1){
		std::cin >> inputFromUser;
		if (inputFromUser == "quit"){
			exit(0);
		}
		opStream << inputFromUser << std::endl;
	}

	// END: 1a
}


void addLineNumbers(const std::string &filename)
{
	// BEGIN: 1b
	std::ifstream ipStream{filename};
	if (!ipStream){
		std::cout << "File does'nt exist" << std::endl;
		exit(0);
	}
	std::ofstream opStream{filename + ".linum"};
	std::string line;
	int lineNumber = 1;
	while (std::getline(ipStream, line)) {
		opStream << lineNumber << line << std::endl;
		lineNumber++;
	}

	// END: 1b
}