import random

from art import logo, vs
from game_data import data
from turtle import clear


def get_random_number():
  return random.choice(data)


def format_data(account):
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name}, a {description} from {country}."


def followers(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'


def game():
  score = 0
  print(logo)
  is_game_over = False
  A = get_random_number()
  B = get_random_number()
  while not is_game_over:
    A = B
    B = get_random_number()

    while A == B:
      B = get_random_number()

    print(f"Compare A: {format_data(A)}")
    print(vs)
    print(f"Against B: {format_data(B)}")
    guess = input("who has more followers? 'A' or 'B':").lower()
    a_follower_count = A['follower_count']
    b_follower_count = B['follower_count']
    is_correct = followers(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"you got it. Current score = {score}")
    else:
      is_game_over = True
      print(f"you're wrong, your score is {score}")


game()
