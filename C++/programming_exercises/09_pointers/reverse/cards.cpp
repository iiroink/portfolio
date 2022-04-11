#include <iostream>
#include <memory>
#include "cards.hh"


Cards::Cards(): top_( nullptr ) {
}


void Cards::add(int id) {
    std::shared_ptr<Card_data> new_card 
            = std::make_shared<Card_data>(Card_data{id, top_});
    top_ = new_card;
}

void Cards::print(std::ostream& s) {
   std::shared_ptr<Card_data> to_be_printed = top_;
   int nr = 1;

   while( to_be_printed != 0 ) {
      s << nr << ": " << to_be_printed->data << std::endl;
      to_be_printed = to_be_printed->next;
      ++nr;
   }
}

bool Cards::remove(int &id)
{
    if (!top_) return false;

    id = top_->data;
    top_ = top_->next;
    return true;
}

void Cards::reverse()
{
    if (top_ and top_->next) {
        std::shared_ptr<Card_data> prev_card( nullptr );
        std::shared_ptr<Card_data> card( top_ );
        std::shared_ptr<Card_data> next_card( nullptr );
        while (card) {
            next_card = card->next;
            card->next = prev_card;
            prev_card = card;
            card = next_card;
        }
        top_ = prev_card;
    }
}
