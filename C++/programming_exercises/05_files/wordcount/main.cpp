#include <iostream>
#include <string>
#include <map>
#include <set>
#include <fstream>

using namespace std;

int main()
{
    string inputFile;
    cout << "Input file: ";
    cin >> inputFile;

    ifstream inFile(inputFile);
    if ( not inFile ){
        cout << "Error! The file " << inputFile << " cannot be opened." << endl;
        return EXIT_FAILURE;
    }
    set<int> found;
    map<string, set<int>> wordcount;

    string row;
    int rownumber = 1;
    while (getline(inFile,row)) {
        size_t pos = row.find(" ");
        string run = row;
        string word;

        while (pos != string::npos){
            word = run.substr(0,pos);
            run = run.substr(pos+1);
            pos = run.find(" ");

            if (wordcount.find(word) == wordcount.end()){
                wordcount.insert({word, {rownumber}});
            } else {
                wordcount.at(word).insert(rownumber);
            }

        }
        word = run;
        if (wordcount.find(word) == wordcount.end()){
            wordcount.insert({word, {rownumber}});
        } else {
            wordcount.at(word).insert(rownumber);
        }
        ++rownumber;
    }

    for (auto word : wordcount){
        int occurance = word.second.size();
        cout << word.first << " "
             << occurance << ": ";

        set<int>::iterator iter = word.second.begin();
        cout << *iter;
        ++iter;

        while (iter != word.second.end()) {
            cout << ", " << *iter;
            ++iter;
        }
        cout << endl;

    }

    inFile.close();
    return EXIT_SUCCESS;
}
