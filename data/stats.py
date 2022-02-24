with open('wordle.txt') as wordle:
    wordle_arr = wordle.read().split(",")
print(f"Length of official Wordle words: {len(wordle_arr)}")

with open('wordle_word_bank.txt') as wordle_word_bank:
    wordle_word_bank_arr = wordle_word_bank.read().split(",")
print(f"Length of official Wordle word bank: {len(wordle_word_bank_arr)}")

with open('test.txt') as test:
    test_arr = test.read().split("\n")
print(f"Length of test set: {len(test_arr)}")

