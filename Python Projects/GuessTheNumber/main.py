from random import randint

from art import logo

easy_turns, hard_turns = 10, 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1


def set_difficulty():
    level = input("Choose the difficulty: 'easy' or 'hard' : ")
    if level == 'easy':
        return easy_turns
    elif level == 'hard':
        return hard_turns
    else:
        print("check difficulty")


def game():
    print(logo)
    print("Welcome to the Guessing game!")
    print("I am thinking of a number between 1 to 100.")
    answer = randint(1, 100)
    print(f"pssst, the correct ans is {answer}")

    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts to guess the number")

        guess = int(input("Guess the number: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")


game()