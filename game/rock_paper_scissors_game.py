import random

class RockPaperScissorsGame:
    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'tie'

        if (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'scissors' and computer_choice == 'paper') or
            (player_choice == 'paper' and computer_choice == 'rock')
        ):
            self.player_wins += 1
            return 'player'
        else:
            self.computer_wins += 1
            return 'computer'