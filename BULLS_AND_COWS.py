"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Daniel Proisl
email: dan.proisl@gmail.com
discord: Daniel P#9243
"""
import random

def duplicity_tst(number: str) -> bool:
    """vrati True pokud se v number nachazi duplicity
    jinak vrati False"""
    digits = []
    for digit in number:
        if digit in digits:
            return True
        else:
            digits.append(digit)
    return False

separator = 47 * "-"
print(f"""Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter a number:
{separator}""")

game_on = True

while True:
    random_number = str(random.choice(range(1000, 9999)))
    if random_number[0] == 0:
        continue
    elif duplicity_tst(random_number):
        continue
    else:
        break
# test_number = "2017"
# print(random_number)  #kontrola
guesses = 0
while game_on:
    bulls = 0
    cows = 0
    while True:
        user_guess = input(">>> ")

        if not user_guess.isnumeric():      #kontrola uzivatelskeho vstupu
           print("You have to enter a number")
        elif user_guess[0] == "0":
           print("The number can't start with 0")
        elif len(user_guess) != 4:
            print("The number must be four-digit")
        elif duplicity_tst(user_guess):      #duplikaty
            print("The number can't contain duplicit digits")
        else:
            guesses += 1
            break

    for i in range(4):

        if user_guess[i] == random_number[i]:
            bulls += 1
        elif user_guess[i] in random_number and user_guess[i] != random_number[i]:
            cows += 1

    if bulls == 1:
        bulls_txt = "bull"
    else:
        bulls_txt = "bulls"

    if cows == 1:
        cows_txt = "cow"
    else:
        cows_txt = "cows"

    if bulls == 4:
        game_on = False
        print("Nailed it! Good job")

        continue

    print(f"{bulls} {bulls_txt}, {cows} {cows_txt}")
    print(separator)

print(f"You guessed the number in {guesses} guesses.")
