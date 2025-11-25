import random
import json
import os

HIGHSCORE_FILE = "highscores.json"

def load_highscores():
    """Load highscores from a JSON file. If the file doesn't exist, return an empty dict."""
    if not os.path.exists(HIGHSCORE_FILE):
        return {}
    try:
        with open(HIGHSCORE_FILE, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            else:
                return {}
    except (json.JSONDecodeError, OSError):
        return {}
    
def save_highscores(highscores):
    """Save highscores to a JSON file."""
    try:
        with open(HIGHSCORE_FILE, "w") as f:
            json.dump(highscores, f, indent=4)
    except OSError:
        print("Error saving highscores. Highscores will not be saved.")

def show_leaderboard(highscores):
    if not highscores or all(score is None for score in highscores.values()):
        print("No highscores yet. Be the first to set one!")
        return
    print("\nLeaderboard:")
    sorted_scores = sorted(
        [(player, score) for player, score in highscores.items() if score is not None],
        key=lambda x: x[1]
    )
    for i, (player, score) in enumerate(sorted_scores, start=1):
        print(f"{i}. {player} - {score} guesses")

    print("\n")

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 50.")

highscores = load_highscores()

player_name = input("Before we start, what's your name? ").strip()
if not player_name:
    player_name = "Player"

if player_name not in highscores:
    highscores[player_name] = None

while True:
    number = random.randint(1,50)
    guesses = 0

    while True:
        guess_input = input("Take a guess (type 'scores' to see leaderboard, type 'q' to quit): ").lower()
        if guess_input == 'q':
            print(f"Thanks for playing, {player_name}! Goodbye!")
            quit()
        if guess_input == "scores":
            show_leaderboard(highscores)
            continue
        if not guess_input.isdigit():
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
                save_highscores(highscores)
            else:
                print(f"The current high score is still {current_highscore} guesses.")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print(f"Thanks for playing, {player_name}! Goodbye!")
                save_highscores(highscores)
                quit()
            else:
                break