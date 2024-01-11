

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if choice_road == "left":
    choice_lake = input("You come to lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swin across.\n")
    if choice_lake == "wait":
        choice_house = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if choice_house == "yellow":
            print("You Win!")
        elif choice_house == "red":
            print("Burned by fire.")
        else:
            print("Eaten by beasts.")
    else:
        print("attacked by trout.")
else:
    print("Fall into a hole.")
print("Game is over.")
