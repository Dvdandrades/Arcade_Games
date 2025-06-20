import sys
import random
import argparse

def start_guessing_game(name="PlayerOne"):
    game_count = 0
    player_wins = 0

    while True:
        player_choice = input(f"\n{name}, guess which number I'm thinking of... 1, 2 or 3:\n")

        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2 or 3.")
            continue

        computer_choice = random.randint(1, 3)
        player_choice = int(player_choice)

        print(f"\n{name}, you chose {player_choice}")
        print(f"I was thinking about the number {computer_choice}.\n")

        if player_choice == computer_choice:
            player_wins += 1
            print(f"{name}, you win!")
        else:
            print(f"Sorry, {name}. Better luck next time.")

        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Winning percentage: {player_wins / game_count:.2%}")

        while True:
            play_again = input("\nPlay again? (Y for Yes, Q to Quit): ").strip().lower()
            if play_again in ["y", "q"]:
                break
            print("Please enter Y or Q.")

        if play_again == "q":
            print("\n####")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!")
            else:
                return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    start_guessing_game(args.name)
