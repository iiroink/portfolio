#include <iostream>

using namespace std;

int main()
{
    int number = 0;
    cout << "Enter a number: ";
    cin >> number;

    int cube = 0;
    cube = number * number * number;

    int test = 0;
    test = cube / number / number;

    if ( number == test ) {
        cout << "The cube of " << number << " is " << cube << "." << endl;
    } else {
        cout << "The cube of " << number << " is not " << cube << "." <<  endl;
    }


    return 0;
}
