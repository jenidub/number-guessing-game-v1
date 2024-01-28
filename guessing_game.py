# Python Development Techdegree: Project 1 - The Number Guessing Game
# Written by JeniDub

# Import the random module.
import random

# start_game Definition
def start_game():
  #   When the program starts, we want to:
  #   ------------------------------------
  #   1. Create a local variable called 'guesses' and set it to 0.
  guesses = 0

  #   2. Get the player's name and save it in the local variable name
  name = input("What is your name?   ")

  #   3. Display an intro/welcome message with the player's name.
  print("Welcome to the Number Guessing Game by JeniDub {}!".format(name))

  #   4. Store a random number as the answer/solution.
  solution = random.randrange(0, 100)

  #   Use a while loop to run the game until the player gets the number right
  while True:
    # If the player enters a non-integer or non-numeric value as a guess,
    # create a ValueError and prompt the user to guess again
    try:
      current_guess = input("What is your guess {}?    ".format(name))
      if current_guess.isnumeric() != True:
        raise ValueError("Invalid input. Please enter an integer value between 1 and 100.")
    except ValueError as e:
      print (e)
    
    # If the player entered a valid guess, check to see if the guess is correct
    else:
      # If the guess is greater than the solution, display to the player "It's lower".
      # Increment the guesses variable
      if current_guess > solution:
        print("It's lower")
        # print("Your guess is too high - Keep guessing!")
        guesses += 1
        continue
      
      # If the guess is less than the solution, display to the player "It's higher".
      # Increment the guesses variable
      elif current_guess < solution:
        print("It's higher")
        # print("Your guess is too low - Keep guessing!")
        guesses += 1
        continue
      
      # If the guess is correct, display a congratulations message
      # that includes the number of guesses it took to get the right answer.
      # Once the guess is correct, stop looping, inform the user they "Got it"
      # and show how many attempts it took them to get the correct number.
      elif current_guess == solution:
        print("\n***********************")
        print("You got it {}! Congratulations!".format(name))
        print("It only took you {} guesses to get it right!".format(guesses))
        break


  # Let the player know the game is ending, or something that indicates game over.
  print("\n***********************")
  print("It is game over for now.")
  print("I challenge you to restart the game and see if you can do better. 'Till next time...?")

# ( You can add more features/enhancements if you'd like to. )

# Kick off the program by calling the start_game function.
start_game()
