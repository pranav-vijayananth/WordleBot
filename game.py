##############################
# WORDLE MODULE
##############################

from words import words

class WorldGame: 
    def __init__(self, target_word):
        self.target_word = target_word
        self.black = "BLACK"
        self.yellow = "YELLOW"
        self.green = "GREEN"
        self.words = words
        self.output = [["" for j in range(2)] for i in range(5)]
    
    def is_valid_word(self, user_guess): 
        if user_guess in self.words:
            pass 
        else: 
            print(SyntaxError("Not a valid word"))
    
    
    def check_answer(self):
        for arr in self.output: 
            if arr[1] == self.green:
                return True

    def run(self):
        for guess in range(1, 5+1): 

            if self.check_answer(): 
                quit("You got the correct answer")
            else: 
                pass
    
            user_guess = input(f"Guess {guess}: ") 
            self.is_valid_word(user_guess)

            ##########
            # User-defined Data Structures 
            # 
            # list = [[letter, color], [letter, color]]
            # Each index of the list equals a letter of the word
            #
            #########


            for index in range(0, 5):
                self.output[index][0] = user_guess[index]


        
            ### changing output ###

            for index in range(0, 5):
                if user_guess[index] == self.target_word[index]:
                    self.output[index][1] = self.green
            
                elif (user_guess[index] != self.target_word[index] and user_guess[index] in self.target_word): 
                    self.output[index][1] = self.yellow
                
                else: 
                    self.output[index][1] = self.black
            
            print(self.output) 

if __name__ == "__main__": 
   
    test_game = WorldGame(target_word="cynic")
    print(test_game.run())
    

### GAME SIM ### 

# target_word = "cynic"
# ### example_word = "cnity"

# for guess in range(1, 5+1): 
    
#     user_guess = input(f"Guess {guess}: ")

#     if user_guess in words:
#         pass 
#     else: 
#         print(SyntaxError("Not a valid word"))
    
#     ##########
#     # User-defined Data Structures 
#     # 
#     # list = [[letter, color], [letter, color]]
#     # Each index of the list equals a letter of the word
#     #
#     #########

#     output = [["" for j in range(2)] for i in range(5)]

#     for index in range(0, 5):
#         output[index][0] = user_guess[index]

    
#     ### changing output ###

#     for index in range(0, 5):
#         if user_guess[index] == target_word[index]:
#             output[index][1] = "GREEN"
        
#         elif (user_guess[index] != target_word[index] and user_guess[index] in target_word): 
#             output[index][1] = "YELLOW"
        
#         else: 
#             output[index][1] = "BLACK"
        
#     print(output)