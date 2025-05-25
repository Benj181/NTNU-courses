#include <iostream>
#include <unistd.h>

// ------------------------------------------------------------
#include "Renderers.h"
#include "BoardGame.h"
#include "Board.h"
#include "Tasks.h"
#include "AnimationWindow.h"
#include "Color.h"
#include "widgets/DropdownList.h"
#include "widgets/Button.h"


using Point = TDT4102::Point;
using Color = TDT4102::Color;


std::ostream &operator<<(std::ostream &os, const TDT4102::Point pt)
{
    return os << pt.x  << ", " << pt.y;
}

std::unique_ptr<TDT4102::DropdownList> list{};
std::unique_ptr<BoardGame> game_ptr{};


int main() {

    if ( equality_operator_presence_point() ) {
        std::cout << "TDT4102::Point equality overload in use!" << "\n";
    }

    std::vector<std::string> options{"6", "8", "10", "12" };
    list = std::unique_ptr<TDT4102::DropdownList>(new TDT4102::DropdownList{{0,0}, 200, 40, options});


    TDT4102::Button btn{{200,0}, 100, 40, "Reset"};

    btn.setCallback(reset_button_callback);

    // Load atlas images
    ImageAtlas::getInstance().add_image(player_key(Player::ONE), "images/checker-chip001.png");
    ImageAtlas::getInstance().add_image(player_key(Player::TWO), "images/checker-chip002.png");
    ImageAtlas::getInstance().add_image(player_key(Player::NONE), "images/checker-chip002.png");

    // Load images
    auto window = TDT4102::AnimationWindow{50, 50, 1024, 768, "AnimationWindow"};

    window.add(*list);
    window.add(btn);


    game_ptr = std::unique_ptr<BoardGame>(new BoardGame{8});;

    BoardGame &game = *game_ptr;
    game = load_board("state");
    game.set_position({200,50});

    bool lmb_state[2] = {false, false};



    while ( ! window.should_close() )
    {
        auto cursor_position = window.get_mouse_coordinates();

        lmb_state[1] = lmb_state[0];
        lmb_state[0] = window.is_left_mouse_button_down();

        bool lmb_click = lmb_state[0] != lmb_state[1] && lmb_state[1] == false;
        bool lmb_held = lmb_state[0] == lmb_state[1] && lmb_state[1] == true;
        bool lmb_released = lmb_state[0] != lmb_state[1] && lmb_state[1] == true;

        if ( lmb_click ) {
            game.interact(cursor_position);
        }

        window.next_frame();

        game.set_width(window.width() - 250);
        game.set_height(window.height() - 100);

        auto counts = count_chips(game.board.get_cells());

        BoardRenderer::render(window, game, game.get_position());

        if ( game.get_winner() == Player::NONE ) {

            ChipRenderer::render(window, {20,50}, game.get_current_player(), 30, 30);

            window.draw_text({50,50}, "Player " + player_key(game.get_current_player()) + "'s turn", TDT4102::Color::black, 20);
        } else {
            auto halfway = window.height() / 2 - 80 / 2;

            window.draw_rectangle({50, halfway - 60}, window.width() - 100, 200, TDT4102::Color::black);
            window.draw_text({50,halfway}, "Player " + player_key(game.get_winner()) + " has won!", TDT4102::Color::white, 80);
        }

        const int chipCountSz = 40;
        const int chipCountPad = 5;

        ChipRenderer::render(window, {0, window.height() - 50 - chipCountSz}, Player::ONE, chipCountSz, chipCountSz);
        window.draw_text({chipCountSz, window.height() - 50 - chipCountSz}, std::to_string(counts.first), TDT4102::Color::black, chipCountSz);
        ChipRenderer::render(window, {0, window.height() - 50 - 2*(chipCountPad + chipCountSz)}, Player::TWO, chipCountSz, chipCountSz);
        window.draw_text({chipCountSz, window.height() - 50 - 2*(chipCountPad + chipCountSz)}, std::to_string(counts.second), TDT4102::Color::black, chipCountSz);
    }

    return 0;
}
