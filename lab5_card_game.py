"""
# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 17-10-2019
# purpose: Lab 5 - GUI and card game using queue
"""

from tkinter import *
# to use the queue FIFO
from queue import Queue

# to use the shuffle for shuffling the cards
from random import shuffle

class CardGame(Frame):
    """
    Card game
    """
    # Deck list used to make a shuffle deck
    deck_list = []
    # Deck dictionary used to get sore
    deck_values = {}
    # Deck itself
    deck = Queue(maxsize=52)
    player_score = 0
    game_running = True


    # initialises the application
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # set up game logic here:
        self.create_deck()
        # shuffle the cards before first use
        self.load_deck()

        self.init_window()
    #END __init__()

    def create_deck(self):
        """Create the deck
        1. Create an array of the card names
        2. Create a dictionary with card names and file path
        """

        card_suits = ('clubs', 'diamonds', 'hearts', 'spades')
        card_types_non_numeric = ['jack', 'queen', 'king']

        card_types_numeric = list(range(1, 11))

        # Convert card_values items to strings
        for i, card_type in enumerate(card_types_numeric):
            card_types_numeric[i] = str(card_type)
        #END FOR

        # Merge card types
        card_types = card_types_numeric + card_types_non_numeric

        # Create list of all cards
        for suits in card_suits:
            for card_type in card_types:
                card = card_type + '_' + suits

                self.deck_list.append(card)
            #END INNER FOR
        #END FOR

        # Create a deck dictionary
        for card in self.deck_list:
            if ('jack' in card) or ('queen' in card) or ('king' in card):
                self.deck_values[card] = 10
            else:
                for number in card_types_numeric:
                    if number in card:
                        self.deck_values[card] = int(number)
                    #END IF
                #END INNER FOR
            #END IF
        #END FOR
    #END create_deck()

    def load_deck(self):
        """ load shuffled deck """

        shuffle(self.deck_list)

        self.deck.queue.clear()

        for card in self.deck_list:
            self.deck.put(card)
        #END FOR
    #END load_deck()

    def pick_card(self):
        """ Pick up a new card and display it """
        if self.game_running:
            card = self.deck.get()

            self.update_score(card)

            self.score_label.config(text="Your score: " + str(self.player_score))
            self.score_label.update_idletasks()

            card_img = PhotoImage(file='cards/' + card + '.gif')
            self.open_card.config(image=card_img)
            self.open_card.photo = card_img
            self.open_card.update_idletasks()

            self.check_scores()
    #END pick_card()

    def update_score(self, card):
        """ Updates the score with the current card value"""
        self.player_score += int(self.deck_values[card])
    #END update_score()

    def done_playing(self):
        """ Done playing """
        self.game_running = False
        self.check_scores()
    #END done_playing()

    def check_scores(self):
        """ Check scores """
        if self.player_score == 21:
            self.score_label.config(text="Your score: 21. You hit the jack pot!")
            self.game_running = False
        elif self.player_score < 21 and not self.game_running:
            self.score_label.config(
                text="Your score " + str(self.player_score)+ " Well done! Play again?")
        elif self.player_score > 21:
            self.score_label.config(
                text="Your score " + str(self.player_score) + " Bad luck, GAME OVER!")
            self.game_running = False
        #END IF

        self.score_label.update_idletasks()
    #END check_scores()

    def new_game(self):
        """ Starts new game """
        self.player_score = 0
        self.game_running = True
        self.load_deck()
        self.pick_card()
    #END new_game()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        """Create the game window"""
        self.pack(expand=True)

        card = self.deck.get()
        print(card)
        self.update_score(card)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(self)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(self)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(self)
        score_frame.grid(row=1, column=0, columnspan=2)

        # add elements into the frames
        self.open_card = Button(cards_frame)
        card_img = PhotoImage(file='cards/'+card+'.gif')
        self.open_card.config(image=card_img)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = card_img

        closed_deck = Button(cards_frame, command=self.pick_card)
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        closed_deck.config(image=closed_card)
        closed_deck.grid(row=0, column=1, padx=2, pady=2)
        closed_deck.photo = closed_card

        done_button = Button(button_frame, text="I'm done!", command=self.done_playing)
        done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.new_game)
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        self.score_label = Label(score_frame, text="Your score: "+ str(self.player_score),
                                 justify=LEFT)
        self.score_label.pack()


    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        """Exits the game"""
        exit()


# object creation here:
root = Tk()
root.geometry("300x200")
root.title("Card Game")
app = CardGame(root)
root.mainloop()
