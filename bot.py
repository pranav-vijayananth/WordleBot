from audioop import avg
from turtle import pos, position
from words import words
from game import WorldGame
from wordfreq import word_frequency
import itertools
import math

"""
WorldeBot that simulates the WordleGame module using entropy, 
information theory, and day-to-day word frequencies. 

"""
class WordleBot(WorldGame): 
    def __init__(self, word):
        self.word_state = []
        self.word = word

    @staticmethod
    def information(p):
        return math.log(1/p, 2)

    def calculate_entropy(self):

        avg_entropy = 0
        all_states = []

        # using numbers for easier calculation
        # each number coresponds to a color code

        color_codes = ["GREEN", "YELLOW", "BLACK"]
        pattern_variations = [p for p in itertools.product(color_codes, repeat=5)]

        for var in pattern_variations:
            all_states.append([
                [self.word[0], var[0]], 
                [self.word[1], var[1]], 
                [self.word[2], var[2]], 
                [self.word[3], var[3]], 
                [self.word[4], var[4]]
            ])

        for state in all_states:
            self.word_state = state
            p = self.probability()
            info = self.information(p)
            avg_entropy += p * info
        
        return ((avg_entropy / 243) * 100)
        
        # return ((avg_entropy / (3**5)) * 100)

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
        
        return len(possibilities) / len(words)

    def simulate_game(self): 
        pass


bot = WordleBot("sient")
print(bot.calculate_entropy())