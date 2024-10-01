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
            if game.player_wins > game.computer_wins:
                final_message = random.choice([
                    "You're the ultimate champion! 🏆",
                    "Victory is yours! 👑",
                    "You've mastered the art of rock, paper, scissors! 🎉"
                ])
            elif game.player_wins < game.computer_wins:
                final_message = random.choice([
                    "The computer reigns supreme! 🤖",
                    "It looks like you've been outplayed! 🙃",
                    "Tough luck! The computer wins this time! 💻"
                ])
            else:
                final_message = random.choice([
                    "It's a tie overall! Balance has been restored. ⚖️",
                    "Neither side wins. What a close match! 🕊️",
                    "An evenly matched battle! 🤝"
                ])
            
            print("\nThank you for playing! GG")
            print(f"Final Score: Player: {game.player_wins}, Computer: {game.computer_wins}")
            print(final_message)
            break

if __name__ == "__main__":
    main()
