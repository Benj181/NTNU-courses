#pragma once
#include "std_lib_facilities.h"
#include <filesystem>
#include <fstream>

void writeUserInputToFile(const std::string &filename);
void addLineNumbers(const std::string &filename);