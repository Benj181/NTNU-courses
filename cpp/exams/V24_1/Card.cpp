#include "Card.h"
#include "common.h"


// TASK: T1
bool Card::is_flipped() const  {
// BEGIN: T1
// Write your answer to assignment T1 here, between the //BEGIN: T1
// and // END: T1 comments. You should remove any code that is
// already there and replace it with your own.
    return flipped;
// END: T1
}


// TASK: T2
CardColor Card::get_color() const {
// BEGIN: T2
// Write your answer to assignment T2 here, between the //BEGIN: T2
// and // END: T2 comments. You should remove any code that is
// already there and replace it with your own.
    if (suit == Suit::SPADES) {
        return CardColor::BLACK;
    } else if (suit == Suit::CLUBS) {
        return CardColor::BLACK;
    } else if (suit == Suit::HEARTS) {
        return CardColor::RED;
    } else {
        return CardColor::RED;
    }
// END: T2
}



// TASK: T5
std::string Card::get_identifier() const {
// BEGIN: T5
// Write your answer to assignment T5 here, between the //BEGIN: T5
// and // END: T5 comments. You should remove any code that is
// already there and replace it with your own.
    // have to include map: #include <map>
    std::map<Suit, char> to_char{
        {Suit::SPADES, 'S'},
        {Suit::CLUBS, 'C'},
        {Suit::HEARTS, 'H'}, 
        {Suit::DIAMONDS, 'D'}};
    std::string id = std::to_string(get_rank() + 1) + to_char[get_suit()];
    return id;
// END: T5
}



// ========================================
// Do not touch anything below this point
// ========================================

Card::Card(int rank, Suit suit_) : rank{rank}, suit{suit_} {
    set_width(CARD_WIDTH);
    set_height(CARD_HEIGHT);
};


Card::Card(int rank, Suit suit_, Point pos) : Card(rank, suit_) {
    set_width(CARD_WIDTH);
    set_height(CARD_HEIGHT);
    set_position(pos);
};


int Card::get_rank() const {
    return rank;
}

Suit Card::get_suit() const {
    return suit;
}

void Card::set_flipped(bool flipped_)  {
    flipped = flipped_;
}

void Card::flip() {
    flipped = ! flipped;
}

int Card::CARD_WIDTH = 60;
int Card::CARD_HEIGHT = 89;



