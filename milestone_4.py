import random

class Hangman: 
    def __init__(self, word_list, num_lives=5):
       self.word = random.choice(word_list)
       self.word_guessed = ['_' for _ in self.word]
       self.num_letters = len(set(self.word)) #using set to only get the unique letters 
       self.num_lives = num_lives
       self.word_list = word_list
       self.list_of_guesses = []
       
       print(f"The mistery word has {self.num_letters} characters")
       print(f"{self.word_guessed}")

    def check_guess(self, guess):
        guess = guess.lower()
        word = self.word.lower()
        if guess in word: #Check whether the letter is in the word
            for index, letter in enumerate(word):
                if letter == guess:
                    self.word_guessed[index] = guess
            print(f"Good guess! {guess} is in the word.")
            self.num_letters -= 1
        else: 
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} left")

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ").lower()
            if guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_list = ["apple", "papaya", "mango", "blueberry", "banana"]
word = random.choice(word_list)

handman_game = Hangman(word_list)
handman_game.ask_for_input()

