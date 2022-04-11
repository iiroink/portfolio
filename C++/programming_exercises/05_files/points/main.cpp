#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
    string inputFile;
    cout << "Input file: ";
    cin >> inputFile;

    ifstream inFile(inputFile);
    if (not inFile)
    {
        cout << "Error! The file "<< inputFile << " cannot be opened." << endl;
        return EXIT_FAILURE;
    }
    map<string, int> scoresheet;

    string row;
    char divider = ':';
    while (getline(inFile, row))
    {
        string player;
        string points;
        int int_points;

        size_t pos = row.find(divider);
        player = row.substr(0, pos);
        points = row.substr(pos+1);
        int_points = stoi(points);

        if ( scoresheet.find(player) == scoresheet.end() )
        {
            scoresheet.insert( { player, int_points } );
        }
        else
        {
            scoresheet.at(player) += int_points;
        }
    }
    cout << "Final scores:" << endl;
    for ( auto pari : scoresheet )
    {
        cout << pari.first << ": " << pari.second << endl;
    }

    return EXIT_SUCCESS;
}
