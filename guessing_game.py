# Python Development Techdegree: Project 1 - The Number Guessing Game
# Written by JeniDub
# I am aiming for the Exceed Expectations grade with this submission

# Import the random module.
import random

# Create the global variables for the solution upper limit and the current high score
SOLUTION_UPPER_LIMIT = 100

# Create a function to generate a random number between 1 and SOLUTION_UPPER_LIMIT
def generate_random_number():
  solution = random.randrange(1, SOLUTION_UPPER_LIMIT)
  return solution

# start_game Definition
def start_game():
  # Set up the tracking variables for while loop: game_over and CURRENT_HIGH_SCORE
  game_over = False
  current_high_score = 100

  # Set up the first game by defining the answer and guesses variables
  answer = generate_random_number()
  guesses = 0

  # Display an intro/welcome message with the player's name.
  print("Welcome to the Number Guessing Game by JeniDub!")

  # Get the player's name and save it in the local variable name
  name = input("What is your name?   ")

  # Display a message with the current_high_score
  print("The current high score for guesses is ", current_high_score)

  # Create a while loop to run the game until the player wants to exit the game
  while game_over is False:
    # If the player enters a non-integer or non-numeric value as a guess,
    # create a ValueError and prompt the user to guess again
    try:
      current_guess = input("What is your guess {}?    ".format(name))
      if current_guess.isnumeric() != True:
        raise ValueError(
            "Invalid input. Please enter an integer value between 1 and {}.".
            format(SOLUTION_UPPER_LIMIT))
      current_guess = int(current_guess)
      if current_guess <= 0 or current_guess > SOLUTION_UPPER_LIMIT:
        raise ValueError(
            "Your guess is out of range. Please enter an integer value between 1 and {}."
            .format(SOLUTION_UPPER_LIMIT))

    except ValueError as e:
      print(e)

    # If the player entered a valid guess, check to see if the guess is correct
    else:
      # If the guess is greater than the solution, display to the player "It's lower".
      # Increment the guesses variable
      guesses += 1

      if current_guess > answer:
        print("It's lower")
        # print("Your guess is too high - Keep guessing!")
        continue

      # If the guess is less than the solution, display to the player "It's higher".
      # Increment the guesses variable
      elif current_guess < answer:
        print("It's higher")
        # print("Your guess is too low - Keep guessing!")
        continue

      # If the guess is correct, display a congratulations message
      # that includes the number of guesses it took to get the right answer.
      # Once the guess is correct, stop looping, inform the user they "Got it"
      # and show how many attempts it took them to get the correct number.
      elif current_guess == answer:
        print("\n***********************")
        print("You got it {}! Congratulations!".format(name))
        print("It only took you {} guesses to get it right!".format(guesses))

      # Let the player know the game is ending, or something that indicates game over.
      print("\n***********************")
      print("It is game over for now.")
      while True:
        if guesses < current_high_score:
          current_high_score = guesses
        user_choice = input("Would you like to play again?  (Y/N)   ")
        if user_choice.lower() == "n":
          game_over = True
          break
        elif user_choice.lower() == "y":
          print("\n\nLet's play again!")
          print("The current high score for guesses is ", current_high_score)
          answer = generate_random_number()
          print("The new number is ", answer)
          guesses = 0
          break

  print("\n\n***********************")
  print("Thank you for playing the Number Guessing Game!")
  print("Your best score for guesses was", current_high_score)
  print("See you soon! Have a great day!")


# Kick off the program by calling the start_game function.
start_game()
