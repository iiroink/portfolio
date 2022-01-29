#include <iostream>

using namespace std;

int is_positive(int number) {
    if( number > 0 ) {
        return 1;
    }
    else {
        return 0;
    }
}

double factorial(double number) {
    double total = 1;
    while (number > 0) {
        total *= number;
        --number;
    }

    return total;
}

double lotto_probability(int total_balls, int draw_balls) {
    double numerator = 0;
    double denominator = 0;

    numerator = factorial(total_balls);
    denominator = factorial(total_balls - draw_balls) * factorial(draw_balls);

    return (numerator / denominator);
}

int main()
{
    unsigned long int total_balls = 0;
    cout << "Enter the total number of lottery balls: ";
    cin >> total_balls;

    unsigned long int draw_balls = 0;
    cout << "Enter the number of drawn balls: ";
    cin >> draw_balls;

    if ( is_positive(total_balls) == 0 or is_positive(draw_balls) == 0 ){
        cout << "The number of balls must be a positive number." << endl;
        return 0;
    }else if ( draw_balls > total_balls ){
        cout << "The maximum number of drawn balls is the total amount of balls." << endl;
        return 0;
    }

    double probability = 0;
    probability = lotto_probability(total_balls, draw_balls);

    cout << "The probability of guessing all " << draw_balls << " balls correctly is 1/" << probability << endl;

    return 0;
}
