"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random

# Global Variable Definitions
name = input(
    "Welcome to the Number Guessing Game by JeniDub. What is your name?   ")
solution = random.randrange(0, 100)


# Create the start_game function.
# Write your code inside this function.
def start_game():
  #   When the program starts, we want to:
  #   ------------------------------------
  #   1. Display an intro/welcome message to the player.
  #   2. Store a random number as the answer/solution.
  #   3. Continuously prompt the player for a guess.
  #     a. If the guess is greater than the solution, display to the player "It's lower".
  #     b. If the guess is less than the solution, display to the player "It's higher".
  guesses = 0

  while True:
    current_guess = int(input("What is your guess {}?    ".format(name)))
    if current_guess != solution:
      print("Keep guessing!")
      guesses += 1
      continue
    else:
      break

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.
  print("\n***********************")
  print("You got it {}! Congratulations!".format(name))
  print("It only took you {} guesses to get it right!".format(guesses))
  print("\n***********************")
  print("It is game over for now.")
  print("I challenge you to do the following:")
  print("Restart the game to test your skills... if you dare")


# ( You can add more features/enhancements if you'd like to. )

# Kick off the program by calling the start_game function.
start_game()
