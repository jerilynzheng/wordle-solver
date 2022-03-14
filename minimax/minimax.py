from collections import Counter


# Suggests which word to guess

def guessVStarget(guess, targetWord):
  guess = guess.lower()
  targetWord = targetWord.lower()
  wordCount = Counter(guess)
  info = []
  for i in range(len(guess)):
    if guess[i] == targetWord[i]:
      info.append('green')
      wordCount[guess[i]] -= 1
    elif guess[i] in targetWord and wordCount[guess[i]] > 0:
      info.append('yellow')
      wordCount[guess[i]] -= 1
    else:
      info.append('gray')
  return info

def iterateGuesses(targetWord, wordBank):
  newWordBank = []
  for guess in wordBank:
    if guessVStarget(guess, targetWord) == ['gray'] * 5:
        newWordBank.append(guess)
  return newWordBank

def iterateTargets(wordBank):
  minWordBankLength = len(wordBank)
  bestWord = ""
  for targetWord in wordBank:
    tempWordBank = iterateGuesses(targetWord, wordBank)
    if len(tempWordBank) < minWordBankLength:
      minWordBankLength = len(tempWordBank)
      bestWord = targetWord
  return bestWord


# Prunes the word bank based on the results of the guess

def solve(info, guess, wordBank):
    greens = ['_']*5
    yellows = {}
    blacks = set()
    for i in range(len(guess)):
        if info[i] == 'g':
            greens[i] = guess[i]
        elif info[i] == 'y':
            if info[i] not in yellows:
                yellows[guess[i]] = 1
            else:
                yellows[guess[i]] += 1
        elif info[i] == 'b':
            blacks.add(guess[i])
    newWordBank = prune(greens, yellows, blacks, wordBank)
    print(f"{len(newWordBank)} words remain")
    return newWordBank

def prune(greens, yellows, blacks, wordBank):
    newWordBank = []
    for word in wordBank:
        if greenCheck(greens, word):
            if blackCheck(blacks, word):
                if yellowCheck(yellows, word):
                    newWordBank.append(word)
    return newWordBank
        
def greenCheck(greens, word):
    for i in range(len(greens)):
        if greens[i] != '_' and greens[i] != word[i]:
            # print(f"{word} has green letters in the wrong spot")
            return False
    return True

def blackCheck(blacks, word):
    for black in blacks:
        if black in word:
            # print(f"{word} contains {black}")
            return False
    return True

def yellowCheck(yellows, word):
    wordCount = Counter(word)
    for yellow in yellows.keys():
        if yellow not in word:
            # print(f"{word} doesn't have yellow letters")
            return False
    return True

# User guesses the word

def userGuess(fileLocation, roundNum):
    with open(fileLocation) as wordleWordBank:
        wordBank = wordleWordBank.read().split(",")

    print("Enter your guess:")
    guess = input().lower()
    if guess == '':
        return None
    while(len(guess) != 5):
        guess = input().lower()

    print("Enter the results of your guess (ex. 'gygbb'):")
    info = input().lower()
    while(len(info) != 5):
        info = input().lower()

    newWordBank = solve(info, guess, wordBank)
    newFileLocation = f"wordBank{roundNum}.txt"
    f = open(newFileLocation, "w")
    s = ","
    s = s.join(newWordBank)
    f.write(s)
    f.close()
    return newWordBank

def analyzeWordBank():
    with open("wordle_word_bank.txt") as wordleWordBank:
        startingWordBank = wordleWordBank.read().split(",")
    print(f"Analyzing word bank to determine the best starting word...")
    suggestedWord = iterateTargets(startingWordBank)
    print(f"Suggested guess: {suggestedWord}")
    return suggestedWord

def playGame():
    print("Welcome to Wordle solver!")
    print("Would you like me to suggest a starting word?")
    print("This may take a while. (y/n)")
    starter = input().lower()
    if starter == 'y':
        analyzeWordBank()
    for i in range(6):
        wordBank = userGuess(f'wordBank{i}.txt', i+1)
        if wordBank == None:
            print(f"Wordle solved in {i} guesses. NOICE.")
            return
        print(f"Suggested guess: {iterateTargets(wordBank)}")
    print("I suck at this game")
    return

playGame()