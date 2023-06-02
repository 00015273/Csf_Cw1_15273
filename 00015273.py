
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.player1_score = 0
        self.player2_score = 0
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Tic Tac Toe", font=("Helvetica", 24))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.scoreboard = tk.Label(self.master, text=f"Player 1: {self.player1_score}   |   Player 2: {self.player2_score}", font=("Helvetica", 18))
        self.scoreboard.grid(row=1, column=0, columnspan=3, pady=10)

        self.restart_button = tk.Button(self.master, text="Restart", font=("Helvetica", 18), command=self.restart)
        self.restart_button.grid(row=2, column=0, pady=10)

        self.new_game_button = tk.Button(self.master, text="New Game", font=("Helvetica", 18), command=self.new_game)
        self.new_game_button.grid(row=2, column=2, pady=10)

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.master, text=" ", font=("Helvetica", 18), width=5, height=2, command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row+3, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

    def make_move(self, row, col):
        if self.board[row][col] != " ":
            messagebox.showerror("Error", "Invalid Move!")
            return
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)
        if self.check_win_condition():
            messagebox.showinfo("Winner", f"{self.current_player} wins!")
            self.update_scores()
            self.restart()
        elif self.check_draw_condition():
            messagebox.showinfo("Draw", "It's a draw!")
            self.restart()
        else:
            self.current_player = "X" if self.current_player == "O" else "O"

    def check_win_condition(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_draw_condition(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def update_scores(self):
        if self.current_player == "X":
            self.player1_score += 1
        else:
            self.player2_score += 1
        self.scoreboard.config(text=f"Player 1: {self.player1_score}   |   Player 2: {self.player2_score}")

    def restart(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = " "
                self.buttons[row][col].config(text=" ")
        self.current_player = "X"

    def new_game(self):
        self.player1_score = 0
        self.player2_score = 0
        self.scoreboard.config(text=f"Player 1: {self.player1_score}   |   Player 2: {self.player2_score}")
        self.restart()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()



