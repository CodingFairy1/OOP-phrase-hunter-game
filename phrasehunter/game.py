# Create your Game class logic in here.
from phrasehunter.phrase import Phrase
import random

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('dance machine'), Phrase('home theatre'), Phrase('arcade games'), Phrase('pixel perfect'), Phrase('karaoke bar')]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
        # ^ This is a list that contains the letters guessed by the user

    def start(self):
        # Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, increments
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"Number missed: {self.missed}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            self.active_phrase.check_guess(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
            self.active_phrase.check_complete(self.guesses)
        self.game_over()

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

    def get_guess(self):
        # this method gets the guess from a user and records it in the guesses attribute
        user_input = input("\n\nTry and guess a letter:  ")
        return user_input

    def game_over(self):
        # this method displays a friendly win or loss message and ends the game.
        if self.missed == 5:
            print("Sorry, you're out of guesses. Better luck next time!")
        else:
            print("Congratulations! You win!")
