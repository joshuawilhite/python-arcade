import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 50.")

highscores = {}

player_name = input("Before we start, what's your name? ")
if not player_name:
    player_name = "Player"

if player_name not in highscores:
    highscores[player_name] = None

while True: #this will keep the game running until the user guesses the correct number
    number = random.randint(1,50) #this generates a random number between 1 and 50
    guesses = 0 #this will keep track of how many guesses the user has taken

    while True: #this will keep asking the user for guesses until they get it right
        guess_input = input("Take a guess (or type 'q' to quit): ") #this will take the user's input as a string
        if guess_input == 'q':
            print(f"Thanks for playing, {player_name}! Goodbye!")
            quit()
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
            print(f"You got it, {player_name}!")
            print(f"It took you {guesses} tries!")

            current_highscore = highscores[player_name]
            if current_highscore is None or guesses < current_highscore:
                highscores[player_name] = guesses
                print(f"Congratulations, {player_name}! You have the new high score!")
            else:
                print(f"The current high score is still {current_highscore} guesses.")
            break