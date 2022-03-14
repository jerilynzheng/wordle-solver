from collections import Counter

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
    # print(greens, yellows, blacks)
    newWordBank = prune(greens, yellows, blacks, wordBank)
    print(f"{round(100*len(newWordBank)/len(wordBank),2)}% of words remain")
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
            return False
    return True

def blackCheck(blacks, word):
    for black in blacks:
        if black in word:
            return False
    return True

def yellowCheck(yellows, word):
    wordCount = Counter(word)
    for yellow in yellows.keys():
        if yellows[yellow] < wordCount[yellow] or yellow not in word:
            return False
    return True