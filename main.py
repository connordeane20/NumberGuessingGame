from random import randint

def random(num):
    for num in range(1):
        value = randint(0,100)
        return value


number = random("")
guess = 0

while guess != number:
    first_guess = input("Enter Guess: ")
    if number < int(first_guess):
        input("Number is lower than guess, press enter: ")
        continue
    elif number > int(first_guess):
        input("Number is higher than guess, press enter: ")
        continue
    else: print("You Win!")
    break