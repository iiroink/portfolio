#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int number = 0;
    cout << "Enter a positive number: ";
    cin >> number;

    if ( number <= 0 ) {
        cout << "Only positive numbers accepted" << endl;
    } else {

        int factorial_1 = 1;
        int factorial_2 = number;

        int try_factorial_1 = 0;
        int try_factorial_2 = 0;

        for ( int try_number = 2; try_number < number; ++try_number) {
            if ( number % try_number == 0 ) {
                try_factorial_1 = try_number;
                try_factorial_2 = number / try_number;

                if ( abs(try_factorial_1 - try_factorial_2) < abs(factorial_1 - factorial_2) ){
                    factorial_1 = try_factorial_1;
                    factorial_2 = try_factorial_2;
                }
            }
        }

        cout << number << " = " << factorial_1 << " * " << factorial_2 << endl;

    }

    return 0;
}
