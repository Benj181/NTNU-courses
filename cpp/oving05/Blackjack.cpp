#include "Blackjack.h"


Blackjack::Blackjack(){
    deck.shuffle();
    drawDealerCard();
    drawDealerCard();
    dealerHandSum = getHandScore(dealerHand);
    drawPlayerCard();
    drawPlayerCard();
    playerHandSum = getHandScore(playerHand);
}

bool Blackjack::isAce(Card c){
    if (static_cast<int>(c.getRank()) == 14){
        return 1;
    } else {
        return 0;
    }
}

int Blackjack::getCardValue(Card c){
    if (static_cast<int>(c.getRank()) < 10){
        return static_cast<int>(c.getRank());
    } else if (isAce(c)) {
        return 11;
    } else {
        return 10;
    }
}

int Blackjack::getHandScore(vector<Card> hand){
    int score = 0;
    for (size_t i = 0; i < hand.size(); ++i){
        score += getCardValue(hand.at(i));
    }
    return score;
}

bool Blackjack::askPlayerDrawCard(){
    char choice;
    while(1){
        cout << "Hit [h] or stand [s]\n> ";
        cin >> choice;
        cout << "------------" << endl;
        if (choice == 'h'){
            return 1;
        } else if (choice == 's') {
            return 0;
        } else {
            cout << "Invalid choice" << endl;
        }
    }
}

void Blackjack::drawPlayerCard(){
    playerHand.push_back(deck.drawCard());
    playerHandSum = getHandScore(playerHand);
}

void Blackjack::drawDealerCard(){
    dealerHand.push_back(deck.drawCard());
    dealerHandSum = getHandScore(dealerHand);
}
string Blackjack::playerHandToString(){
    string prettyHand;
    for (size_t i = 0; i < playerHand.size(); i++){
        prettyHand += playerHand.at(i).toString();
        prettyHand += ", ";
    }
    return prettyHand;
}
string Blackjack::dealerHandToString(){
    string prettyHand;
    for (size_t i = 0; i < dealerHand.size() - 1; i++){
        prettyHand += dealerHand.at(i).toString();
        prettyHand += ", ";
    }
    return prettyHand;
}

void Blackjack::playGame(){
    while(1){
        cout << "On hand: " << playerHandToString()  << endl; 
        cout << "Dealers hand: " << dealerHandToString() << endl;
        if (askPlayerDrawCard()){
            drawPlayerCard();
        } else {
            break;
        }
    }

    cout << "You have " << playerHandSum << " points" << endl;
    cout << "The dealer have " << dealerHandSum << " points" << endl;
    if (dealerHandSum >= playerHandSum){
        cout << "You lost" << endl;
    } else {
        cout << "You win" << endl;
    }
}