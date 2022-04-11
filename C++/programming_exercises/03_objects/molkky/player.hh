#ifndef PLAYER_HH
#define PLAYER_HH
#include <string>


class Player
{
public:
    // Constructor
    Player(const std::string name);

    // Returns players name.
    std::string get_name();

    // Returns players points.
    int get_points();

    // Adds points to player total. If player ends
    // up with more than 50 points, sets them to 25.
    void add_points(int points);

    // Returns true if player has won the game.
    bool has_won();

private:
    std::string name_;
    int points_;
};

#endif // PLAYER_HH
