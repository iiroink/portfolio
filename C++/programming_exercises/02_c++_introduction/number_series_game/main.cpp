#include <iostream>


int main()
{
    int numbers = 0;
    std::cout << "How many numbers would you like to have? ";
    std::cin >> numbers;

    for ( int count = 1; count <= numbers; ++count ) {

        if ( count % 21 == 0 ) {
            std::cout << "zip boing" << std::endl;
        } else if ( count % 3 == 0 ) {
            std::cout << "zip" << std::endl;
        } else if ( count % 7 == 0 ) {
            std::cout << "boing" << std::endl;
        } else {
            std::cout << count << std::endl;
        }

    }

    return 0;
}
