#include "Card.h"

// BEGIN: 1c
string suitToString(const Suit suit){
    return SuitToStringMap.at(suit);
}

// END: 1c

// BEGIN: 1d
string rankToString(const Rank rank){
    return rankToStringMap.at(rank);
}

// END: 1d

// BEGIN: 2b
Card::Card(Suit suit, Rank rank): s{suit}, r{rank}{}  
// END: 2b

// BEGIN: 2c
Suit Card::getSuit(){
    return s;
}
// END: 2c

// BEGIN: 2d
Rank Card::getRank(){
    return r;
}
// END: 2d

// BEGIN: 2e
string Card::toString(){
    return rankToStringMap.at(r)  + " of "  + SuitToStringMap.at(s);
}
// END: 2e