#include "Tasks.h"
#include "CardDeck.h"
#include "Entity.h"
#include "ImageAtlas.h"
#include "Pile.h"
#include "utils.h"
#include <filesystem>

#include <fstream>


// TASK: T3
bool inside_box(TDT4102::Point point, Rectangle rectangle) {
// BEGIN: T3
// Write your answer to assignment T3 here, between the //BEGIN: T3
// and // END: T3 comments. You should remove any code that is
// already there and replace it with your own.
    if (point.x > rectangle.top_left.x && point.x < rectangle.top_left.x + rectangle.width){
        if (point.y > rectangle.top_left.y && point.y < rectangle.top_left.y + rectangle.height){
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
// END: T3
}

// TASK: T4
void stack_set_flip(std::vector<Card> &stack) {
// BEGIN: T4
// Write your answer to assignment T4 here, between the //BEGIN: T4
// and // END: T4 comments. You should remove any code that is
// already there and replace it with your own.
    if (stack.size() == 0) {
        return;
    } else {
        stack.at(-1).set_flipped(true);
    }
// END: T4
}

// TASK: T6
std::filesystem::path get_card_image_path(const Card &card) {
// BEGIN: T6
// Write your answer to assignment T6 here, between the //BEGIN: T6
// and // END: T6 comments. You should remove any code that is
// already there and replace it with your own.
    return std::string{IMAGE_DIR} + card.get_identifier() + ".png";
// END: T6
}


// TASK: T8
bool can_push_to_tableau(const Card card, std::vector<Card> cards)
{
// BEGIN: T8
// Write your answer to assignment T8 here, between the //BEGIN: T8
// and // END: T8 comments. You should remove any code that is
// already there and replace it with your own.
    Card lastCard = cards.at(-1);
    if (cards.size() == 0){
        if (card.get_rank() == 13){
            return true;
        }
    } else {
        if (card.get_color() != lastCard.get_color() && card.get_rank() < lastCard.get_rank()){
            return true;
        }
    }
    return false;
// END: T8
}



// TASK: T9
bool is_valid_image_path(const std::filesystem::path &path) {
// BEGIN: T9
// Write your answer to assignment T9 here, between the //BEGIN: T9
// and // END: T9 comments. You should remove any code that is
// already there and replace it with your own.
    // ville først separert path med delimiter ".", deretter tatt siste element i 

    std::string imageType;
    // imageType == path.split(".").at(-1)
    std::vector<std::string> supportedImageTypes = {"png", "jpg", "bmp"};
    return std::ranges::find(supportedImageTypes, imageType) != supportedImageTypes.end();
// END: T9
}

// TASK: T11
// BEGIN: T11
// Write your answer to assignment T11 here, between the //BEGIN: T11
// and // END: T11 comments. You should remove any code that is
// already there and replace it with your own.
std::ostream& operator<<(std::ostream& os, const Card& card){
    os << card.get_identifier();
    return os;
}
// END: T11


// DO NOT TOUCH ANYTHING BELOW THIS POINT
void update_card_stack_positions(const TDT4102::Point anchor, std::vector<Card> &container) {
    auto pos = 0;
    for ( auto &card : container ) {
        int y_offset = pos++ * CARD_OVERLAP;


        card.set_position({anchor.x, anchor.y + y_offset});
    }
}



