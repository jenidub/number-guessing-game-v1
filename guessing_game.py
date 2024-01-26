"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random

# Create the start_game function.
# Write your code inside this function.
def start_game():
  #   When the program starts, we want to:
  #   ------------------------------------
  #   1. Create a local variable called 'guesses' and set it to 0.
  guesses = 0

  #   2. Display an intro/welcome message to the player.
  print("Welcome to the Number Guessing Game by JeniDub.")
  name = input("What is your name?   ")

  #   3. Store a random number as the answer/solution.
  solution = random.randrange(0, 100)

  #   4. Continuously prompt the player for a guess.
  #     a. If the guess is greater than the solution, display to the player "It's lower".
  #     b. If the guess is less than the solution, display to the player "It's higher".

  while True:
    current_guess = int(input("What is your guess {}?    ".format(name)))
    if current_guess > solution:
      print("Your guess is too high - Keep guessing!")
      guesses += 1
      continue
    elif current_guess < solution:
      print("Your guess is too low - Keep guessing!")
      guesses += 1
      continue
    elif current_guess == solution:
      print("\n***********************")
      print("You got it {}! Congratulations!".format(name))
      print("It only took you {} guesses to get it right!".format(guesses))
      break
    else:
      print("Invalid input. Please enter an integer value between 1 and 100.")
      continue

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates game over.
  print("\n***********************")
  print("It is game over for now.")
  print("I challenge you to do the following:")
  print("Restart the game to test your skills... if you dare")


# ( You can add more features/enhancements if you'd like to. )

# Kick off the program by calling the start_game function.
start_game()
