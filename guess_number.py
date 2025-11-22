import random

print("Welcome to Guess the Number!")
number = random.randint(1,50)

while True:
    guess = int(input("Pick a number between 1 and 50: "))
    if guess < number:
        print("Too low! Try again! If you want to.")
    elif guess > number:
        print("Too high! Try again! If you want to.")
    else:
        print("You got it!")
        break