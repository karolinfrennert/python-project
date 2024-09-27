
choices = ['rock', 'paper', 'scissors']
player_input = input("Enter your choice (rock, paper, scissors): ").lower()
if player_input in choices:
  print(player_input)
else:
  print("Invalid input. Please enter rock, paper, or scissors.")
