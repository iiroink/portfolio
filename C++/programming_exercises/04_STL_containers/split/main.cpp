#include <iostream>
#include <string>
#include <vector>


std::vector< std::string > split(std::string line, char separator, bool exclude_empty = false)
{
    std::vector< std::string > parts;
    std::string str = "";
    int counter = 0;

    for( char character : line )
    {
        if( character == separator )
        {
            if(exclude_empty && str == "") continue;

            parts.push_back(str);
            counter = 0;
            str = "";
            continue;
        }
        str += character;
        ++counter;
    }
    if(exclude_empty && str == "") return parts;

    parts.push_back(str);
    return parts;
}


int main()
{
    std::string line = "";
    std::cout << "Enter a string: ";
    getline(std::cin, line);
    std::cout << "Enter the separator character: ";
    char separator = getchar();

    std::vector< std::string > parts  = split(line, separator);
    std::cout << "Splitted string including empty parts: " << std::endl;
    for( auto part : parts ) {
        std::cout << part << std::endl;
    }

    std::vector< std::string > parts_no_empty  = split(line, separator, true);
    std::cout << "Splitted string ignoring empty parts: " << std::endl;
    for( auto part : parts_no_empty ) {
        std::cout << part << std::endl;
    }
}
