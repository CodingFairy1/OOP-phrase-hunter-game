
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        pass

    def __repr__(self):
        return f'{self.phrase}'

    def display(self, guesses):
        # this prints out the phrase to the console with guessed letters visibile and unguessed letters as underscores. For
        # example, if the current phrase is "hello world" and the user has guessed the letter "o", the output should look like this:
        # _ _ _ _ o    _ o _ _
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
        """
        loop through 'phrase' attribute. If any letter is not present in 'guesses', return 'False'. If it makes it through
        the entire loop without returning 'False', return True

        if all letters have been guessed:
                return True
            elif:
                return False
        """
        pass
