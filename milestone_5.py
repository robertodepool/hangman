import random


class Hangman: 
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
       self.word = random.choice(word_list) 
       self.word_guessed = ['_' for char in self.word] 
       self.num_letters = len(set(self.word))
       self.num_lives = num_lives
       self.word_list = word_list
       self.list_of_guesses = []
       
       print(f"The mistery word has {self.num_letters} characters")
       print(f"{self.word_guessed}") 

    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is, also reduces the num_letters by 1
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked

        '''
        guess = guess.lower() 
        word = self.word.lower()
        if guess in word: 
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
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method and appends the guess to the list_of_guesses
        '''
        while True:
            guess = input("Enter a single letter: ").lower()
            if guess.isalpha() and len(guess) != 1: 
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: 
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess) 
            break
    

def play_game(word_list): 
        '''
        The function that the player uses to play the game
        Variables:
        ----------
        num_lives:
            Number of lives you have, in this case 5
        game:
            Instance of the class Hangman, we use this to call this class throughout the function.
            Arguments: word_list and num_lives
        There are 3 coditions in the while True loop
        1. If num_lives 0 the player loses
        2. If the num_lives are greater than 0 and num_letters are equal to 0 the player wins
        3. If the num_letters are greater than 0 the loop keeps going (calls ask_for_input) until either of the two other conditions are satified 
        '''
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while True:
            print(f"\n{' '.join(game.word_guessed)}")  # Print the current state of the word
            if game.num_lives == 0:
                print("You lost!")
                break
            elif game.num_lives > 0 and game.num_letters == 0:
                print("Congratulations. You won the game!")
                break
            elif game.num_letters > 0:
                game.ask_for_input()


if __name__ == "__main__":
    word_list = ["apple", "papaya", "mango", "blueberry", "banana"]  # word_list created with my favourite fruits 
    play_game(word_list)  # Calls play_game to play the game