from random import randint
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

turns = 0
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("too high")
    return turns - 1
  elif guess < answer:
    print("too low")
    return turns - 1
  else:
    print(f"you got it ! the answer was {answer}")

def set_dificulty():
  level = input("choose a dificulty 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURN
  else:
    return HARD_LEVEL_TURN

def game():
  print(logo)
  print("Welcome to the guessing game")
  print("I'm thinking of a number between 1 to 100")
  answer = randint(1, 100)
  print(f"the actual answer is {answer}")
  turns = set_dificulty()
 
  guess = 0
  while guess != answer:
    
    print(f"you have {turns} attempts remaining to guess the number")
    guess = int(input("make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses you lose")
      return
    elif guess != answer:
      print("guess again")
game()
