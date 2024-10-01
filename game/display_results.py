import random

def display_result(player_choice, computer_choice, winner, player_wins, computer_wins):
    
    print(f"\nYour choice: ({player_choice})")
    print(f"Computer's choice: ({computer_choice})")

    if winner == 'tie':
        print('It is a tie')
    elif winner == 'player':
        print('You win!')
    else:
        print('Computer wins :(')

    print(f"Score: Player: {player_wins}, Computer: {computer_wins}")
    print("\n")
