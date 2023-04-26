import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.turn = "X"
        self.board = [" "] * 9

        self.cells = []
        for i in range(3):
            row = []
            for j in range(3):
                cell = tk.Button(
                    master, text="", font=("Arial", 24), width=8, height=4,
                    command=lambda i=i, j=j: self.play(i, j)
                )
                cell.grid(row=i, column=j)
                row.append(cell)
            self.cells.append(row)

        self.message = tk.Label(master, text="")
        self.message.grid(row=3, column=0, columnspan=3)

        self.restart_button = tk.Button(
            master, text="Restart", font=("Arial", 18), command=self.restart
        )
        self.restart_button.grid(row=4, column=0, columnspan=3)

    def play(self, i, j):
        if self.board[3*i+j] == " ":
            self.board[3*i+j] = self.turn
            self.cells[i][j].config(text=self.turn)
            if self.check_win():
                self.message.config(text=f"{self.turn} wins!")
                self.disable_cells()
            elif self.check_tie():
                self.message.config(text="Tie game!")
                self.disable_cells()
            else:
                self.turn = "O" if self.turn == "X" else "X"
                self.message.config(text=f"It's {self.turn}'s turn")

    def check_win(self):
        # check rows
        for i in range(3):
            if self.board[3*i] == self.board[3*i+1] == self.board[3*i+2] != " ":
                return True
        # check columns
        for j in range(3):
            if self.board[j] == self.board[j+3] == self.board[j+6] != " ":
                return True
        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def check_tie(self):
        return " " not in self.board

    def disable_cells(self):
        for row in self.cells:
            for cell in row:
                cell.config(state=tk.DISABLED)

    def restart(self):
        self.turn = "X"
        self.board = [" "] * 9
        for i in range(3):
            for j in range(3):
                self.cells[i][j].config(text="")
                self.cells[i][j].config(state=tk.NORMAL)
        self.message.config(text="")
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
