import random

def display_result(player_choice, computer_choice, winner, player_wins, computer_wins):
    emoji_dict = {
        'r': '🪨',
        'p': '📄',
        's': '✂'
    }
    
    win_messages = [
        "You are the winner! You smashed it! 💥",
        "You won! You're on fire! 🔥",
        "You are the winner! You've got the magic touch! ✨"
    ]
    
    lose_messages = [
        "Oh no, you lost. Better luck next time! 🍀",
        "Dang you lost! The robots are taking over 🤖",
        "You lost... Don't give up! 💪"
    ]
    
    tie_messages = [
        "It's a tie! You can do better 😐",
        "It's a tie, no winners here...🤙🏻",
        "A draw...try again! ☯️"
    ]
    
    print(f"\nYour choice: {emoji_dict[player_choice]}")
    print(f"Computer's choice: {emoji_dict[computer_choice]}")

    if winner == 'tie':
        print(random.choice(tie_messages))
    elif winner == 'player':
        print(random.choice(win_messages))
    else:
        print(random.choice(lose_messages))

    print(f"Score: Player: {player_wins}, Computer: {computer_wins}")
    print("\n")
