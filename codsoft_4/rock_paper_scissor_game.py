import tkinter as tk
import random

user_points = 0
computer_points = 0

def play(user_choice):
    global user_points, computer_points

    computer_choice = random.choice(['rock', 'paper', 'scissor'])

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        result = "You win this round!"
        user_points += 1
    else:
        result = "Computer wins this round!"
        computer_points += 1

    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_points} | Computer: {computer_points}")

    if user_points == 5 or computer_points == 5:
        winner = "You" if user_points == 5 else "Computer"
        result_label.config(text=f"{winner} won the game!")
        rock_button.config(state="disabled")
        paper_button.config(state="disabled")
        scissor_button.config(state="disabled")
        retry_button.pack(pady=10)


def retry_game():
    global user_points, computer_points
    user_points = 0
    computer_points = 0
    score_label.config(text="Score - You: 0 | Computer: 0")
    result_label.config(text="")
    user_label.config(text="Your Choice:")
    computer_label.config(text="Computer's Choice:")
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissor_button.config(state="normal")
    retry_button.pack_forget()

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")

title_label = tk.Label(window, text="Rock Paper Scissors Game", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)
user_label = tk.Label(window, text="Your Choice:", font=("Helvetica", 12))
user_label.pack()

computer_label = tk.Label(window, text="Computer's Choice:", font=("Helvetica", 12))
computer_label.pack()
result_label = tk.Label(window, text="", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)
score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12))
score_label.pack()

rock_button = tk.Button(window, text="Rock", width=15, command=lambda: play('rock'))
rock_button.pack(pady=5)
paper_button = tk.Button(window, text="Paper", width=15, command=lambda: play('paper'))
paper_button.pack(pady=5)
scissor_button = tk.Button(window, text="Scissor", width=15, command=lambda: play('scissor'))
scissor_button.pack(pady=5)
retry_button = tk.Button(window, text="Retry", width=15, command=retry_game)
window.mainloop()
