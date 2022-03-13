from collections import Counter

def guess(guess, word):
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

def prune(word, wordBank):
  newWordBank = []
  for word in wordBank:
    if guess(guessWord, targetWord) != ['gray'] * 5:
      newWordBank.append(word)
  return newWordBank

def playRound(wordBank):
  minWordBankLength = len(wordBank)
  for guessWord in wordBank:
    wordBankLength = len(prune(guessWord, wordBank))
    if wordBankLength < minWordBankLength:
      minWordBankLength = wordBankLength
      bestWord = guessWord
  return guessWord

with open('../data/wordle_word_bank.txt') as wordle_word_bank:
    wordle_word_bank_arr = wordle_word_bank.read().split(",")

print(playRound(wordle_word_bank_arr)[:50])