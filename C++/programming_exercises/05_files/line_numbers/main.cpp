#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    string inputFile;
    cout << "Input file: ";
    cin >> inputFile;

    string outputFile;
    cout << "Output file: ";
    cin >> outputFile;

    ifstream inputObject(inputFile);
    if ( not inputObject ) {
        cout << "Error! The file " << inputFile << " cannot be opened." << endl;
        return EXIT_FAILURE;
    }
    ofstream outputObject(outputFile);
    string row;
    int rowNumber = 1;
    while(getline(inputObject, row)) {
        outputObject << rowNumber << " " << row << endl;
        ++ rowNumber;
    }
    inputObject.close();
    return EXIT_SUCCESS;
}
