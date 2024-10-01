import random

class RockPaperScissorsGame:
    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        return random.choice(['r', 'p', 's'])

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'tie'

        if (
            (player_choice == 'r' and computer_choice == 'scissors') or
            (player_choice == 's' and computer_choice == 'paper') or
            (player_choice == 'p' and computer_choice == 'rock')
        ):
            self.player_wins += 1
            return 'player'
        else:
            self.computer_wins += 1
            return 'computer'