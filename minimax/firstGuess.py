from collections import Counter

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
  bestWord = ""
  for guessWord in wordBank:
    wordBank = pruneRemainingWords(guessWord, wordBank)
    if len(wordBank) < minWordBankLength:
      minWordBankLength = len(wordBank)
      bestWord = guessWord
  return bestWord