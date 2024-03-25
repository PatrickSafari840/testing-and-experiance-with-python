import random

def play_game():
  """
  This function plays a guessing game with the user.
  """
  # Generate a random number between 1 and 100
  secret_number = random.randint(1, 100)

  # Set the number of attempts to 7
  attempts_remaining = 7

  # Loop while the user has attempts remaining and has not guessed the number
  while attempts_remaining > 0 and not guess == secret_number:
    # Prompt the user to guess the number
    print(f"You have {attempts_remaining} attempts remaining.")
    guess = input("Guess the secret number: ")

    # Check if the guess is valid
    if not guess.isdigit():
      print("Invalid input! Please enter a number.")
      continue

    # Convert the guess to an integer
    guess = int(guess)

    # Check if the guess is too high or too low
    if guess > secret_number:
      print("Your guess is too high.")
    elif guess < secret_number:
      print("Your guess is too low.")

    # Decrement the number of attempts remaining
    attempts_remaining -= 1

  # Display the result of the game
  if guess == secret_number:
    print(f"Congratulations! You guessed the secret number in {7 - attempts_remaining} attempts.")
  else:
    print(f"You failed to guess the secret number. The number was {secret_number}.")

# Play the game repeatedly until the user quits
while True:
  play_game()

  # Prompt the user to continue playing
  continue_playing = input("Would you like to continue playing (y/n): ")

  # Break out of the loop if the user enters 'n'
  if continue_playing.lower() != "y":
    break

print("Goodbye!")
print("-" * 100)
