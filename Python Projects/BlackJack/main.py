# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.

import random
from turtle import clear

from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """returns sum of score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "you went over, you lose"

    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "you lose, computer wins"
    elif user_score == 0:
        return "you win"
    elif user_score > 21:
        return "you lose"
    elif computer_score > 21:
        return "you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"


def play_game():
    global computer_score, user_score
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9
    # need to be repeated until the game ends.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards : {user_cards} and your score : {user_score}")
        print(f"computer's first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_wish = input("Do you want to draw another card? 'y' or 'n'")
            if user_wish == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your final hand : {user_cards} and you final score: {user_score}")
    print(
        f"  Computer final hand : {computer_cards} , final score: {computer_score} "
    )
    print(compare(user_score, computer_score))


while input("do you want to start the game ? 'y' or 'n'") == 'y':
    clear()
    play_game()

# Hint 12: Once the user is done, it's time to let the computer play.
# The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0),
# then the user loses. If the user has a blackjack (0), then the user wins.
# If the user_score is over 21, then the user loses. If the computer_score is over 21,
# then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game.
# If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
