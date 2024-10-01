def get_player_choice():
    choices = ['r', 'p', 's']
    while True:
        player_input = input("Enter your choice (r, p, s): ").lower()
        if player_input in choices:
            return player_input
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")
