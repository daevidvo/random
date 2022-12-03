import random

moves = ["rock", "paper", "scissor"]

def choose_moves():
    player_move = input("Choose your move (rock, paper, or scissor):")
    if player_move not in moves:
        print("Move does not exist, try again")
        return choose_moves()
    return player_move

def play_game():
    player_move = choose_moves()
    computer_move = random.choice(moves)
    print("What's your move?", player_move)
    print("The computer chooses", computer_move)

    if player_move == computer_move:
        print("Tied")
    elif player_move == "rock" and computer_move == "scissor":
        print("You won!")
    elif player_move == "scissor" and computer_move == "paper":
        print("You won!")
    elif player_move == "paper" and computer_move == "rock":
        print("You won!")
    else:
        print("You lost...")

play_game()