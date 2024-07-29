"""
This class handles the word the user needs to guess.
It checks whether the letter has been guessed before, updates the current guess status,
checks if the user guessed correctly, and appends guessed letters to a list.

By Jae Kim
"""

class Word:
    
    def __init__(self, word_string):
        self.guessed_letters = []
        self.word_string = word_string
        underscore = "_ " * len(word_string)
        self.current_guess = underscore[:-1]
        
    def already_guessed(self, letter):
        if letter in self.guessed_letters:
            return True
        return False
    
    def update_current_status(self, letter):
        temp = self.current_guess.split(' ')
        for i in range(len(self.word_string)):
            if self.word_string[i] == letter:
                temp[i] = letter
        self.current_guess = " ".join([x for x in temp])
        
    def guess(self, letter):
        self.guessed_letters.append(letter)
        if letter in self.word_string:
            return True
        return False
        
    def guessed_correctly(self):
        if "_" not in self.current_guess:
            return True
        return False
