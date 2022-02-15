##############################
# GAME RLUES: 
# 1.) 

##############################

from doctest import OutputChecker
from words import words

class WorldGame: 
    def __init__(self, target_word):
        self.target_word = target_word
        self.black = ""
        self.yellow = ""
        self.green = ""
    
    def check_for_green(self):
        pass 

    def check_for_yellow(self):
        pass

    def check_for_black(self):
        pass 

    def main(self):
        pass

### GAME SIM ### 

target_word = "cynic"
### example_word = "cnity"

for guess in range(1, 5+1): 
    
    user_guess = input(f"Guess {guess}: ")

    if user_guess in words:
        pass 
    else: 
        print(SyntaxError("Not a valid word"))
    
    ##########
    # User-defined Data Structures 
    # 
    # list = [[letter, color], [letter, color]]
    # Each index of the list equals a letter of the word
    #
    #########

    output = [["" for j in range(2)] for i in range(5)]

    for index in range(0, 5):
        output[index][0] = user_guess[index]

    
    ### changing output ###

    for index in range(0, 5):
        if user_guess[index] == target_word[index]:
            output[index][1] = "GREEN"
        
        elif (user_guess[index] != target_word[index] and user_guess[index] in target_word): 
            output[index][1] = "YELLOW"
        
        else: 
            output[index][1] = "BLACK"
        
    print(output)