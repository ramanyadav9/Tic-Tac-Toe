import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'

        # Create buttons for the board
        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('Helvetica', 24), width=5, height=2,
                                              command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.buttons[row][col]['text'] == '':
            self.buttons[row][col]['text'] = self.current_player
            if self.check_win():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'O':
                    self.computer_move()

    def computer_move(self):
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == '']
        if available_moves:
            row, col = random.choice(available_moves)
            self.buttons[row][col]['text'] = 'O'
            if self.check_win():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'X'

    def check_win(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '':
                return True  # Check rows
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != '':
                return True  # Check columns

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            return True  # Check diagonal
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            return True  # Check reverse diagonal
        
        return False

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == '':
                    return False  # There is an empty cell
        return True  # Board is full

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
        self.current_player = 'X'
        if random.choice([True, False]):
            self.computer_move()  # Computer starts randomly

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
