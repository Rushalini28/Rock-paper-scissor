
import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("450x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#202438")

        self.player_score = 0
        self.computer_score = 0
        self.choices = ["Rock", "Paper", "Scissors"]

        title = tk.Label(
            root,
            text="ROCK PAPER SCISSORS",
            font=("Arial", 20, "bold"),
            bg="#202438",
            fg="white"
        )
        title.pack(pady=25)

        subtitle = tk.Label(
            root,
            text="Choose your move!",
            font=("Arial", 13),
            bg="#202438",
            fg="#cccccc"
        )
        subtitle.pack(pady=5)

        # Player choice buttons
        button_frame = tk.Frame(root, bg="#202438")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="🪨 Rock",
            width=10,
            font=("Arial", 12, "bold"),
            bg="#4b6584",
            fg="white",
            command=lambda: self.play("Rock")
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="📄 Paper",
            width=10,
            font=("Arial", 12, "bold"),
            bg="#4b6584",
            fg="white",
            command=lambda: self.play("Paper")
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="✂ Scissors",
            width=10,
            font=("Arial", 12, "bold"),
            bg="#4b6584",
            fg="white",
            command=lambda: self.play("Scissors")
        ).grid(row=0, column=2, padx=5)

        # Result display
        self.result_label = tk.Label(
            root,
            text="Make your first move!",
            font=("Arial", 15, "bold"),
            bg="#202438",
            fg="#ffd166",
            wraplength=400
        )
        self.result_label.pack(pady=25)

        self.choice_label = tk.Label(
            root,
            text="You: -    Computer: -",
            font=("Arial", 12),
            bg="#202438",
            fg="white"
        )
        self.choice_label.pack(pady=10)

        self.score_label = tk.Label(
            root,
            text="Your Score: 0  |  Computer: 0",
            font=("Arial", 14, "bold"),
            bg="#202438",
            fg="#06d6a0"
        )
        self.score_label.pack(pady=15)

        tk.Button(
            root,
            text="Reset Score",
            font=("Arial", 11, "bold"),
            bg="#ef476f",
            fg="white",
            command=self.reset_score
        ).pack(pady=15)

    def play(self, player_choice):
        computer_choice = random.choice(self.choices)

        self.choice_label.config(
            text=f"You: {player_choice}    "
                 f"Computer: {computer_choice}"
        )

        if player_choice == computer_choice:
            result = "It's a Draw!"
            color = "#ffd166"

        elif (
            (player_choice == "Rock" and computer_choice == "Scissors")
            or
            (player_choice == "Paper" and computer_choice == "Rock")
            or
            (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You Win! 🎉"
            color = "#06d6a0"
            self.player_score += 1

        else:
            result = "Computer Wins!"
            color = "#ef476f"
            self.computer_score += 1

        self.result_label.config(text=result, fg=color)

        self.score_label.config(
            text=f"Your Score: {self.player_score}  |  "
                 f"Computer: {self.computer_score}"
        )

    def reset_score(self):
        self.player_score = 0
        self.computer_score = 0

        self.result_label.config(
            text="Make your first move!",
            fg="#ffd166"
        )
        self.choice_label.config(text="You: -    Computer: -")
        self.score_label.config(
            text="Your Score: 0  |  Computer: 0"
        )


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
