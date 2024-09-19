import random


EASYLEVELTURNS = 10
HARDLEVELTURNS = 5

turns = 0
def check(guess, answer, turns):
  """Checks answer against guess, returns number of remaining turns"""
  if guess > answer:
    print("Too High.")
    return turns - 1 
  elif guess < answer:
    print("Too Low.")
    return turns - 1 
  else:
    print(f"You Got it! The answer was {answer}")


def setlevel():  
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "hard":
    return HARDLEVELTURNS
  elif level == "easy":
    return EASYLEVELTURNS

def game():
  print("Welcome to the Number Guessing Game \n I'm thinking of a number between 1 and 100.")
  answer = random.randint(1,100)
  
  turns = setlevel()
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check(guess, answer, turns)
    if turns == 0:
      print("You have run out of guesses, you lose.")
      return


game()