#include "MeetingWindow.h"
#include <iostream>

MeetingWindow::MeetingWindow(TDT4102::Point position, int width, int height, const std::string& title):
	// BEGIN 4a
    AnimationWindow{position.x, position.y, width, height, title},
	// END 4a

	// BEGIN 4e
	quitBtn{TDT4102::Point{width - btnW - pad, pad}, btnW, btnH, "Quit"},
	// END 4e

	// BEGIN 5a	
	personName{TDT4102::Point{pad, pad}, fieldW, fieldH, "Name: "},
	personEmail{TDT4102::Point{pad, pad + (pad + fieldH)}, fieldW, fieldH, "Email: "},
	// END 5a
	
	// BEGIN 5b
	personSeats{TDT4102::Point{pad, pad + (pad + fieldH)*2}, fieldW, fieldH, "Free seats: "},
	personNewBtn{TDT4102::Point{pad, pad + (pad + fieldH)*3}, fieldW, fieldH, "Add person"},
	// END 5b

	dummyArgument{0}
{
	// Felles
	// BEGIN 4f
	attachPersonWidget(quitBtn);
	// END 4f
	
	// BEGIN 4g
	quitBtn.setCallback(std::bind(&MeetingWindow::cb_quit, this));
	// END 4g

	// BEGIN 5d
	personNewBtn.setCallback(std::bind(&MeetingWindow::newPerson, this));
	// END 5d

	// Ny person
	attachPersonWidget(personName);
	attachPersonWidget(personEmail);

	attachPersonWidget(personSeats);
	attachPersonWidget(personNewBtn);
}

// Callbackfunksjoner
// BEGIN 4d
void MeetingWindow::cb_quit(){
	close();
}
// END 4d

// BEGIN 5c
void MeetingWindow::clearWindow(){
	personName.setText("Name: ");
	personEmail.setText("Email: ");
	personSeats.setText("Free seats: ");
}

void MeetingWindow::newPerson(){
	std::string name = personName.getText().substr(6); // Remove "Name: "
	std::string email = personEmail.getText().substr(7); // Remove "Email: "
	std::string seats_str = personSeats.getText().substr(12); // Remove "Free seats: "
	if (name != "" && email != "" && seats_str != ""){
		try {
			int seats = std::stoi(seats_str);
			if (seats == 0) {
				throw std::invalid_argument("Number of seats cannot be zero");
			}
			auto car = std::make_unique<Car>(seats);
			car->reserveFreeSeat();
			people.emplace_back(new Person{name, email, std::move(car)});
			clearWindow();
		} catch (const std::invalid_argument& e) {
			std::cerr << "Invalid number of seats: " << seats_str << std::endl;
		}
	} else {}
}

void MeetingWindow::attachPersonWidget(TDT4102::Widget& pw)
{
	add(pw);
	personWidgets.emplace_back(std::ref(pw));
}

void MeetingWindow::printPeople(){
	for (const auto& person : people){
		std::cout << *person << std::endl;
		std::cout << std::endl;
	}
}