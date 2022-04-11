/* Hitori
 *
 * Ohjelma toteuttaa Hitori-pelin yksinkertaisella käyttöliittymällä.
 *
 * Säännöt:
 * - Pelilauta on 5x5 ruudukko, jossa on numeroita 1-5.
 * - Tarkoituksena on poistaa numeroita niin, että kullekin riville ja
 * jokaiseen sarakkeeseen jää korkeintaan yksi kappale kutakin numeroa.
 * - Kahta vierekkäistä ruutua ei saa poistaa.
 * - Mikään numero ei saa jäädä irralleen muista niin, että sen sivuilla ja
 * ylä- sekä alapuolella on tyhjä ruutu.
 *
 * Toiminnallisuudet:
 * - Käyttäjä voi valita, täytetäänkö ruudukko satunnaisilla luvuilla vai
 * syöttääkö hän 25 lukua.
 * - Pelilauta tulostetaan näkyviin alussa ja jokaisen muutoksen jälkeen.
 * - Poistettava ruutu ilmoitetaan koordinaatteina, joiden on oltava numeroita
 * välillä 1-5. Tyhjää ruutua ei voi poistaa uudestaan.
 * - Peli päättyy automaattisesti
 *    - pelaajan tappioon, jos hän poistaa ruudun sääntöjen vastaisesti.
 *    - pelaajan voittoon, jos hän onnistuu poistamaan kaikkien numeroiden
 *    kaksoiskappaleet.
 * - Lopputulos kerrotaan pelaajalle.
 *
 * Ohjelman kirjoittaja
 * Nimi: Iiro Inkinen
 * Opiskelijanumero: 50393673
 * Käyttäjätunnus: vbiiin ( https://course-gitlab.tuni.fi/
 *                          comp.cs.110-ohj-2_2022-KEVAT/vbiiin )
 * E-Mail: iiro.inkinen@tuni.fi
 *
 * Huomioita ohjelmasta ja sen toteutuksesta:
 *
 * */

#include <iostream>
#include <vector>
#include <random>

using namespace std;

const unsigned int BOARD_SIDE = 5;
const unsigned char EMPTY = ' ';

// Muuttaa annetun numeerisen merkkijonon vastaavaksi kokonaisluvuksi
// (kutsumalla stoi-funktiota).
// Jos annettu merkkijono ei ole numeerinen, palauttaa nollan.
//
// Converts the given numeric string to the corresponding integer
// (by calling stoi).
// If the given string is not numeric, returns zero.
unsigned int stoi_with_check(const string& str)
{
    bool is_numeric = true;
    for(unsigned int i = 0; i < str.length(); ++i)
    {
        if(not isdigit(str.at(i)))
        {
            is_numeric = false;
            break;
        }
    }
    if(is_numeric)
    {
        return stoi(str);
    }
    else
    {
        return 0;
    }
}

// Tulostaa pelilaudan rivi- ja sarakenumeroineen.
//
// Prints the game board with row and column numbers.
void print(const vector< vector< int >>& gameboard)
{
    cout << "=================" << endl;
    cout << "|   | 1 2 3 4 5 |" << endl;
    cout << "-----------------" << endl;
    for(unsigned int i = 0; i < BOARD_SIDE; ++i)
    {
        cout << "| " << i + 1 << " | ";
        for(unsigned int j = 0; j < BOARD_SIDE; ++j)
        {
            if(gameboard.at(i).at(j) == 0)
            {
                cout << EMPTY << " ";
            }
            else
            {
                cout << gameboard.at(i).at(j) << " ";
            }
        }
        cout << "|" << endl;
    }
    cout << "=================" << endl;
}

// Generoi pelilaudalle numerot annetulla siemenluvulla.
void generate_board_numbers(vector< vector< int >>& gameboard)
{
    unsigned int seed;
    cout << "Enter seed value: ";
    cin >> seed;

    default_random_engine gen(seed);
    uniform_int_distribution<int> distr(1,5);

    unsigned int i;
    unsigned int j;
    for (i = 0; i < BOARD_SIDE; ++i)
    {
        vector< int > row;
        for (j = 0; j < BOARD_SIDE; ++j)
        {
            row.push_back(distr(gen));
        }
        gameboard.push_back(row);
    }
    print(gameboard);
}

// Luo pelilaudan käyttäjän syöttämillä numeroilla.
void read_board_numbers(vector< vector< int >>& gameboard)
{
    cout << "Input: ";
    unsigned int input;

    unsigned int i;
    unsigned int j;
    for (i = 0; i < BOARD_SIDE; ++i)
    {
        vector< int > row;
        for (j = 0; j < BOARD_SIDE; ++j)
        {
            cin >> input;
            row.push_back(input);
        }
        gameboard.push_back(row);
    }
    print(gameboard);
}

// Kysyy käyttäjältä koordinaatteja, kunnes ne ovat pelilaudan alueella, eikä
// ruutu ole tyhjä. Palauttaa true, kun koordinaatit on luettu onnistuneesti.
// Palauttaa false, jos käyttäjä syöttää "q" tai "Q".
bool read_coordinates(const vector< vector< int >>& gameboard,
                      unsigned int& x, unsigned int& y)
{
    string x_string;
    string y_string;
    while (true)
    {
        cout << "Enter removable element (x, y): ";
        cin >> x_string;
        // Syöte q lopettaa pelin kesken.
        if (x_string == "Q" or x_string == "q")
        {
            return false;
        }
        cin >> y_string;
        x = stoi_with_check(x_string);
        y = stoi_with_check(y_string);

        if (x < 1 or x > BOARD_SIDE or y < 1 or y > BOARD_SIDE)
        {
            cout << "Out of board" << endl;
            continue;
        }
        else if (gameboard.at(y-1).at(x-1) == 0)
        {
            cout << "Already removed" << endl;
            continue;
        }
        else
        {
            // Korjaa syötteen vastaamaan pelilaudan indeksointia.
            x -= 1;
            y -= 1;
            return true;
        }
    }
}

// Tekee voittotarkastelun ja tulostaa lopputuloksen. Palauttaa true, jos peli
// on päättynyt, muuten palauttaa false.
bool is_game_over(const vector< vector< int >>& gameboard,
               unsigned int& x, unsigned int& y)
{
    bool has_won = true;

    // Pelaaja häviää, jos poistetun ruudun vieressä on tyhjä ruutu.
    if (y != 0)
    {
        if (gameboard.at(y-1).at(x) == 0)
        {
            cout << "You lost" << endl;
            return true;
        }
    }
    if (y != 4)
    {
        if (gameboard.at(y+1).at(x) == 0)
        {
            cout << "You lost" << endl;
            return true;
        }
    }
    if (x != 0)
    {
        if (gameboard.at(y).at(x-1) == 0)
        {
            cout << "You lost" << endl;
            return true;
        }
    }
    if (x != 4)
    {
        if (gameboard.at(y).at(x+1) == 0)
        {
            cout << "You lost" << endl;
            return true;
        }
    }

    // Käy läpi pelilaudan kaikki ruudut.
    for (unsigned int i = 0; i < BOARD_SIDE; ++i)
    {
        for (unsigned int j = 0; j < BOARD_SIDE; ++j)
        {
            if (gameboard.at(i).at(j) == 0) continue;

            // Pelaaja ei ole voittanut, jos jollain numerolla on kaksoiskappale.
            for (unsigned int k = j + 1; k < BOARD_SIDE; ++k)
            {
                if (gameboard.at(i).at(j) == gameboard.at(i).at(k))
                {
                    has_won = false;
                }
            }
            for (unsigned int l = i + 1; l < BOARD_SIDE; ++l)
            {
                if (gameboard.at(i).at(j) == gameboard.at(l).at(j))
                {
                    has_won = false;
                }
            }
            // Pelaaja on hävinnyt, jos ruudun kaikki naapurit on tyhjiä.
            int neighbors = 0;
            int zeros = 0;
            if (i != 0)
            {
                neighbors += 1;
                if (gameboard.at(i-1).at(j) == 0)
                {
                    zeros += 1;
                }
            }
            if (i != 4)
            {
                neighbors += 1;
                if (gameboard.at(i+1).at(j) == 0)
                {
                    zeros += 1;
                }
            }
            if (j != 0)
            {
                neighbors += 1;
                if (gameboard.at(i).at(j-1) == 0)
                {
                    zeros += 1;
                }
            }
            if (j != 4)
            {
                neighbors += 1;
                if (gameboard.at(i).at(j+1) == 0)
                {
                    zeros += 1;
                }
            }
            if (neighbors - zeros == 0)
            {
                cout << "You lost" << endl;
                return true;
            }
        }
    }
    if (has_won)
    {
        cout << "You won" << endl;
        return true;
    }
    return false;
}

int main()
{
    // Pelilauta. Ulompi vektori sisältää rivit ja sisempi sarakkeet.
    vector< vector< int >> gameboard;

    // Pelin alku. Valitaan, täytetäänkö lauta satunnaisilla numeroilla vai
    // syötetäänkö ne itse.
    string choice;
    while (true)
    {
        cout << "Select start (R for random, I for input): ";
        getline(cin, choice);
        if (choice == "r" or choice == "R")
        {
            generate_board_numbers(gameboard);
            break;
        }
        else if (choice == "i" or choice == "I")
        {
            read_board_numbers(gameboard);
            break;
        }
    }
    // Ruutujen poisto. Luetaan koordinaatteja ja poistetaan niiden mukaisia
    // ruutuja kunnes peli päättyy.
    unsigned int x;
    unsigned int y;
    while (true)
    {
        // Erityistapaus: Syöte "q" tai "Q" lopettaa pelin kesken.
        if (not read_coordinates(gameboard, x, y))
        {
            cout << "Quitting" << endl;
            return 0;
        }
        gameboard.at(y).at(x) = 0;
        print(gameboard);
        if (is_game_over(gameboard, x, y))
        {
            break;
        }
    }

    return 0;
}
