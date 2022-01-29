"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 50393673
Name:       Iiro Inkinen
Email:      iiro.inkinen@tuni.fi

Blackjack-game with graphical user interface.
Advanced gui

Rules:
- Player vs. Dealer (House).
- Face cards are worth 10, Aces 11 or 1 and the rest their face value.
- The goal is to get as close to 21 without going over (busting).
- Player is dealt two cards face up, dealer one face up and one face down.
- If player has 21 from the deal it's "Blackjack" and they win.
- Otherwise the player can:
    - Hit: Take a card and add it to the total. If the points in players hand
      exceed 21, they lose (bust).
    - Stand: End their actions and start dealers turn.
- Dealer will hit until they have 17 or more points in their hand.
- If dealer busts, player wins.
- When both have finished their turn, the one with higher points wins. (Dealer
  wins in case of a tie)
- If either player gets 5 cards in their hand without busting, they win (5 card
  Charlie)

Actions in the gui:
- Menu:
    - "New Game" resets points and deck(s)
    - "Options" -> "Show ideal move" enables text that tells player the best
      move in given situation.
    - "Quit" closes the game.
- "Hit" gives player a card.
- "Stand" ends players turn.
- "Deal" starts a new round.

Pictures of the playing cards:
http://byronknoll.blogspot.com/2011/03/vector-playing-cards.html
"""

from tkinter import *
import random

# Variable for the number of decks in one shoe.
SHOE_SIZE = 6
# Matrix of the ideal moves that aren't obvious. Rows are dealer cards 1-10 and
# columns are player total points 12-16.
HINTS = [0,
         ["hit", "hit", "hit", "hit", "hit"],
         ["hit", "stand", "stand", "stand", "stand"],
         ["hit", "stand", "stand", "stand", "stand"],
         ["stand", "stand", "stand", "stand", "stand"],
         ["stand", "stand", "stand", "stand", "stand"],
         ["stand", "stand", "stand", "stand", "stand"],
         ["hit", "hit", "hit", "hit", "hit"],
         ["hit", "hit", "hit", "hit", "hit"],
         ["hit", "hit", "hit", "hit", "hit"],
         ["hit", "hit", "hit", "hit", "hit"]]


class Userinterface:
    def __init__(self):
        self.__mainw = Tk()
        self.__mainw.title("Black Jack")

        # The menu
        menu = Menu(self.__mainw)
        self.__mainw.config(menu=menu)
        options = Menu(menu, tearoff=0)

        # New Game button
        menu.add_command(label="New Game", command=self.new_game)

        # Drop-menu for Options
        menu.add_cascade(label="Options", menu=options)
        # Currently has only one option, Show ideal move.
        self.__hints = IntVar()
        options.add_checkbutton(label="Show ideal move", variable=self.__hints,
                                onvalue=1, offvalue=0)

        # Quit button
        menu.add_command(label="Quit", command=self.quit)

        # Set a bigger font for rest of the texts.
        self.__mainw.option_add("*Font", "Verdana 24")

        # The pictures of the playing cards will be stored here. They can be
        # retrieved with <self.__card_photos["suit"][number]>. Number 0 is
        # the card back.
        self.__card_photos = {}
        self.__card_photos["hearts"] = []
        self.__card_photos["diamonds"] = []
        self.__card_photos["clubs"] = []
        self.__card_photos["spades"] = []

        # Adds the pictures into the matrix. Assumes that the files are named
        # "value_of_suit.png"
        for suit in self.__card_photos:
            # Card back to value 0 of every suit.
            card_back = "card_back.png"
            self.__card_photos[suit].append(PhotoImage(file=card_back))

            # Ace to value 1
            ace = f"ace_of_{suit}.png"
            self.__card_photos[suit].append(PhotoImage(file=ace))

            # Cards 2-10
            counter = 2
            while counter <= 10:
                card_photo = f"{counter}_of_{suit}.png"
                self.__card_photos[suit].append(PhotoImage(file=card_photo))
                counter += 1

            # Jack, Queen and King
            for card in ["jack", "queen", "king"]:
                card_photo = f"{card}_of_{suit}.png"
                self.__card_photos[suit].append(PhotoImage(file=card_photo))

        # Create a deck of playing cards.
        self.__suits = ["hearts", "diamonds", "clubs", "spades"]
        self.__numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        # This will store the cards that are in the deck. With
        # <self.__card_photos["suit"][number]> you'll get the number of copies
        # of the said card still in the deck.
        self.__deck = {}

        for suit in self.__suits:
            self.__deck[suit] = {}

            for number in self.__numbers:
                # The format is best seen here. SHOE_SIZE changes the number
                # of decks.
                self.__deck[suit][number] = SHOE_SIZE

        # Dealer and player have no cards or points in the beginning.
        self.__dealer_cards = []
        self.__player_cards = []
        self.__player_score = 0
        self.__dealer_score = 0

        # Both players can draw up to five cards. Initialize places for the
        # pictures.
        self.__d1_photo = Label()
        self.__d2_photo = Label()
        self.__d3_photo = Label()
        self.__d4_photo = Label()
        self.__d5_photo = Label()

        self.__p1_photo = Label()
        self.__p2_photo = Label()
        self.__p3_photo = Label()
        self.__p4_photo = Label()
        self.__p5_photo = Label()

        self.__d1_photo.grid(row=1, column=0)
        self.__d2_photo.grid(row=1, column=1)
        self.__d3_photo.grid(row=1, column=2)
        self.__d4_photo.grid(row=1, column=3)
        self.__d5_photo.grid(row=1, column=4)

        self.__p1_photo.grid(row=4, column=0)
        self.__p2_photo.grid(row=4, column=1)
        self.__p3_photo.grid(row=4, column=2)
        self.__p4_photo.grid(row=4, column=3)
        self.__p5_photo.grid(row=4, column=4)

        # All the texts in the gui.
        self.__dealer_text = Label(text=f"Dealer:")
        self.__player_text = Label(text=f"You:")
        self.__info_text = Label(text="Welcome, let's play!",
                                 foreground="magenta")
        self.__result_text = Label(foreground="lime")
        self.__score_text = Label(text="Wins:")
        self.__player_score_text = Label(text="Player: 0")
        self.__dealer_score_text = Label(text="House: 0")
        self.__hint_text = Label(text="")

        self.__dealer_text.grid(row=0, column=0, columnspan=2)
        self.__player_text.grid(row=3, column=0, columnspan=2)
        self.__info_text.grid(row=2, column=0, columnspan=2)
        self.__result_text.grid(row=2, column=2, columnspan=2)
        self.__score_text.grid(row=0, column=6)
        self.__player_score_text.grid(row=1, column=5)
        self.__dealer_score_text.grid(row=1, column=7)
        self.__hint_text.grid(row=5, column=4, columnspan=3)

        # The three action buttons.
        self.__hit_button = Button(text="Hit", command=self.hit)
        self.__stand_button = Button(text="Stand", command=self.stand)
        self.__next_round_button = Button(text="Deal", state=DISABLED,
                                          command=self.next_round)

        self.__hit_button.grid(row=6, column=0, sticky=E+W)
        self.__stand_button.grid(row=6, column=1, sticky=E+W)
        self.__next_round_button.grid(row=6, column=2, sticky=E+W)

        # Set minimum sizes for rows and columns to keep the elements from
        # bobbing around.
        self.__mainw.grid_rowconfigure(2, minsize=130)
        self.__mainw.grid_rowconfigure(5, minsize=70)

        self.__mainw.grid_columnconfigure(0, minsize=210)
        self.__mainw.grid_columnconfigure(1, minsize=210)
        self.__mainw.grid_columnconfigure(2, minsize=210)
        self.__mainw.grid_columnconfigure(3, minsize=210)
        self.__mainw.grid_columnconfigure(4, minsize=210)

        # Variable to control whose turn it is.
        self.__dealers_turn = False

        # Deal the first hand.
        self.deal()

        self.__mainw.mainloop()

    def deal(self):
        """
        Deals a hand. (=two cards face up for player, one face up and one face
        down for the dealer). Also checks if Blackjack is dealt to player.
        Orders a reshuffle of the deck if the deck doesn't have enough cards
        for a full round.
        """
        # Checks the number of cards in the deck.
        remaining_cards = 0
        for suit in self.__deck:
            for card in self.__deck[suit]:
                remaining_cards += self.__deck[suit][card]

        # Orders a reshuffle if there are less than 10 cards in the deck.
        if remaining_cards < 10:
            self.__info_text.configure(text="Out of cards, reshuffled")
            self.out_of_cards()

        # Deals dealer and player both two cards.
        self.__dealer_cards.append(self.random_card())
        self.__dealer_cards.append(self.random_card())

        self.__player_cards.append(self.random_card())
        self.__player_cards.append(self.random_card())

        # This is only the card back to hide the dealers first card.
        self.__d1_photo.configure(
            image=self.__card_photos["hearts"][0])

        # Display images of the rest of the dealt cards.
        self.__d2_photo.configure(
            image=self.__card_photos[self.__dealer_cards[1][0]]
            [self.__dealer_cards[1][1]])

        self.__p1_photo.configure(
            image=self.__card_photos[self.__player_cards[0][0]]
            [self.__player_cards[0][1]])

        self.__p2_photo.configure(
            image=self.__card_photos[self.__player_cards[1][0]]
            [self.__player_cards[1][1]])

        # If player has 21 points from the deal, they win immediately.
        if self.check_total("Player") == 21:
            self.__info_text.configure(text="BLACK JACK!")
            self.has_won("blacjack")

        # Calls the total checker for the dealer also to update the points.
        self.check_total("Dealer")

        # If hints are turned on, tells player the ideal move.
        if self.__hints.get() == 1:
            self.ideal_move()

    def hit(self):
        """
        Method for the action "Hit". Deals a card for player. Also checks if
        player busts from the hit. Allows for a maximum of five cards to be
        dealt to player.
        """
        new_card = self.random_card()
        self.__player_cards.append(new_card)

        # Variable for controlling the number of cards.
        max_cards = False

        # Displays the picture of the card dealt.
        if len(self.__player_cards) == 3:
            self.__p3_photo.configure(
                image=self.__card_photos[self.__player_cards[2][0]]
                [self.__player_cards[2][1]])

        elif len(self.__player_cards) == 4:
            self.__p4_photo.configure(
                image=self.__card_photos[self.__player_cards[3][0]]
                [self.__player_cards[3][1]])

        elif len(self.__player_cards) == 5:
            self.__p5_photo.configure(
                image=self.__card_photos[self.__player_cards[4][0]]
                [self.__player_cards[4][1]])
            # If five cards are dealt, no more will be allowed.
            max_cards = True

        # Checks for bust, in which case player loses immediately.
        if self.check_total("Player") > 21:
            self.__info_text.configure(text="Bust")
            self.has_won("bust")

        # If player draws 5 cards without busting they win.
        elif max_cards:
            self.has_won("charlie")

        # If hints are turned on, tells player the ideal move.
        elif self.__hints.get() == 1:
            self.ideal_move()

    def stand(self):
        """
        Method for the action "Stand". Ends players turn and deals cards to the
        dealer until they have 17 or more points.
        """
        self.__dealers_turn = True
        # Reveal the card that was face down.
        self.__d1_photo.configure(
            image=self.__card_photos[self.__dealer_cards[0][0]]
            [self.__dealer_cards[0][1]])

        # Deals cards until dealer has 17 or more points.
        while True:

            total = self.check_total("Dealer")
            if total >= 17:
                break

            new_card = self.random_card()
            self.__dealer_cards.append(new_card)

            # Displays the picture of the card dealt.
            if len(self.__dealer_cards) == 3:
                self.__d3_photo.configure(
                    image=self.__card_photos[self.__dealer_cards[2][0]]
                    [self.__dealer_cards[2][1]])

            elif len(self.__dealer_cards) == 4:
                self.__d4_photo.configure(
                    image=self.__card_photos[self.__dealer_cards[3][0]]
                    [self.__dealer_cards[3][1]])

            elif len(self.__dealer_cards) == 5:
                self.__d5_photo.configure(
                    image=self.__card_photos[self.__dealer_cards[4][0]]
                    [self.__dealer_cards[4][1]])
                # If five cards are dealt, no more are allowed.
                self.check_total("Dealer")
                break

        # Both player have finished their turn, chek who won.
        self.has_won()

    def random_card(self):
        """
        Chooses a random card and checks that it's still in the deck. If not,
        draws new ones until a card that is in the deck is found. Then removes
        the card from the deck. Assumes that this method won't be called when
        the deck is empty.

        :return: str, int, the suit and number of the random card.
        """
        while True:
            suit = random.choice(self.__suits)
            card = random.choice(self.__numbers)

            if self.__deck[suit][card] != 0:
                self.__deck[suit][card] -= 1
                break

        return suit, card

    def check_total(self, person):
        """

        """
        if person == "Player":
            cards = self.__player_cards
            text = self.__player_text

        else:
            text = self.__dealer_text

            if not self.__dealers_turn:
                cards = self.__dealer_cards[1:]
            else:
                cards = self.__dealer_cards

        total = 0
        ace = 0

        for card in cards:

            if card[1] > 10:
                points = 10

            elif card[1] == 1:
                ace += 1
                points = 0

            else:
                points = card[1]

            total += points

        for card in range(ace):

            if total + 11 > 21:
                total += 1
            else:
                total += 11

        text.configure(text=f"{person}: {total}")

        return total

    def ideal_move(self):
        player_total = self.check_total("Player")
        dealer_total = self.check_total("Dealer")

        if dealer_total == 11:
            dealer_total = 1

        if player_total < 12:
            move = "hit"

        elif player_total > 16:
            move = "stand"

        else:
            player_total -= 12
            move = HINTS[dealer_total][player_total]

        self.__hint_text.configure(text=f"You should {move}.")

    def has_won(self, reason=""):

        if reason == "blacjack":
            self.__result_text.configure(text="You won!")
            self.__player_score += 1

        elif reason == "bust":
            self.__result_text.configure(text="House wins!")
            self.__dealer_score += 1

        elif reason == "charlie":
            self.__info_text.configure(text="5 card Charlie")
            self.__result_text.configure(text="You won!")
            self.__player_score += 1

        else:
            if self.check_total("Dealer") > 21:
                self.__info_text.configure(text="House busts")
                self.__result_text.configure(text="You won!")
                self.__player_score += 1

            elif len(self.__dealer_cards) == 5:
                self.__info_text.configure(text="5 card Charlie")
                self.__result_text.configure(text="House wins!")
                self.__dealer_score += 1

            elif self.check_total("Dealer") < self.check_total("Player"):
                self.__info_text.configure(text="You have a bigger hand")
                self.__result_text.configure(text="You won!")
                self.__player_score += 1

            else:
                self.__info_text.configure(text="House has a bigger hand")
                self.__result_text.configure(text="House wins!")
                self.__dealer_score += 1

        self.end_of_round()

    def end_of_round(self):
        self.__player_score_text.configure(text=f"Player: {self.__player_score}")
        self.__dealer_score_text.configure(text=f"House: {self.__dealer_score}")
        self.__hint_text.configure(text="")

        self.__hit_button.configure(state=DISABLED)
        self.__stand_button.configure(state=DISABLED)
        self.__next_round_button.configure(state=NORMAL)

    def next_round(self):
        empty_image = PhotoImage(width=150, height=218)

        self.__d1_photo.configure(image=empty_image)
        self.__d2_photo.configure(image=empty_image)
        self.__d3_photo.configure(image=empty_image)
        self.__d4_photo.configure(image=empty_image)
        self.__d5_photo.configure(image=empty_image)

        self.__p1_photo.configure(image=empty_image)
        self.__p2_photo.configure(image=empty_image)
        self.__p3_photo.configure(image=empty_image)
        self.__p4_photo.configure(image=empty_image)
        self.__p5_photo.configure(image=empty_image)

        self.__dealers_turn = False
        self.__info_text.configure(text="New hand!")
        self.__result_text.configure(text="")

        self.__hit_button.configure(state=NORMAL)
        self.__stand_button.configure(state=NORMAL)
        self.__next_round_button.configure(state=DISABLED)

        self.__player_cards = []
        self.__dealer_cards = []
        self.deal()

    def new_game(self):
        for suit in self.__suits:
            self.__deck[suit] = {}

            for number in self.__numbers:
                self.__deck[suit][number] = SHOE_SIZE

        empty_image = PhotoImage(width=150, height=218)

        self.__d1_photo.configure(image=empty_image)
        self.__d2_photo.configure(image=empty_image)
        self.__d3_photo.configure(image=empty_image)
        self.__d4_photo.configure(image=empty_image)
        self.__d5_photo.configure(image=empty_image)

        self.__p1_photo.configure(image=empty_image)
        self.__p2_photo.configure(image=empty_image)
        self.__p3_photo.configure(image=empty_image)
        self.__p4_photo.configure(image=empty_image)
        self.__p5_photo.configure(image=empty_image)

        self.__dealers_turn = False
        self.__info_text.configure(text="Welcome, let's play!")
        self.__result_text.configure(text="")

        self.__player_score = 0
        self.__dealer_score = 0
        self.__player_score_text.configure(text="Player: 0")
        self.__dealer_score_text.configure(text="House: 0")

        self.__hit_button.configure(state=NORMAL)
        self.__stand_button.configure(state=NORMAL)
        self.__next_round_button.configure(state=DISABLED)

        self.__player_cards = []
        self.__dealer_cards = []
        self.deal()

    def out_of_cards(self):
        for suit in self.__suits:
            self.__deck[suit] = {}

            for number in self.__numbers:
                self.__deck[suit][number] = SHOE_SIZE

    def quit(self):
        self.__mainw.destroy()


def main():

    Userinterface()


if __name__ == "__main__":
    main()
