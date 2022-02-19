from words import words
from wordfreq import word_frequency
import math

class WordleBot(): 
    def __init__(self, arr):
        self.arr = arr
    
    def entropy(self):
        pass

    def information(self):
        pass 

    @staticmethod
    def into_bits(pos):
        return math.log((1/pos),2)    
    
    @staticmethod
    def filter(lexicon):

        # pre-defined variables/constants        
        possibilities = words
        bits = 1
        index = 0

        while index != 5: 
            if lexicon[index][1] == "GREEN":

                target_letter = lexicon[index][0]

                possibilities = list(filter(
                    lambda word: word[index] == target_letter, 
                    possibilities
                ))

            if lexicon[index][1] == "YELLOW":

                target_letter = lexicon[index][0]

                possibilities = list(filter(
                    lambda word: target_letter in word, 
                    possibilities
                ))
            
            if lexicon[index][1] == "GRAY":
                pass 

            else:
                SyntaxError("Something went wrong here")

            index += 1 
        
        return len(possibilities) / len(words)

    def run(self): 
        pass


# print(WordleBot.filter([["w", "GREEN"], [None, None], [None, None], ["r", "YELLOW"], ["y", "GREEN"]]))
print(WordleBot.into_bits(0.0005))