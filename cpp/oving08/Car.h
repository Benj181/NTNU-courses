#pragma once

// BEGIN: 1a
class Car {
int freeSeats;
public:
    Car(int freeSeats);
    bool hasFreeSeats() const;
    void reserveFreeSeat();
};
// END: 1a