import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 50.")
number = random.randint(1,50) #this will generate a random number between 1 and 50

guesses = 0

while True: #this will keep the game running until the user guesses the correct number
    guess_input = input("Take a guess: ") #this will take the user's input as a string
    if not guess_input.isdigit(): #this checks if the input is a valid number
        print("Please enter a valid number.")
        continue
    guess = int(guess_input)
    guesses += 1
    if guess < number:
        print("Too low! Try again!")
    elif guess > number:
        print("Too high! Try again!")
    else:
        print("You got it!")
        print(f"It took you {guesses} tries!")
        break