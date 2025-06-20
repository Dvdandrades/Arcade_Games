import sys
import random
from enum import Enum

def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    def play_rps():
        nonlocal player_wins, python_wins, game_count

        print(f"\n{name}, please enter:")
        print("1 for Rock")
        print("2 for Paper")
        print("3 for Scissors")

        player_choice = input("\nYour choice: ")

        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2 or 3.")
            return play_rps()

        player = int(player_choice)
        computer = random.choice([1, 2, 3])

        print(f"\n{name}, you chose {RPS(player).name.title()}.")
        print(f"Python chose {RPS(computer).name.title()}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins, python_wins
            if (player == 1 and computer == 3) or \
               (player == 2 and computer == 1) or \
               (player == 3 and computer == 2):
                player_wins += 1
                return f"{name}, you win!"
            elif player == computer:
                return "Tie game!"
            else:
                python_wins += 1
                return f"Python wins!\nSorry, {name}."

        print(decide_winner(player, computer))

        game_count += 1
        print(f"\nGame count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Python's wins: {python_wins}")

        while True:
            play_again = input("\nPlay again? (Y for Yes, Q to Quit): ").strip().lower()
            if play_again in ["y", "q"]:
                break
            print("Please enter Y or Q.")

        if play_again == "y":
            return play_rps()
        else:
            print("\n####")
            print("Thank you for playing!\n")
            return

    return play_rps()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Play Rock Paper Scissors with Python!"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
    sys.exit(f"Bye {args.name}!")
