#pragma once
#include "bouncingBall.h"

// BEGIN: 4b
map<int, Color> ball_color = {
    {1, Color::blue},
    {2, Color::yellow},
    {3, Color::red},
    {4, Color::green}    
};
 
// END: 4b

// BEGIN: 4c
istream& operator>>(istream& is, Config& cfg){
    is >> cfg.color_up;
    is >> cfg.color_down;
    is >> cfg.velocity;
    return is;
}
// END: 4c

ostream& operator<<(ostream& os, Config& cfg){
    os << cfg.color_up << " ";
    os << cfg.color_down << " ";
    os << cfg.velocity << " ";
    return os;
}

constexpr Point BOUNCE_WINDOW_TOP_LEFT{50, 50};
constexpr int BOUNCE_WINDOW_WIDTH{800}; 
constexpr int BOUNCE_WINDOW_HEIGHT{500};

void bouncingBall(){
    AnimationWindow window{BOUNCE_WINDOW_TOP_LEFT.x, BOUNCE_WINDOW_TOP_LEFT.y, 
                           BOUNCE_WINDOW_WIDTH, BOUNCE_WINDOW_HEIGHT, "Bouncing ball"};
    
    Color color_up;
    Color color_down;
    Config slow;
    Config fast;
    const int radius{10};
    int alpha{1};
    int velocity{2};
    int x{0};
    int y{360};
    int increment_x{0};
    int increment_y{0};
    int count_num_passes{0};
    bool moving_down{true};


    // read in the configurations
    filesystem::path file_name{"konfigurasjon.txt"};
    ifstream is{file_name};
    is >> slow >> fast; 

    // initialise the run
    velocity = slow.velocity;
    color_up = ball_color.at(slow.color_up);
    color_down = ball_color.at(slow.color_down);

    while (!window.should_close()) {
        // determine increments based on the velocity
        increment_x = velocity * cos(alpha);
        increment_y = velocity * sin(alpha);

        // movement i x-direction
        if ((increment_x + x) + radius> window.width()) {
            // reached right side - wrap around to the leftmost
            x = 0;
            // increment counter which counts number of full left-to-right passes
            count_num_passes++;
            // alternate between slow and fast configuration every second pass
            if (count_num_passes % 2 == 0) {
                if (velocity == slow.velocity) {
                    velocity = fast.velocity;
                    color_up = ball_color.at(fast.color_up);
                    color_down = ball_color.at(fast.color_down);
                } else {
                    velocity = slow.velocity;
                    color_up = ball_color.at(slow.color_up);
                    color_down = ball_color.at(slow.color_down);
                }
            }
        } else {
            // moving rightwards
            x += increment_x;
        }

        
        // HINT 1: Ta en titt på koden ovenfor og se hvilke variabler som brukes. 
        // Bruk disse variablene for å implementere bevegelsen til den sprettende ballen. For eksempel:
        // Variablene count_bounce_top og count_bounce_bottom kan brukes
        // for å holde styr på hvilken retning ballen skal gå. 
        // Variabelen increment_y skal brukes for å øke y.
        
        // HINT 2: window.draw_circle({x, y}, r, c) tegner en sirkel med radius r, 
        // sentrum i (x, y) og fargen c
        
        // BEGIN: 4d
        // movement in y-direction
        if (moving_down){
            if ((increment_y + y) + radius > window.height()) {
                moving_down = false;
            } else {
                y += increment_y;
                window.draw_circle({x, y}, radius, color_down);
            }
        } else {
            if ((increment_y + y) - radius < 0) {
                moving_down = true;
            } else {
                y -= increment_y;
                window.draw_circle({x, y}, radius, color_up);
            }
        }
        // END: 4d
    
        window.next_frame();
    }
}