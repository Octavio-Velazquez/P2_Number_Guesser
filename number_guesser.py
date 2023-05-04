"""
In this game, we have to guess which is the number that the computer has chosen.
But first, you will have to choose which is the top number of the range.
"""

# First, we need to import the 'random' library
import random

# Welcome message. Mention the game's name and what the user have to do.
print("\nWelcome to the 'Number Guessing Game'.\nYou have to guess what number the computer choose between a range!")

# We ask the user which is the top number of the range.
top_of_range = input("\nType a top number for the range: ")

# In this conditional, we have to assure that the user enter a digit.
if top_of_range.isdigit():  # The function 'isdigit' check that the value is a digit.
    top_of_range = int(top_of_range)  # If the value is digit, them the variable will change its type as an integer.

    if top_of_range <= 0:  # If the value is equal or less than 0, it will show a message.
        print("Please, type a number larger than 0.")
        quit()   # And the game will close.
else:            # If the value is not a digit, it will show this another message.
    print("Please type a number next time.")
    quit()       # And the game will close.

# For the variable 'random_number' we pick the function 'random.randint()' which allow us to use a random integer number
# from the range of two numbers. The top of range number is chose by the user.
random_number = random.randint(0, top_of_range)
guesses = 0   # We also add a counter to know in how many tries we guess the number.

# We use the 'while' loop to ask the question and to increment the guesses counter value.
while True:
    guesses += 1   # We put the counter at the beginning because the first question it's the first try.
    user_guess = input("\nMake a guess: ")  # Ask the question for the user.
    if user_guess.isdigit():                # We also have to check that the value is also a digit.
        user_guess = int(user_guess)   # If the value is a digit, the user guess number type will change as an integer.
    else:                              # If the value is not a digit, it will show this message.
        print("\nPlease, type a number next time.")
        continue                       # This 'continue' let the loop ask again the question.

    if user_guess == random_number:  # If the user guess and the random number is the same, you won!
        print("\nExcellent! You guess the number!")
        break                        # And the game is finish!
    elif user_guess > random_number:  # This appear if the random number is above of the number that you chose.
        print("You were above the number!")
    else:                             # This appear if the random number is below of the number that you chose.
        print("You were below the number!")

# This message shows in how many tries you got the guess.
print(f"\nYou got it in {guesses} guesses!")






