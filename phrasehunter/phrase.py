# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        pass

    def display(self):
        # this prints out the phrase to the console with guessed letters visibile and unguessed letters as underscores. For
        # example, if the current phrase is "hello world" and the user has guessed the letter "o", the output should look like this:
        # _ _ _ _ o    _ o _ _
        pass

    def check_letter(self):
        # checks to see if the letter selected by the user matches a letter in the phrase.
        pass

    def check_complete(self):
        # checks to see if the whole phrase has been guessed.
        pass
