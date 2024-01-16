# Guess The Number

from art import logo
import random

chosen_number = random.randrange(1, 100)
attempt = 0
print(logo)
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")
# USe blow print line to make it easy
# print(f"chosen number: {chosen_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5

play_game = True

while play_game:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}")
        break
    elif guess > chosen_number:
        print("To high.")
    elif guess < chosen_number:
        print("To low.")
    attempt -= 1
    if attempt == 0:
        print("You lost all attempt! You lose")
        play_game = False
    else:
        print("Guess again.")
