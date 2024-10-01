def get_player_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        player_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_input in choices:
            return player_input
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")
