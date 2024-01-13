# secret auction program

from art import logo

run = True
dict = {}


def get_winner(dict):
    winner = max(zip(dict.values(), dict.keys()))[1]
    print(f"The winner is {winner} with a bid of {dict[winner]}")


def add_bidders(user_name, user_bid):
    global dict
    dict[user_name] = user_bid


print(logo)

while run:
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid: $"))
    add_bidders(user_name, user_bid)
    prog_con = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if prog_con == "no":
        run = False
        get_winner(dict)
    else:
        # use this 'clear()' function here to clear your terminal before next bidding.
        pass
    