"""
This is the main function file to run the 'Hangman Game'. The main function calls two helper functions: get_word() and run_game().
The objective of the 'Hangman' game is for a player to guess a word by guessing the letters it contains. Each incorrect guess results in part of the gallows being drawn.
The game is over when the gallows are fully printed out (player loses) or the player successfully guesses all the letters in the word within the 7 phases.

By Jae Kim
"""

from Dictionary_Reader import DictionaryReader
from Word import Word
from Drawing import Drawing
import random
random.seed(30)

def get_word(dict_reader, dict_file):
    list_words = dict_reader.get_valid_words(dict_file)
    if list_words == []:
        print("No valid words available. The game will end.")
        return None
    else:
        list_capacity = len(list_words)
        random_word_index = random.randint(0, len(list_words)-1)
        return Word(list_words[random_word_index])

def run_game(word):
    gallow = Drawing()
    print("Word:", word.current_guess)
    while not gallow.game_over():
        print()
        prompt = input("Please guess a letter: ")
        while word.already_guessed(prompt):
            prompt = input(f"You have already used {prompt} as a guess.\n Guess another letter:")
            print()
        if word.guess(prompt):
            print(f"The word contains the letter: {prompt}")
            print()
            word.update_current_status(prompt)
        else:    
            print(f"The word does not contain the letter: {prompt}")
            print()
            gallow.increment_phase()
        print("Word:", word.current_guess)
        print()
        print("Guessed letters:")
        print(" " + str(word.guessed_letters))
        print()
        print("Gallows:")
        print()
        gallow.draw()
        gallow.gallow_index += 1
        if word.guessed_correctly():
            print()
            print("Congratulations! You have won!")
            return
    print("You have lost!")
    return

def main():
    game_banner = "Hangman Game"
    banner_border = "=" * len(game_banner)
    print(game_banner)
    print(banner_border)
    print()
    dict_reader = DictionaryReader('Words2.txt', 5, 5)
    dict_file = dict_reader.get_file_object()
    if dict_file != None:
        word_random_selected = get_word(dict_reader, dict_file)
        if word_random_selected != None:
            word_random_selected.current_guess
            run_game(word_random_selected)
            
main()
