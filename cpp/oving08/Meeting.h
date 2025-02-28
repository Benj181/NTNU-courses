#pragma once

#include "Person.h"

#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <unordered_map>

// BEGIN 3a
enum class Campus {trh, aal, gjo};
// END 3a

// BEGIN 3b
std::ostream& operator<<(std::ostream& os, const Campus& c);
// END 3b


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


class Meeting{
	// BEGIN 3c
	int day;
	int startTime;
	int endTime;
	Campus location;
	std::string subject;
	const std::shared_ptr<Person> leader;
	std::vector<std::shared_ptr<Person>> participants;
	// END 3c
public:
	// BEGIN 3d
	int getDay() const { return day; }
	int getStartTime() const { return startTime; }
	int getEndTime() const { return endTime; }
	Campus getLocation() const { return location; }
	std::string getSubject() const { return subject; }
	std::shared_ptr<Person> getLeader() const { return leader; }
	// END 3d

	// BEGIN 3e
	void addParticipant(std::shared_ptr<Person> p);
	// END 3e
	
	Meeting(int day, int startTime, int endTime, Campus location, const std::string& subject, const std::shared_ptr<Person> leader);

	// BEGIN 3h
	std::vector<std::string> getParticipantList() const;
	// std::vector<std::shared_ptr<Person>> getParticipants() const { return participants; }
	// END 3h

	// BEGIN 3i
	std::vector<std::shared_ptr<Person>> findPotentialCoDriving(Meeting& meeting) const;
	// END 3i

	// Vi ønsker ikke å tillate kopiering av Meeting-objekter
	Meeting(const Meeting&) = delete;
	Meeting& operator=(const Meeting&) = delete;
};

// BEGIN 3j
std::ostream& operator<<(std::ostream& os, const Meeting& meeting);

// END 3j