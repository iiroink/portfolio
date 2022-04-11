/*  COMP.CS.100 Project 2: GAME STATISTICS
 *
 * Game statistics analyser.
 *
 * Reads the data from a file and offers tools to analyse it. The data is
 * expected to be in format game;player;score.
 *
 * Commands:
 * - ALL_GAMES - Prints all the different games.
 * - GAME <game_name> - Prints all scores and who got them for the game.
 * - ALL_PLAYERS - Prints all players.
 * - PLAYER <player_name> - Prints all the games that <player_name> has scores
 *   in.
 * - ADD_GAME <game_name> - Adds a new game.
 * - ADD_PLAYER <game_name> <player_name> <score> - Adds a new player and their
 *   score to a game. The game has to already exist. If player already exists,
 *   updates their score
 * - REMOVE_PLAYER <player_name> - Removes player and their scores from every
 *   game.
 *
 * Code written by
 * Name: Iiro Inkinen
 * Student number: 50393673
 * Username: vbiiin ( https://course-gitlab.tuni.fi/
 *                    comp.cs.110-ohj-2_2022-KEVAT/vbiiin )
 * E-Mail: iiro.inkinen@tuni.fi
 *
 * */
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <set>
#include <algorithm>

// Data structure to store games, players and scores.
using Games = std::map<std::string, std::map<std::string, int>>;

// Casual split func, if delim char is between "'s, ignores it.
std::vector<std::string> split( const std::string& str, char delim = ';' )
{
    std::vector<std::string> result = {""};
    bool inside_quatation = false;
    for ( auto current_char : str )
    {
        if ( current_char == '"' )
        {
            inside_quatation = not inside_quatation;
        }
        else if ( current_char == delim and not inside_quatation )
        {
            result.push_back("");
        }
        else
        {
            result.back().push_back(current_char);
        }
    }
    if ( result.back() == "" )
    {
        result.pop_back();
    }
    return result;
}

// Prints out all the different games in ASCII-order.
void allGames(const Games& games){
    std::cout << "All games in alphabetical order:" << std::endl;
    for (auto game : games) {
        std::cout << game.first << std::endl;
    }
}

// Prints out all scores and who got them for <game_name>.
void gameStats(const Games& games, const std::string& game_name){
    if (games.find(game_name) == games.end()){
        std::cout << "Error: Game could not be found." << std::endl;
    } else {
        std::cout << "Game " << game_name << " has these scores and players, "
                  << "listed in ascending order:" << std::endl;
        // Rearrange all players by their score.
        std::map<int, std::vector<std::string>> points = {};
        for (auto player_points : games.at(game_name)) {
            int score = player_points.second;
            std::string player = player_points.first;
            if (points.find(score) == points.end()) {
                points.insert({score, {}});
            }
            points.at(score).push_back(player);
        }
        // Print the scores.
        for (auto score : points) {
            std::cout << score.first << " : ";
            for (std::size_t i = 1; i < score.second.size(); ++i) {
                std::cout << score.second.at(i-1) << ", ";
            }
            std:: cout << score.second.back() << std::endl;
        }
    }
}

// Prints all players in ASCII-order.
void allPlayers(const Games& games) {
    std::cout << "All players in alphabetical order:" << std::endl;
    std::set<std::string> players = {};
    for (auto game : games) {
        for (auto player_points : game.second) {
            players.insert(player_points.first);
        }
    }
    for (auto player : players) {
        std::cout << player << std::endl;
    }
}

// Prints all the games that <player_name> has scores in.
void playerGames(const Games& games, const std::string& player_name) {
    std::set<std::string> player_games = {};
    for (auto game : games) {
        for (auto player_points : game.second) {
            if (player_points.first == player_name) {
                player_games.insert(game.first);
            }
        }
    }
    if (player_games.size() == 0) {
        std::cout << "Error: Player could not be found." << std::endl;
    } else {
        std::cout << "Player " << player_name << " playes the following games:"
                  << std::endl;
        for (auto game : player_games) {
            std::cout << game << std::endl;
        }
    }
}

// Adds a new game into the system.
void addGame(Games& games, const std::string& game_name) {
    if (games.find(game_name) != games.end()) {
        std::cout << "Error: Already exists." << std::endl;
    } else {
        games.insert({game_name, {}});
        std::cout << "Game was added." << std::endl;
    }
}

// Adds a new player and their score to a game. The game has to already exist.
// If player already exists, updates their score.
void addPlayer(Games& games, const std::string& game,
               const std::string& player, const int& points){
    // Game not found.
    if (games.find(game) == games.end()) {
        std::cout << "Error: Game could not be found." << std::endl;
    // Player not already in the system.
    } else if (games.at(game).find(player) == games.at(game).end()) {
        games.at(game).insert({player, points});
        std::cout << "Player was added." << std::endl;
    // Update the score of an existing player.
    } else {
        games.at(game).at(player) = points;
        std::cout << "Player was added." << std::endl;
    }
}

// Removes player and their scores from every game. Returns true if player was
// in the system.
bool removePlayer(Games& games, const std::string player) {
    bool found = false;
    for (auto game : games) {
        if (games.at(game.first).find(player) != games.at(game.first).end()) {
            games.at(game.first).erase(player);
            found = true;
        }
    }
    return found;
}

int main()
{
    std::string file_name = "";
    std::cout << "Give a name for input file: ";
    getline(std::cin, file_name);

    std::ifstream input_file(file_name);
    if (not input_file){
        std::cout << "Error: File could not be read." << std::endl;
        return EXIT_FAILURE;
    }

    // This structure will include the games, players and scores.
    Games games = {};
    std::string line = "";
    std::string game = "";
    std::string player = "";
    int points = 0;

    // Read the file.
    std::vector<std::string> parts = {};
    while (std::getline(input_file, line)) {
        parts = split(line);
        if (parts.size() != 3 or parts.at(0) == "" or parts.at(1) == "") {
            std::cout << "Error: Invalid format in file." << std::endl;
            return EXIT_FAILURE;
        }
        game = parts.at(0);
        player = parts.at(1);
        points = stoi(parts.at(2));
        if (games.find(game) == games.end()) {
            games.insert({game, {}});
        }
        games.at(game).insert({player, points});
    }
    input_file.close();
    // User interface.
    while (true) {
        std::string input_line = "";
        std::string command = "";
        std::cout << "games> ";
        getline(std::cin, input_line);
        if (input_line == "") {
            continue;
        }
        std::vector<std::string> input = {};
        input = split(input_line, ' ');
        for (char character : input.at(0)) {
            character = toupper(character);
            command.push_back(character);
        }
        if (command == "QUIT") {
            break;
        } else if (command == "ALL_GAMES") {
            allGames(games);
        } else if (command == "GAME" and input.size() >= 2) {
            gameStats(games, input.at(1));
        } else if (command == "ALL_PLAYERS") {
            allPlayers(games);
        } else if (command == "PLAYER" and input.size() >= 2) {
            playerGames(games, input.at(1));
        } else if (command == "ADD_GAME" and input.size() >= 2) {
            addGame(games, input.at(1));
        } else if (command == "ADD_PLAYER" and input.size() >= 4) {
            addPlayer(games, input.at(1), input.at(2), stoi(input.at(3)));
        } else if (command == "REMOVE" and input.size() >= 2) {
            if (removePlayer(games, input.at(1))) {
                std::cout << "Player was removed from all games." << std::endl;
            } else {
                std:: cout << "Error: Player could not be found." << std::endl;
            }
        } else {
            std::cout << "Error: Invalid input." << std::endl;
        }
    }

    return EXIT_SUCCESS;
}
