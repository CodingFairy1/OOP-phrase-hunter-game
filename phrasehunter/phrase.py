
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def __repr__(self):
        return f'{self.phrase}'

    def display(self, guesses):
        # this prints out the phrase to the console with guessed letters visibile and unguessed letters as underscores.
        for letter in self.phrase:
            if self.phrase.islower() == True:
                if letter in guesses:
                    print(f'{letter}', end=' ')
                else:
                    print ("_ ", end=" ")

    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False

    def check_letter(self):
        # checks to see if the letter selected by the user matches a letter in the phrase.
        pass

    def check_complete(self, guesses):
        # checks to see if the whole phrase has been guessed.
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
