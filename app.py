# Import your Game class
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase
# Create your Dunder Main statement.

# Inside Dunder Main:
#  Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop


#
# print(phrase)
# print(game)


# Tests to make sure it's working

if __name__ == '__main__':
    game = Game()
    print(game.active_phrase)
    game.active_phrase.display(game.guesses)
    # def print_phrase(your_phrase):
    #     print(f'The phrase is: {your_phrase.phrase}')
