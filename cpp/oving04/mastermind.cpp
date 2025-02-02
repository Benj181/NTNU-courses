#include "mastermind.h"

// BEGIN: 4
void playMastermind(){
    constexpr int size = 4;
    constexpr int letters = 6;
    string code;
    string guess;
    code = randomizeString(size, 'A', 'A' + letters - 1);
    cout << code << endl;
    guess = readInputToString(size, 'A', 'A' + letters - 1);
    cout << guess << endl;
    
}
// END: 4

// BEGIN: 4e
int checkCharactersAndPosition(const string &code, const string &guess){
    int count = 0;
    for (int i; i < code.length(); i++){
        if (code[i] == guess[i]){
            count++;
        }
    }
    return count;
}
// END: 4e

// BEGIN: 4f
int checkCharacters(const string &code, const string &guess){
    return 0;
}
///*returverdi*/ checkCharacters(/*param 1: code, param 2: guess*/) {}
// END: 4f
