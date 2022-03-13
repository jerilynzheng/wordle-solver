from collections import Counter

def minimax(guess, word):
  wordCount = Counter(word)
  guessCount = Counter(guess)
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
    guessCount[guess[i]] -= 1
  return info

print(minimax('alloy', 'banal'))