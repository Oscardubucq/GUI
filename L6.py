import tkinter as tk
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0),('paper',1),('scissors',2)]

def computer_wins():
    global computer_score,player_score
    computer_score += 1
    winner_label.config(text="Computer wins!")
    computer_score_label.config(text=f"Computer: {computer_score}")
    player_score_label.config(text=f"Player: {player_score}")

def player_wins():
    global computer_score,player_score
    player_score += 1
    winner_label.config(text="Player wins!")
    computer_score_label.config(text=f"Computer: {computer_score}")
    player_score_label.config(text=f"Player: {player_score}")

def tie():
    global computer_score,player_score
    winner_label.config(text="It's a tie!")
    computer_score_label.config(text=f"Computer: {computer_score}")
    player_score_label.config(text=f"Player: {player_score}")

def player_choice(player_input):
    global player_score,computer_score
    print(player_input)
    computer_input = random.choice(options)
    print(computer_input)
    player_choice_label.config(text=f"Player chose: {player_input[0]}")
    computer_choice_label.config(text=f"Computer chose: {computer_input[0]}")
    
    if (player_input == computer_input):
        tie()
    
    if (player_input[1] == 0):
        if (computer_input[1] == 1):
            computer_wins()
        if (computer_input[1] == 2):
            player_wins()
    if (player_input[1] == 1):
        if (computer_input[1] == 0):
            player_wins()
        if (computer_input[1] == 2):
            computer_wins()
    if (player_input[1] == 2):
        if (computer_input[1] == 0):
            computer_wins()
        if (computer_input[1] == 1):
            player_wins()

root = tk.Tk()
root.title("Rock Paper Scissors")
root.config(bg="lightgreen")
root.geometry("600x600")
myFont = font.Font(family='Helvetica', size=18, weight='bold')
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 24), bg="yellow", fg="black")
title_label.pack(pady=20)

player_choice_label = tk.Label(root, text="Player chose: ", font=("Arial", 16), bg="yellow", fg="black")
player_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 16), bg="yellow", fg="black")
computer_choice_label.pack(pady=10)

winner_label = tk.Label(root, text="Winner: ", font=("Arial", 16), bg="yellow", fg="black")
winner_label.pack(pady=10)

paper_button = tk.Button(root, text="Paper", bg='red', command=lambda: player_choice(options[1]), font=myFont, fg="black")
paper_button.pack(pady=10)
rock_button = tk.Button(root, text="Rock", command=lambda: player_choice(options[0]), font=myFont, bg="pink", fg="black")
rock_button.pack(pady=10)
scissors_button = tk.Button(root, text="Scissors", command=lambda: player_choice(options[2]), font=myFont, bg="pink", fg="black")
scissors_button.pack(pady=10)

computer_score_label = tk.Label(root, text=f"Computer: {computer_score}", font=("Arial", 16), bg="lightblue", fg="black")
computer_score_label.pack(pady=10)
player_score_label = tk.Label(root, text=f"Player: {player_score}", font=("Arial", 16), bg="lightblue", fg="black")
player_score_label.pack(pady=10)

root.mainloop()

