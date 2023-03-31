import random

def play_game(player_choice):
    
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    
    if player_choice == computer_choice:
        result = "tie"
    elif player_choice == "rock" and computer_choice == "scissors":
        result = "win"
    elif player_choice == "paper" and computer_choice == "rock":
        result = "win"
    elif player_choice == "scissors" and computer_choice == "paper":
        result = "win"
    else:
        result = "lose"

    
    return result, player_choice, computer_choice


player_choice = input("Choose rock, paper, or scissors: ")
result, player_choice, computer_choice = play_game(player_choice)
print(f"You {result}! You chose {player_choice} and the computer chose {computer_choice}.")
