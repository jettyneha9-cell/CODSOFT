from tkinter import *
import random

# Main window
app = Tk()
app.title("Rock Paper Scissors")
app.geometry("450x400")
app.resizable(False, False)

# Variables
user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]

# Functions
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text="You chose: " + user_choice)
    computer_label.config(text="Computer chose: " + computer_choice)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Score  You: {user_score}   Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(text="You chose: ")
    computer_label.config(text="Computer chose: ")
    result_label.config(text="")
    score_label.config(text="Score  You: 0   Computer: 0")

# UI
Label(app, text="Rock Paper Scissors Game", font=("Arial", 20, "bold")).pack(pady=10)

Button(app, text="Rock", width=12, height=2, font=("Arial", 12), command=lambda: play("Rock")).pack(pady=5)
Button(app, text="Paper", width=12, height=2, font=("Arial", 12), command=lambda: play("Paper")).pack(pady=5)
Button(app, text="Scissors", width=12, height=2, font=("Arial", 12), command=lambda: play("Scissors")).pack(pady=5)

user_label = Label(app, text="You chose: ", font=("Arial", 12))
user_label.pack(pady=10)

computer_label = Label(app, text="Computer chose: ", font=("Arial", 12))
computer_label.pack(pady=5)

result_label = Label(app, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=10)

score_label = Label(app, text="Score  You: 0   Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

Button(app, text="Play Again", command=reset_game, bg="blue", fg="white", width=15).pack(pady=10)

app.mainloop()
