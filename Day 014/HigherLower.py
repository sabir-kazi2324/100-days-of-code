# HigherLower Game

from game_data import data
from art import logo, vs
import random


def check_winner(winner, guess):
    global play_game, points
    if winner == guess:
        points += 1
    else:
        print(f"Sorry, that's wrong. Final score: {points}")
        play_game = False


def compare():
    global a, b
    winner = ""
    if a["follower_count"] > b["follower_count"]:
        winner = "a"
    elif a["follower_count"] < b["follower_count"]:
        winner = "b"
    check_winner(winner, input("Who has more followers? Type 'A' or 'B': "))


def show_output(a, b):
    global logo, vs
    print(logo)
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
    print(vs)
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")
    compare()


def take_candidate():
    global data
    return random.choice(data)


points = 0
a = take_candidate()

play_game = True
while play_game:
    b = take_candidate()
    while a == b:
        b = take_candidate()
    show_output(a, b)
    a = b
