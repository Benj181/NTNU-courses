#include "Blackjack.h"


Blackjack::Blackjack(){
    deck.shuffle();
    drawDealerCard();
    drawDealerCard();
    drawPlayerCard();
    drawPlayerCard();
    dealerHandSum = getHandScore(dealerHand);
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
        return 0;
    } else {
        return 10;
    }
}

int Blackjack::getHandScore(vector<Card> hand){
    int score = 0;
    for (size_t i = 0; i < hand.size(); ++i){
        score += getCardValue(hand.at(i));
    }
    for (size_t i = 0; i < hand.size(); ++i){
        if (isAce(hand.at(i))){
            if (score < 11){
                score += 11;
            } else {
                score += 1;
            }
        }
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

string Blackjack::playerHandToString(bool last=false){
    string prettyHand;
    if(last){
        return playerHand.back().toString();
    } else {
        for (size_t i = 0; i < playerHand.size(); i++){
            prettyHand += playerHand.at(i).toString();
            prettyHand += ", ";
        }
        return prettyHand.substr(0, prettyHand.size() - 2);
    }
}

string Blackjack::dealerHandToString(){
    string prettyHand;
    for (size_t i = 0; i < dealerHand.size() - 1; i++){
        prettyHand += dealerHand.at(i).toString();
        prettyHand += ", ";
    }
    return prettyHand.substr(0, prettyHand.size() - 2);
}

void Blackjack::playGame(){
    while(1){ // game loop
        while(1){ // round loop
            if(dealerHandSum == 21){
                cout << "Dealers hand: " << dealerHandToString() << endl;
                cout << "Dealer have blackjack, You lose!" << endl;
                break;
            } else if(playerHandSum == 21){
                cout << "On hand: " << playerHandToString() << endl;
                cout << "You have blackjack, You win!" << endl;
                break;
            }

            cout << "Dealers hand: " << dealerHandToString() << endl;
            cout << "On hand: " << playerHandToString()  << endl; 
            
            if (askPlayerDrawCard()){ // Draws card
                drawPlayerCard();
                if (playerHandSum > 21){
                    cout << "You got a " << playerHandToString(true) << ", and gives score of " << playerHandSum << endl;
                    cout << "You lost!" << endl;          
                    break;
                } else {
                    cout << "You got a " << playerHandToString(true) << endl;
                }
            } else { // Stands
                while(dealerHandSum < 17){
                    drawDealerCard();
                    if (dealerHandSum > 21){
                        cout << "Dealer have a " << dealerHandSum << ", and loses!" << endl;
                        break;
                    }
                }
                cout << "You have a " << playerHandSum << endl;
                cout << "The dealer have a " << dealerHandSum  << endl;
                if (dealerHandSum >= playerHandSum){
                    cout << "You lost" << endl;
                } else {
                    cout << "You win" << endl;
                }
                break;
            }
        }


        char choice;
        cout << "Do you want to play again? (y/n)" << endl;
        cin >> choice;
        if (choice == 'y'){
            playerHand.clear();
            dealerHand.clear();
                drawDealerCard();
                drawDealerCard();
                dealerHandSum = getHandScore(dealerHand);
                drawPlayerCard();
                drawPlayerCard();
                playerHandSum = getHandScore(playerHand);
            continue;
        } else{
            break;
        }
    }
}