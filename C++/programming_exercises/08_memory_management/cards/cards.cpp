#include "cards.hh"

Cards::Cards(): top_(nullptr) {
}

Card_data *Cards::get_topmost()
{
    return top_;
}

void Cards::add(int id)
{
    Card_data* new_card = new Card_data{id, nullptr};
    if (top_ == nullptr) {
        top_ = new_card;
    } else {
        new_card->next = top_;
        top_ = new_card;
    }
}

void Cards::print_from_top_to_bottom(std::ostream &s)
{
    if (top_ != nullptr){
        int count = 1;
        Card_data* card = top_;
        while (card->next != nullptr) {
            s << count << ": " << card->data << std::endl;
            card = card->next;
            ++ count;
        }
        s << count << ": " << card->data << std::endl;
    }
}

bool Cards::remove(int &id)
{
    if (top_ == nullptr) {
        return false;
    } else {
        id = top_->data;
        Card_data* to_delete = top_;
        top_ = top_->next;
        delete to_delete;
        return true;
    }
}

bool Cards::bottom_to_top()
{
    if (top_ == nullptr) {
        return false;
    } else if (top_->next == nullptr) {
        return true;
    } else {
        Card_data* card = top_;
        Card_data* bottom = card;
        while (card->next != nullptr) {
            bottom = card;
            card = card->next;
        }
        add(card->data);
        bottom->next = nullptr;
        delete card;

        return true;
    }
}

bool Cards::top_to_bottom()
{
    if (top_ == nullptr) {
        return false;
    } else if (top_->next == nullptr) {
        return true;
    } else {
        Card_data* card = top_;
        while (card->next != nullptr) {
            card = card->next;
        }
        Card_data* second = top_->next;
        card->next = top_;
        top_ = second;
        card->next->next = nullptr;

        return true;
    }
}

void Cards::print_from_bottom_to_top(std::ostream &s)
{
    if (top_ != nullptr) {
        recursive_print(top_, s);
    }
}

Cards::~Cards()
{
    while (top_ != nullptr) {
        Card_data* to_delete = top_;
        top_ = top_->next;
        delete to_delete;
    }
}

int Cards::recursive_print(Card_data *top, std::ostream &s)
{
    int row = 1;
    if (top->next != nullptr) {
        row = recursive_print(top->next, s);
    }
        s << row << ": " << top->data << std::endl;
        return row + 1;
}

