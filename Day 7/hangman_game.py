from hangman_art import stages, logo
from hangman_words import word_list
import random

total_life = 6
run = True
letter_list = []
print(logo)
word = random.choice(word_list)
print(f"Chosen word is {word}")
for i in range(len(word)):
    letter_list.append("_")


def check_life(life):
    global total_life, user_choice, letter_list, run
    total_life -= life
    if life == 1:
        print(f"You guessed {user_choice}, that's not in word. You lose a life")
    print(letter_list)
    print(stages[total_life])
    if total_life == 0:
        run = False
        print("You have lost")
    if '_' not in letter_list:
        run = False
        print("You won")


def list_update(user_choice):
    no = -1
    life = 1
    global letter_list
    for i in word:
        no += 1
        if user_choice == i:
            letter_list[no] = user_choice
            life = 0
    check_life(life)


while run:
    user_choice = input("Guess a letter : ")
    list_update(user_choice)
