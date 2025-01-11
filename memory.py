import random
import tkinter as tk
from tkinter import messagebox

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")

        # Initialize game variables
        self.cards = list(range(1, 9)) * 2  # 8 pairs of cards
        random.shuffle(self.cards)
        self.buttons = []
        self.flipped = []
        self.matched = []

        self.create_board()

    def create_board(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(4):  # 4 rows
            for j in range(4):  # 4 columns
                button = tk.Button(frame, text="", width=10, height=5, command=lambda i=i, j=j: self.flip_card(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def flip_card(self, i, j):
        index = i * 4 + j

        if index in self.flipped or index in self.matched:
            return  # Ignore clicks on flipped or matched cards

        self.buttons[index].config(text=str(self.cards[index]), state="disabled")
        self.flipped.append(index)

        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        first, second = self.flipped

        if self.cards[first] == self.cards[second]:
            self.matched.extend([first, second])
        else:
            self.buttons[first].config(text="", state="normal")
            self.buttons[second].config(text="", state="normal")

        self.flipped = []

        if len(self.matched) == len(self.cards):
            messagebox.showinfo("Congratulations!", "You matched all the cards!")
            self.reset_game()

    def reset_game(self):
        random.shuffle(self.cards)
        self.flipped = []
        self.matched = []

        for button in self.buttons:
            button.config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
