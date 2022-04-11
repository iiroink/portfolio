#include "account.hh"
#include <iostream>
#include <string>

Account::Account(const std::string& owner, bool has_credit):
    owner_(owner), iban_("error"), balance_(0), has_credit_(has_credit), credit_limit_(0) {
    generate_iban();
}

void Account::print() const
{
    std::cout << owner_ << " : " << iban_ << " : " << balance_ << " euros" << std::endl;
}

bool Account::set_credit_limit(int limit)
{
    if (has_credit_ == false) {
        std::cout << "Cannot set credit limit: the account has no credit card" << std::endl;
        return false;
    }
    else {
        credit_limit_ = limit;
        return true;
    }
}

bool Account::save_money(int amount)
{
    if (amount < 0) return false;

    balance_ += amount;
    return true;
}

bool Account::take_money(int amount)
{
    if (amount < 0) return false;
    if (amount > balance_ + credit_limit_) {
        if (has_credit_ == true) std::cout << "Cannot take money: credit underflow" << std::endl;
        else std::cout << "Cannot take money: balance underflow" << std::endl;
        return false;
    }

    balance_ -= amount;
    std::cout << amount << " euros taken: new balance of " << iban_
              << " is " << balance_ << " euros" << std::endl;
    return true;
}

bool Account::transfer_to(Account& target, int amount)
{
    if (take_money(amount)) {
        target.save_money(amount);
        return true;
    } else {
        std::cout << "Transfer from " << iban_ << " failed" << std::endl;
        return false;
    }

}

// Setting initial value for the static attribute running_number_
int Account::running_number_ = 0;

void Account::generate_iban()
{
    ++running_number_;
    std::string suffix = "";
    if(running_number_ < 10)
    {
        suffix.append("0");
    }
    else if(running_number_ > 99)
    {
        std::cout << "Too many accounts" << std::endl;
    }
    suffix.append(std::to_string(running_number_));

    iban_ = "FI00 1234 ";
    iban_.append(suffix);
}
