#include "CardDeck.h"

// BEGIN: 3b
CardDeck::CardDeck(){
    for (int i = 1; i <= 4; i++){
        for (int j = 2; j <= 14; j++){
            cards.push_back(Card {static_cast<Suit>(i), static_cast<Rank>(j)});
        }
    }
}
// END: 3b

// BEGIN: 3c
void CardDeck::swap(size_t  i, size_t j){
    std::swap(cards.at(i), cards.at(j));
}
// END: 3c

// BEGIN: 3d
void CardDeck::print(){
    for (Card c : CardDeck::cards){
        cout << c.toString() << endl;
    }
}
// END: 3d

// BEGIN: 3e
void CardDeck::shuffle(){
    std::random_device rd;
    std::mt19937 g(rd());
    std::uniform_int_distribution<size_t> dis(0, cards.size() - 1);

    for (size_t i = 0; i < cards.size(); ++i) {
        auto j = dis(g);
        swap(i, j);
    }
}
// END: 3e

// BEGIN: 3f
Card CardDeck::drawCard(){
    if (cards.empty()) {
        throw std::out_of_range("No cards left in the deck");
    }
    Card lastCard = cards.back();
    cards.pop_back();
    return lastCard;
}
// END: 3f
