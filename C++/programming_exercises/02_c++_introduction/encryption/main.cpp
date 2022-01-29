#include <iostream>
#include <string>
#include <cctype>

using namespace std;

void encrypter(string text, string key)
{
    int text_length = text.length();
    int ascii = 0;
    int place = 0;

    cout << "Encrypted text: ";

    for (int i = 0; i < text_length; ++i){
        ascii = static_cast< int >(text.at(i));
        place = ascii - 97;
        cout << key.at(place);
    }
    cout << endl;
}

int main()
{
    string key = "";
    cout << "Enter the encryption key: ";
    cin >> key;

    if (key.length() != 26) {
        cout << "Error! The encryption key must contain 26 characters." << endl;
        return EXIT_FAILURE;
    }
    char help = ' ';
    for (int i = 0; i < 26; ++i){
        help = key.at(i);
        if (!(islower(help))) {
            cout << "Error! The encryption key must contain only lower case characters." << endl;
            return EXIT_FAILURE;
        }
    }

    for (char character = 97; character <= 122; ++character) {
        string::size_type place = 0;
        place = key.find(character);

        if (place == string::npos) {
            cout << "Error! The encryption key must contain all alphabets a-z." << endl;
            return EXIT_FAILURE;
        }
    }

    cout << "Enter the text to be encrypted: ";
    string text = "";
    cin >> text;

    int text_lenght = text.length();

    for (int i = 0; i < text_lenght; ++i){
        help = text.at(i);
        if (!(islower(help))) {
            cout << "Error! The text to be encrypted must contain only lower case characters." << endl;
            return EXIT_FAILURE;
        }
    }

    encrypter(text, key);

    return 0;
}
