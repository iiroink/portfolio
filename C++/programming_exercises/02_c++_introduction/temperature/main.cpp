#include <iostream>

using namespace std;

int main()
{
    double temp = 0;
    cout << "Enter a temperature: ";
    cin >> temp;

    double fahrenheit = 0;
    fahrenheit = temp * 1.8 + 32;

    cout << temp << " degrees Celsius is " << fahrenheit << " degrees Fahrenheit" << endl;

    double celsius = 0;
    celsius = (temp - 32) / 1.8;

    cout << temp << " degrees Fahrenheit is " << celsius << " degrees Celsius" << endl;

    return 0;
}
