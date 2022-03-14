from collections import Counter

with open('../data/wordle.txt') as wordleWordBank:
    wordBank = guessWords = wordleWordBank.read().split(",")

def simulatedGuess(guess, word):
  guess = guess.lower()
  word = word.lower()
  wordCount = Counter(word)
  info = []
  for i in range(len(guess)):
    if guess[i] == word[i]:
      info.append('green')
      wordCount[guess[i]] -= 1
    elif guess[i] in word and wordCount[guess[i]] > 0:
      info.append('yellow')
      wordCount[guess[i]] -= 1
    else:
      info.append('gray')
  return info

def pruneRemainingWords(guess, wordBank):
  newWordBank = []
  for word in wordBank:
    if simulatedGuess(guess, word) == ['gray'] * 5:
      newWordBank.append(word)
  return newWordBank

def playRound(wordBank):
  minWordBankLength = len(wordBank)
  newWordBank = []
  bestWord = ""
  for guessWord in guessWords:
    tempWordBank = pruneRemainingWords(guessWord, wordBank)
    if len(tempWordBank) < minWordBankLength:
      minWordBankLength = len(tempWordBank)
      print(f"Possible remaining words: {minWordBankLength}")
      newWordBank = tempWordBank
      bestWord = guessWord
  print(f"Best word: {bestWord}")
  print(f"Eliminated {round(100 - 100*len(newWordBank)/len(wordBank),2)}% of words")
  
playRound(wordBank)