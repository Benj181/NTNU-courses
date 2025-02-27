#pragma once

#include "Person.h"

#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <unordered_map>

// BEGIN 3a
enum class Campus {};
// END 3a

// BEGIN 3b

// END 3b

// FJERN KOMMENTAR NAAR DU SKAL BRUKE
/*
const std::unordered_map<Campus, std::string> campusToString {
	{ Campus::trh, "Trondheim" },
	{ Campus::aal, "Aalesund" },
	{ Campus::gjo, "Gjovik"}
};

const std::unordered_map<std::string, Campus> stringToCampus {
	{ "Trondheim", Campus::trh },
	{ "Aalesund", Campus::aal },
	{ "Gjovik", Campus::gjo }
};
*/

class Meeting
{
private:
	// BEGIN 3c

	// END 3c
public:
	// BEGIN 3d

	// END 3d

	// BEGIN 3e

	// END 3e
	
	Meeting(int day, int startTime, int endTime, Campus location, const std::string& subject, const std::shared_ptr<Person> leader);

	// BEGIN 3h

	// END 3h

	// BEGIN 3i

	// END 3i

	// Vi ønsker ikke å tillate kopiering av Meeting-objekter
	Meeting(const Meeting&) = delete;
	Meeting& operator=(const Meeting&) = delete;
};

// BEGIN 3j

// END 3j