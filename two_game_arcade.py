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
    """Print all highscores in a sorted manner."""
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

#Game 1: Guess the Number

def play_guess_number(player_name, highscores) -> str:
        if player_name not in highscores:
            highscores[player_name] = None
        while True:
            number = random.randint(1,50)
            guesses = 0

            while True:
                guess_input = input(
                    "Take a guess (type 'scores' to see leaderboard, 'm' for menu,type 'q' to quit): "
                ).lower()

                if guess_input == 'q':
                    print(f"Thanks for playing, {player_name}! Goodbye!")
                    save_highscores(highscores)
                    return 'quit'
                
                if guess_input == 'm':
                    return 'menu'
                
                if guess_input == 'scores':
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
                    print(f"Congratulations, {player_name}! You guessed the number {number} in {guesses} guesses.")
                    if highscores[player_name] is None or guesses < highscores[player_name]:
                        highscores[player_name] = guesses
                        print(f"New highscore for {player_name}!")
                    save_highscores(highscores)
                
                play_again = input("Do you want to play again? (y/n): ").lower()
                if play_again != 'y':
                    return 'menu'
                else:
                    break

#Game 2

def play_coin_flip(player_name):
    """Simple second game: guess heads or tails."""
    print("\n=== Coin Flip ===")
    print("Type 'heads' or 'tails'. Type 'm' for menu, 'q' to quit.")

    heads_count = 0
    tails_count = 0
    wins = 0
    losses = 0

    while True:
        choice = input("Your call (heads/tails): ").lower().strip()

        if choice == 'q':
            print(f"Thanks for playing, {player_name}! Goodbye!")
            quit()

        if choice == 'm':
            total_flips = heads_count + tails_count
            if total_flips > 0:
                print(f"\nSession stats for {player_name}")
                print(f" Total flips: {total_flips}")
                print(f"  Heads: {heads_count}, Tails: {tails_count}")
                print(f"  Wins: {wins}, Losses: {losses}\n")
            return
        
        if choice not in ("heads", "tails"):
            print("Please type 'heads' or 'tails' (or 'm' for menu).")
            continue

        result = random.choice(["heads", "tails"])
        print(f"The coin landed on {result}!")

        if result == "heads":
            heads_count += 1
        else:
            tails_count += 1

        if choice == result:
            print("Nice! You guessed it right!")
            wins += 1
        else:
            print("Oops, better luck next time.")
            losses += 1

        again = input("Flip again? (y/n): ").lower()
        if again != 'y':
            total_flips = heads_count + tails_count
            if total_flips > 0:
                print(f"\nSession stats for {player_name}:")
                print(f"  Total flips: {total_flips}")
                print(f"  Heads: {heads_count}, Tails: {tails_count}")
                print(f"  Wins: {wins}, Losses: {losses}\n")
            return

#Menu

def main():
    print("Welcome to the Python Arcade!")

    highscores = load_highscores()

    player_name = input("What's your name? ").strip()
    if not player_name:
        player_name = "Player"

    while True:
        print("\n=== Main Menu ===")
        print("1) Play Guess the Number")
        print("2) Play Coin Flip")
        print("3) Show Leaderboard")
        print("4) Change Player")
        print("5) Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            play_guess_number(player_name, highscores)
        elif choice == "2":
            play_coin_flip(player_name)
        elif choice == "3":
            show_leaderboard(highscores)
        elif choice == "4":
            # Change player (use same highscores dict)
            player_name = input("Enter new player name: ").strip()
            if not player_name:
                player_name = "Player"
            print(f"Current player is now: {player_name}")
        elif choice == "5":
            print("Exiting arcade. Goodbye!")
            save_highscores(highscores)
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()