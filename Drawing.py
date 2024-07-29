"""
This Drawing class handles printing the gallows for the 'Hangman Game' by incrementing phases,
printing out the gallows from the list, and checking if the game is at the final phase of the game.

By Jae Kim
"""

class Drawing:

    def __init__(self):
        self.current_phase = 0
        self.max_phase = 7
        self.gallow_index = 0
        self.each_gallow_phase = ["", # 0 phase
                                  "------", # 1st phase
                                  "|     \n|     \n|     \n|     \n------", # 2nd phase
                                  "-----\n|     \n|     \n|     \n|     \n------", # 3rd phase
                                  "-----\n|   |\n|     \n|     \n|     \n------", # 4th phase
                                  "-----\n|   |\n|   O\n|     \n|     \n------", # 5th phase
                                  "-----\n|   |\n|   O\n|  ---\n|     \n------", # 6th phase
                                  "-----\n|   |\n|   O\n|  ---\n|  / \\\n------"] # 7th phase

    def increment_phase(self):
        if self.current_phase in range(0, self.max_phase+1):
            self.current_phase += 1
    
    def draw(self):
        print(self.each_gallow_phase[self.current_phase])
        
    def game_over(self):
        if self.gallow_index == self.max_phase:
            return True
        return False
