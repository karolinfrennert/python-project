from player_choice import get_player_choice
from rock_paper_scissors_game import RockPaperScissorsGame
from display_results import display_result
import random

def main():
    print("🎮 Welcome to Rock, Paper, Scissors! 🎮")
    game = RockPaperScissorsGame()

    while True:
        player_choice = get_player_choice()
        computer_choice = game.get_computer_choice()
        winner = game.determine_winner(player_choice, computer_choice)
        
        display_result(player_choice, computer_choice, winner, game.player_wins, game.computer_wins)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':   
            
            print("\nThank you for playing!")
            print(f"Final Score: Player: {game.player_wins}, Computer: {game.computer_wins}")
            break

if __name__ == "__main__":
    main()
