#include "Car.h"

#include <cassert>

// BEGIN 1b
Car::Car(int freeSeats) : freeSeats(freeSeats) {}
// END 1b

// BEGIN 1c
bool Car::hasFreeSeats() const{
    return freeSeats;
}

void Car::reserveFreeSeat(){
    freeSeats--;
}
// END 1c
