#include "Person.h"
#include "Meeting.h"
#include "MeetingWindow.h"
#include <iostream>


#include "Meeting.h"
#include "Person.h"
#include "Car.h"
#include <iostream>
#include <memory>


int main(){
	Campus trh = Campus::trh;
    Campus aal = Campus::aal;
    Campus gjo = Campus::gjo;

    std::cout << "Testing Campus printing:" << std::endl;
    std::cout << "Trondheim: " << trh << std::endl;
    std::cout << "Aalesund: " << aal << std::endl;
    std::cout << "Gjovik: " << gjo << std::endl;

	std::cout << std::endl;



	auto leader1 = std::make_shared<Person>("Alice", "alice@example.com", std::make_unique<Car>(2));
    auto leader2 = std::make_shared<Person>("Bob", "bob@example.com");

    auto participant1 = std::make_shared<Person>("Charlie", "charlie@example.com", std::make_unique<Car>(3));
    auto participant2 = std::make_shared<Person>("Dave", "dave@example.com");
    auto participant3 = std::make_shared<Person>("Eve", "eve@example.com", std::make_unique<Car>(1));

    // Creating two meetings
    Meeting meeting1(1, 10, 12, Campus::trh, "Math Study Group", leader1);
    meeting1.addParticipant(participant1);
    meeting1.addParticipant(participant2);

    Meeting meeting2(1, 11, 13, Campus::trh, "Physics Study Group", leader2);
    meeting2.addParticipant(participant3);

    // Testing findPotentialCoDriving()
    std::vector<std::shared_ptr<Person>> potentialDrivers = meeting1.findPotentialCoDriving(meeting2);

    // Printing potential co-drivers
    std::cout << "Potential Co-Drivers for Meeting 1 from Meeting 2:\n";
    for (const auto& driver : potentialDrivers) {
        std::cout << " - " << driver->getName() << " has available seats.\n";
    }

	std::cout << std::endl;

	std::cout << meeting1 << std::endl;
	std::cout << std::endl;

	std::cout << meeting2 << std::endl;

	std::cout << std::endl;

	return 0;
}
