#include <cstdlib>
#include <iostream>
#include <vector>


void read_integers(std::vector< int >& ints, int count)
{
    int new_integer = 0;
    for(int i = 0; i < count; ++i)
    {
        std::cin >> new_integer;
        ints.push_back(new_integer);
    }
}

bool same_values(const std::vector< int >& ints)
{
    for( int number : ints ) {
        if( number != ints.front() ) return false;
    }
    return true;
}

bool is_ordered_non_strict_ascending(const std::vector<int> ints)
{
    if(ints.size() == 1) return true;

    for( unsigned int count = 1; count < ints.size(); ++count ) {
        if( ints.at(count) < ints.at(count - 1) ) return false;
    }
    return true;
}

bool is_arithmetic_series(const std::vector<int> ints)
{
    if(ints.size() == 1) return true;

    int control;
    control = ints.at(1) - ints.front();
    for( unsigned int count = 1; count < ints.size(); ++count ) {
        if( ints.at(count) - ints.at(count - 1) != control ) return false;
    }
    return true;
}

bool is_geometric_series(const std::vector<int> ints)
{
    if(ints.size() == 1) return true;
    for( int number : ints ){
        if( number == 0 ) return false;
    }

    int control;
    control = ints.at(1) / ints.front();
    for( unsigned int count = 1; count < ints.size(); ++count ) {
        if( ints.at(count) / ints.at(count - 1) != control ) return false;
    }
    return true;
}



int main()
{
    std::cout << "How many integers are there? ";
    int how_many = 0;
    std::cin >> how_many;

    std::cout << "Enter the integers: ";
    std::vector<int> integers;
    read_integers(integers, how_many);

    if(same_values(integers))
        std::cout << "All the integers are the same" << std::endl;
    else
        std::cout << "All the integers are not the same" << std::endl;

    if(is_ordered_non_strict_ascending(integers))
        std::cout << "The integers are in a non-strict ascending order" << std::endl;
    else
        std::cout << "The integers are not in a non-strict ascending order" << std::endl;

    if(is_arithmetic_series(integers))
        std::cout << "The integers form an arithmetic series" << std::endl;
    else
        std::cout << "The integers do not form an arithmetic series" << std::endl;

    if(is_geometric_series(integers))
        std::cout << "The integers form a geometric series" << std::endl;
    else
        std::cout << "The integers do not form a geometric series" << std::endl;

    return EXIT_SUCCESS;
}
