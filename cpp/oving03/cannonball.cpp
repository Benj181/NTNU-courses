#include "cannonball.h"
#include "cannonball_viz.h"
#include "utilities.h"

// BEGIN: 2a
double acclY() {
    return -9.81;
}
// END: 2a

// BEGIN: 2b
double velY(double initVelocityY, double time) {
    return initVelocityY + acclY() * time;
}
// END: 2b

// BEGIN: 2c
double posX(double initPositionX, double initVelocityX, double time) {
    return initPositionX + initVelocityX * time + 0.5 * 0 * time * time;
}
double posY(double initPositionY, double initVelocityY, double time) {
    return initPositionY + initVelocityY * time + 0.5 * acclY() * time * time;
}
// END: 2c

// BEGIN: 2d
void printTime(double time) {
    int hours = time / 3600;
    int minutes = (time - hours * 3600) / 60;
    int seconds = time - hours * 3600 - minutes * 60;
    cout << hours << " hours, " << minutes << " minutes and " << seconds << " seconds." << endl;
}
// END: 2d

// BEGIN: 2e
double flightTime(double initVelocityY) {
    return -2 * initVelocityY / acclY();
}
// END: 2e

// BEGIN: 3b
bool testDeviation(double compareOperand, double toOperand, double maxError, string name){
    if (abs(compareOperand - toOperand) <= maxError){
        cout << name << " is within the accepted range." << endl;
        return true;
    } else {
        cout << name << " is not within the accepted range." << endl;
        return false;
    }
}

// END: 3b


// BEGIN: 4a
// Her skal du implementere ALLE funksjonene i oppgave 4a
double getUserInputTheta(){
    double theta;
    cout << "Enter the angle in degrees: ";
    cin >> theta;
    return theta;
}

double getUserInputInitVelocity(){
    double initVelocity;
    cout << "Enter the initial velocity: ";
    cin >> initVelocity;
    return initVelocity;
}

double degToRad(double deg){
    return deg * pi / 180;
}

double getVelocityX(double theta, double initVelocity){
    return initVelocity * cos(degToRad(theta));
}

double getVelocityY(double theta, double initVelocity) {
    return initVelocity * sin(degToRad(theta));
}

vector<double> getVelocityVector(double theta, double initVelocity){
    vector<double> velocityVector;
    velocityVector.push_back(getVelocityX(theta, initVelocity));
    velocityVector.push_back(getVelocityY(theta, initVelocity));
    return velocityVector;
}
// END: 4a

// BEGIN: 4b
double getDistanceTraveled(double velocityX, double velocityY) {
    double time = flightTime(velocityY);
    return posX(0, velocityX, time);
}
// END: 4b

// BEGIN: 4c
double targetPractice(double distanceToTarget, 
                        double velocityX, 
                        double velocityY) {
    double distance = getDistanceTraveled(velocityX, velocityY);
    return abs(distance - distanceToTarget);
}
// END: 4c


// BEGIN: 5b
void playTargetPractice() {
    int targetPosition = randomWithLimits(100, 1000);
    for (int i = 0; i < 10; ++i) {
        double theta = getUserInputTheta();
        double initVelocity = getUserInputInitVelocity();
        double velocityX = getVelocityX(theta, initVelocity);
        double velocityY = getVelocityY(theta, initVelocity);
        double distance = getDistanceTraveled(velocityX, velocityY);
        double time = flightTime(velocityY);
        double distanceToTarget = targetPractice(targetPosition, velocityX, velocityY);

        cout << "Attempt " << i + 1 << ": " << endl;
        printTime(time);
        cout << "Distance to target: " << distanceToTarget << " meters." << endl;

        if (distanceToTarget < 5) {
            cout << "Congratulations! You hit the target!" << endl;
            return;
        } else if (distance < targetPosition) {
            cout << "Your shot was too short." << endl;
        } else {
            cout << "Your shot was too long." << endl;
        }
    }
    cout << "Sorry, you did not hit the target. Better luck next time!" << endl;

 }
// END: 5b
