"""
This class creates file objects that allow words to be read from a text file. The words in the file are used by the game.
It reads the contents of the file passed as an argument and adds words with lengths within a specified range to a list called "valid_words".
The list of valid words can then be returned and used by the game.

By Jae Kim
"""
class DictionaryReader:
    def __init__(self, file_name, min_word_length, max_word_length):
        if int(min_word_length) < 5:
            min_word_length = 5
            print("The minimum word length should be 5 or more characters!")
            print("It has been set to 5.")
        if int(max_word_length) < int(min_word_length):
            max_word_length = 5
            print("The maximum word length should be greater than or equal to the minimum word length!")
            print("The maximum word length has been set to 6")
        self.file_name = file_name
        self.min_word_length = int(min_word_length)
        self.max_word_length = int(max_word_length)

    def get_file_object(self):
        while True:
            try:
                input_file = open(self.file_name, 'r')
                return input_file
            except FileNotFoundError:
                print(f"{self.file_name} cannot be found.")
                prompt = input("Please enter a valid file name or Q to quit: ")
                if prompt == "Q":
                    return None
                self.file_name = prompt
                continue 

    def get_valid_words(self, words_file):
        content = words_file.read().split()
        word_list = []
        for word in content:
            if len(word) in range(self.min_word_length, self.max_word_length+1):
                word_list.append(word)
        words_file.close()
        return word_list
                
                
