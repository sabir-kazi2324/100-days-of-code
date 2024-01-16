# Calculate with result
from art import logo


def ask_user(result):
    global run
    user_con = input(f"Type 'y' to continue calculating with {result}, or type 'no' to start new calculation: ")
    if user_con == "n":
        run = False


def calculate(a, b, operator):
    global fist_number
    result = 0
    if operator == "+":
        result = a+b
    if operator == "-":
        result = a-b
    if operator == "*":
        result = a*b
    if operator == "/":
        result = a/b
    fist_number = result
    print(f"{a} {operator} {b} = {result}")
    ask_user(result)


def second_number(a):
    operator_list = ["+", "-", "*", "/"]
    for i in operator_list:
        print(i)
    user_oper = input("Pick an operation:\n")
    b = int(input("What's the next number?:\n"))
    calculate(a, b, user_oper)


run = True
print(logo)
fist_number = int(input("What's the first number?:\n"))
while run:
    second_number(fist_number)
