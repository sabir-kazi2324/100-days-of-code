# stone paper game

from stone_paper_data import rock, paper, scissors

# Write your code below this line 👇

import random

choices_1 = [rock, paper, scissors]
choice_2 = ["rock", "paper", "scissors"]

user = int(input("What do you choose? Type 0 for rock, 1 for paper, or for 2 scissors.\n"))

print("Your choice : ")
print(choice_2[user])
print(choices_1[user])
print("\n\n")

computer = random.randint(0, 2)
print("Computer choice : ")
print(choice_2[computer])
print(choices_1[computer])
print("\n\n")

if user < 3:
    if user == 0 and computer == 2:
        print("You Won!")
    elif computer == 0 and user == 2:
        print("you lose")
    elif user > computer:
        print("You Won!")
    elif user < computer:
        print("ou lose")
    else:
        print("its draw")
else:
    print("wrong choice by user you lose")
