from words import words
from wordfreq import word_frequency
import itertools
import math

"""
WorldeBot that simulates the WordleGame module using entropy, 
information theory, and day-to-day word frequencies. 

"""
class WordleBot(): 
    def __init__(self, word_state):
        self.word_state = word_state
    
    def calculate_entropy(self):

        # using numbers for easier calculation
        # each number coresponds to a color code

        color_codes = [1, 2, 3]
        pattern_variations = [p for p in itertools.product(color_codes, repeat=5)]
        
        return pattern_variations
    
    # works in all cases 
    def probability(self):

        # pre-defined variables/constants        
        possibilities = words
        bits = 1
        index = 0

        while index != 5: 
            if self.word_state[index][1] == "GREEN":

                target_letter = self.word_state[index][0]

                possibilities = list(filter(
                    lambda word: word[index] == target_letter, 
                    possibilities
                ))

            if self.word_state[index][1] == "YELLOW":

                target_letter = self.word_state[index][0]

                possibilities = list(filter(
                    lambda word: target_letter in word, 
                    possibilities
                ))
            
            if self.word_state[index][1] == "GRAY":
                pass 

            else:
                SyntaxError("Something went wrong here")

            index += 1 
        
        return possibilities

    def run(self): 
        pass


bot = WordleBot([["w", "GREEN"], ["o", "GREEN"], ["o", "GREEN"], ["t", "GREEN"], ["z", "GREEN"]])
print(bot.probability())