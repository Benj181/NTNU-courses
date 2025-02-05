#pragma once
#include "CardDeck.h"

class Blackjack{
    private:
        CardDeck deck{};
        vector<Card> playerHand;
        vector<Card> dealerHand;
        int playerHandSum;
        int dealerHandSum;
        bool isAce(Card c);
        int getCardValue(Card c);
        int getHandScore(vector<Card> hand);
        bool askPlayerDrawCard();
        void drawPlayerCard();
        void drawDealerCard();
        string playerHandToString();
        string dealerHandToString();
    public:
        Blackjack();
        void playGame();


};  