# Hangman - Project 
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

This project serves as a learning experience to better understand python. 

## Usage Instructions
The game is ready to be played by running the code. This piece of code is located on milestone_5.py

If the player would like to change the list of words to be guessed, simply change word_list. 

There are docstrings and explanations of the code throughout the code if you would like to better understand or modify the code. 

## Phases of project detailed in milestones 
This is a diary of the stages I had constructing this code.

### Milestone 1
- Simply setting up the Github repositories, downloading the project to the local computer. 

### Milestone 2
- word_list was defined as a list of my 5 favourite fruits
- We use the random module, which is going to help the programme randomise words using random.choice on the word.list
- This was tested 
- guess was assigned as the variable to have the input for the game 
- A piece of code that checks whether the input is a single character was implemented. Using if-else statements
- The README code was updated (not very much at that stage)
- The code was pushed to Github for the first time since being cloned. 
- Conclusion - the code has some features that can be used for Hangman, however, it is pretty disorderly at this stage 

### Milestone 3
- A piece of code was written doing While True loop checking whether the guess is a single alphabetical character. isalpha method was used to see whether it is alphabetical
- A piece of code if-else created to check whether the guess is in the letter. 
- Using the hangman template the code started to take some shape by assigning functions to the code already written. Curating ask_for_input and check_guess functions
- Additions such as lower casing to the guess and adding the check_guess function to the ask_for_input argument was done
- Most of the Milestone 1, 2, 3 README was done at this stage
- The code was pushed to Github.
- Conclusion this part was quite challenging as all the code was being put together into the class at this point.  Having to write all the attributes, checking indentations, adding new features whilst trying to not affect the current ones proved challenging, the code still feels pretty incomplete and is not working fully as whole.  

### Milestone 4
- The ask_for_input method was reshuffled so the invalid letter message was inside while true rather than else, also another if statement was added to add the 'You already tried that' print when a guess has already been tried
- Futhermore, in in ask_for_input the we append the guess when correct in the else statement
- In the check_guess we add the subtraction of num_lives and num_letters plus a message showing this. 
- The README file was updated
- The code was pushed to Github
- Conclusion: I have previously done a lot of the tasks for this milestone as I organised my code in earlier milestone to achieve this. However, a few tweaks had to be done, plus the added features mentioned before. 

### Milestone 5
- The play_game function was created using the Hangman class in a variable. 
- A while True loop was created to discern whether the player won, lost or needed to put in another input. 
- Conclusion: at this final stage the features of the play_game functions were not too dificult to set up, however, some tweaking with breaks and some placing throughout the code needed to be changed to achieve the final product. 
