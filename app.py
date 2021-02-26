# Import your Game class
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase
# Create your Dunder Main statement.
def __main__():
    phrase = Phrase()
    game = Game()
    # for phrase in game.phrases:
    #     print(phrase.phrase)
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop


#
# print(phrase)
# print(game)


# Tests to make sure it's working

phrase = Phrase("dance")
print(phrase.phrase)
