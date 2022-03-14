from minimax import *
from firstGuess import *

def play():
    with open('../data/wordle.txt') as wordleWordBank:
            wordBank = guessWords = wordleWordBank.read().split(",")

    for i in range(6):

        print("Enter your guess:")
        guess = input().lower()
        while(len(guess) != 5):
            guess = input().lower()

        print("Enter the results of your guess (ex. 'gygbb'):")
        info = input().lower()
        while(len(info) != 5):
            info = input().lower()

        newWordBank = solve(info, guess, wordBank)
        
        return playRound(newWordBank) 

print(play())