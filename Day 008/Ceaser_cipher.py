# Ceaser Cipher
from data import logo, alphabet

run = True
print(logo)


def ask_con():
    global run
    con = input(f"Type 'yes' if you want to go again. otherwise type 'no'.")
    if con == "no":
        run = False


def check(solve_message, user_message):
    num = 0
    message = ""
    for i in user_message:
        if i == " ":
            solve_message.insert(num, " ")
        num += 1
    for i in solve_message:
        message += i
    print(f"your message is {message}")
    ask_con()


def decode(user_message, user_shift):
    encode_message = []
    for i in user_message:
        index = 0
        for j in alphabet:
            if i == j:
                encode_message.append(alphabet[index - user_shift])
                break
            index += 1
    check(encode_message, user_message)


def encode(user_message, user_shift):
    encode_message = []
    for i in user_message:
        index = 0
        for j in alphabet:
            if i == j:
                encode_message.append(alphabet[index + user_shift])
                break
            index += 1
    check(encode_message, user_message)


while run:
    user_need = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    user_message = input("Type your message:\n").lower()
    user_shift = int(input("Type shift number: "))
    if user_need == "encode":
        encode(user_message, user_shift)
    elif user_need == "decode":
        decode(user_message, user_shift)
