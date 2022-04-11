#include "book.hh"
#include <string>
#include <iostream>

Book::Book(std::string author, std::string title):
    author_(author), title_(title), is_loaned_(false), loan_day_(Date()), loan_end_(Date()) {
}

void Book::print()
{
    std::cout << author_ << " : " << title_ << std::endl;
    if (is_loaned_) {
        std::cout << "- loaned: ";
        loan_day_.print();

        std::cout << "- to be returned: ";
                  loan_end_.print();
    } else {
        std::cout << "- available" << std::endl;
    }

}

bool Book::loan(Date date)
{
    if (is_loaned_){
        std::cout << "Already loaned: cannot be loaned" << std::endl;
        return false;
    }
    is_loaned_ = true;
    loan_day_ = date;

    date.advance(28);
    loan_end_ = date;
    return true;
}

bool Book::renew()
{
    loan_end_.advance(28);
    return true;
}

bool Book::give_back()
{
    is_loaned_ = false;
    return true;
}
