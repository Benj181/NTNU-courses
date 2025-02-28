#include "Meeting.h"

#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

// BEGIN 3b
std::ostream& operator<<(std::ostream& os, const Campus& c){
    os << campusToString.at(c);
    return os;
}
// END 3b

// BEGIN 3e
void Meeting::addParticipant(std::shared_ptr<Person> p){
    participants.push_back(p);
}
// END 3e

// BEGIN 3f
Meeting::Meeting(int day, int startTime, int endTime, 
        Campus location, const std::string& subject, 
        const std::shared_ptr<Person> leader) :
        day(day), startTime(startTime), endTime(endTime), 
        location(location), subject(subject), leader(leader){

    addParticipant(leader);
}
// END 3f

// BEGIN 3h
std::vector<std::string> Meeting::getParticipantList() const{
    std::vector<std::string> nameList;
    for (const auto& person : participants){
        nameList.push_back(person->getName());
    }
    return nameList;
}
// END 3h

// BEGIN 3i
std::vector<std::shared_ptr<Person>> Meeting::findPotentialCoDriving(Meeting& meeting) const {
    std::vector<std::shared_ptr<Person>> potentialDrivers;

    if (meeting.getLocation() == location &&
    meeting.getDay() == day &&
        std::abs(meeting.getStartTime() - startTime) <= 1 &&
        std::abs(meeting.getEndTime() - endTime) <= 1) {
        
        for (const auto& person : meeting.participants) {
            if (person->hasAvailableSeats()) {
                potentialDrivers.push_back(person);
            }
        }
    }
    return potentialDrivers;
}
// END 3i

// BEGIN 3j
std::ostream& operator<<(std::ostream& os, const Meeting& meeting) {
    os << "Meeting: " << meeting.getSubject() << "\n";
    os << "Location: " << campusToString.at(meeting.getLocation()) << "\n";
    os << "Time: " << meeting.getStartTime() << " - " << meeting.getEndTime() << "\n";
    os << "Leader: " << meeting.getLeader()->getName() << "\n";
    os << "Participants:\n";

    for (const auto& participant : meeting.getParticipantList()) {
        os << " - " << participant << "\n";
    }

    return os;
}

// END 3j
