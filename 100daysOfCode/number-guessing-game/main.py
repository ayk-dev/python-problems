from random import randint
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def choose_a_number():
  return randint(1, 101)


def set_attempts(diff):
  if diff.lower() == 'easy':
    return EASY_LEVEL_ATTEMPTS
  elif diff.lower() == 'hard':
    return HARD_LEVEL_ATTEMPTS
  else:
    print("Invalid answer. Try again.")


def play_game():

  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = choose_a_number()
  print(f"Pssst the correct answer is {answer}")
  
  print("Choose a difficulty. Type 'easy' or 'hard':", end=" ")
  difficulty = input()
  attempts = set_attempts(difficulty)
  
  game_won = False
  while not game_won and attempts > 0:
    print(f"You have {attempts} attempts to guess the number.")
    player = int(input("Make a guess: "))
    
    if player == answer:
      game_won = True
    else:
      attempts -= 1
      if player > answer:
        print("Too high")
      elif player < answer:
        print("Too low")
      if attempts == 0:
        continue
      print("Guess again.")
    
  if game_won:
    print(f"You got it! The answer was {answer}")
  else:
    print("You've run out of guesses. You lose.")

  play_again = input("Would you like to play again? type 'y' or 'n': ")
  if play_again == 'y':
    play_game()
  else:
    print("Thanks for playing!")


play_game()


