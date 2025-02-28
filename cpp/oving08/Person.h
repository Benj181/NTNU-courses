#pragma once
#include "Car.h"
#include <string>
#include <iostream>
#include <memory>

class Person{
	// BEGIN 2a
	std::string name;
	std::string email;
	std::unique_ptr<Car> car;
	// END 2a
public:
	// BEGIN 2b
	Person(std::string name, std::string email, std::unique_ptr<Car> car = nullptr);
	std::string getName() const;
	std::string getEmail() const;
	void setEmail(const std::string& email);
	// END 2b

	// BEGIN 2c
	bool hasAvailableSeats() const;
	// END 2c

	// BEGIN 2d
	friend std::ostream& operator<<(std::ostream& os, const Person& person);
	// END 2d

	// Vi onsker ikke å tillate kopiering av Person-objekter
	Person(const Person&) = delete;
	Person& operator=(const Person&) = delete;

};
