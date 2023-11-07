import random

class hangman: 
    def __init__(self, word_list, num_lives=5):
       self.word = randon.choice(word_list)


word_list = ["apple", "papaya", "mango", "blueberry", "banana"]
print(word_list)
word = random.choice(word_list)
print(word)
guess = input("Enter a single letter: ")

if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
