#ifndef BOOK_HH
#define BOOK_HH
#include <string>
#include "date.hh"


class Book
{
public:
    // Constructor
    Book(const std::string author, const std::string title);

    // Prints "auhtor : title" and that the book is
    // available or when it is to be returned.
    void print();

    // If the book is available, loans it and marks
    // loan to end in 28 days, returns true. If the
    // book is loaned prints an error message, returns
    // false.
    bool loan(Date date);

    // Moves the return date 28 days forward.
    bool renew();

    // Returns the book, making it available to loan.
    bool give_back();

private:
    std::string author_;
    std::string title_;
    bool is_loaned_;
    Date loan_day_;
    Date loan_end_;
};

#endif // BOOK_HH
