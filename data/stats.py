with open('wordle.txt') as wordle:
    wordle_arr = wordle.read().split(",")
print(f"{len(wordle_arr)} Wordle words")

with open('wordle_word_bank.txt') as wordle_word_bank:
    wordle_word_bank_arr = wordle_word_bank.read().split(",")
print(f"{len(wordle_word_bank_arr)} words in official Wordle word bank")

with open('test.txt') as test:
    test_arr = test.read().split("\n")
print(f"{len(test_arr)} words in test set")

similarity = 0
for word in wordle_arr:
    if word in test_arr:
        similarity += 1
similarity = (similarity/len(wordle_arr) + similarity/len(test_arr)) / 2
print(f"{round(100*similarity, 3)}% similarity between the official Wordle words and the test set")

badWords = []
for badWord in test_arr:
    if badWord not in wordle_word_bank_arr:
        badWords.append(badWord)

print(f"{len(badWords)} words are not in the official Wordle word bank: {badWords}")