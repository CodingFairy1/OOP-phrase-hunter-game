# Create your Game class logic in here.
from phrasehunter.phrase import Phrase
import random

class Game:
    def __init__(self):
        self.missed = 0
        # ^ used to track the number of incorrect guesses by the user. The initial value is 0 since no guesses have been made at the
        # start of the game.
        self.phrases = [Phrase('dance machine'), Phrase('home theatre'), Phrase('arcade games'), Phrase('pixel perfect'), Phrase('karaoke bar')]
        # ^ a list of five Phrase objects to use with the game. A phrase should only include letters and spaces -- no numbers,
        # puntuation or other special characters.
        self.active_phrase = self.get_random_phrase()
        # ^ This is the Phrase object that's currently in play. The initial value will be None. Within the start_game() method, this
        # property will be set to the Phrase object returned from a call to the get_random_phrase() method.
        self.guesses = [" "]
        # ^ This is a list that contains the letters guessed by the user

    def start(self):
        # Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, increments
        self.welcome()
        while self.missed < 5 or self.active_phrase.check_complete(self.guesses) == False:
            print(f"Number missed: {self.missed}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            self.active_phrase.check_guess(user_guess)
            elif not self.active_phrase.check_guess(user_guess):
                self.missed += 1
            self.active_phrase.check_complete(self.guesses)
            # Assigning the guesses?^
        pass

    def get_random_phrase(self):
        # this method randomly retrieves one of the phrases stored in the phrases list and returns it.
        your_phrase = random.choice(self.phrases)
        return your_phrase

    def welcome(self):
        # this method prints a friendly welcome message to the user at the start of the game
        print("""
                  0===========0============0
          (>^_^)>| Welcome to Phrase Hunter |<(^o^<)
         0____________________0_____________________0
        """)
        pass

    def get_guess(self):
        # this method gets the guess from a user and records it in the guesses attribute
        user_input = input("\n\nTry and guess a letter:  ")
        return user_input
        pass

    def game_over(self):
        # this method displays a friendly win or loss message and ends the game.
        pass
