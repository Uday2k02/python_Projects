rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random

game_images = [rock, paper, scissors]
user = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors."))
print(game_images[user])

computer = random.randint(0, 2)
print(f"Computer chose:\n{game_images[computer]}")

if user > 2 or user < 0:
    print('invalid, you lose')
if user == 0 and computer == 2:
    print("you win")
elif user == 0 and computer == 1:
    print("you lose")
elif user == 1 and computer == 0:
    print("you win")
elif user == 1 and computer == 2:
    print("you win")
elif user == 2 and computer == 0:
    print("you lose")
elif user == 2 and computer == 1:
    print("you win")
elif user == computer:
    print("It's a draw")
