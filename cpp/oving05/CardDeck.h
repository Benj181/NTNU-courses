#pragma once
#include "Card.h"
#include "std_lib_facilities.h"
#include <random>

// BEGIN: 3a
class CardDeck{
    private:
        void swap(size_t i, size_t j);
    public:
        CardDeck();
        vector<Card> cards;
        void print();
        void shuffle();
        Card drawCard();
};
// END: 3a
