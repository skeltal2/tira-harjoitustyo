import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter.messagebox import showinfo
from board import Board
from minimax import Minimax

class UI():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("2048")

        self.frm = ttk.Frame(
            master=self.root,
            padding=10,
            #relief="solid"
        )
        self.frm.grid(column=0,row=0)

        self.control_frm = ttk.Frame(
            master=self.root,
            padding=10,
            #relief="solid"
        )
        self.control_frm.grid(column=1,row=0)

        self.tile_font = Font(
            family="Clear Sans",
            size=40,
            weight="bold"
        )

        self.labels = []
        self.tiles = []

        self.color_map = {
            2:("#776e65", "#eee4da"),
            4:("#776e65", "#ede0c8"),
            8:("#f9f6f2", "#f2b179"),
            16:("#f9f6f2", "#f59563"),
            32:("#f9f6f2", "#f67c5f"),
            64:("#f9f6f2", "#f65e3b"),
            128:("#f9f6f2", "#edcf72"),
            256:("#f9f6f2", "#edcc61"),
            512:("#f9f6f2", "#edc850"),
            1024:("#f9f6f2", "#edc53f"),
            2048:("#f9f6f2", "#edc22e")
        }

        self.move_map = {
            # WASD
            "a":0,
            "d":1,
            "s":2,
            "w":3,
            # Nuolet
            "Left":0,
            "Right":1,
            "Down":2,
            "Up":3
        }

        self.do_solve = False

        self.board = Board()
        self.setup_controls()

    def setup_controls(self):
        start_button = tk.Button(
            master=self.control_frm,
            text="Ratkaise!",
            width=20,
            height=4
        )

        exit_button = tk.Button(
            master=self.control_frm,
            text="Lopeta",
            width=20,
            height=4
        )

        start_button.bind('<ButtonRelease>', self.solve_button)
        exit_button.bind('<ButtonRelease>', self.quit_button)

        start_button.grid(row=0, column=0)
        exit_button.grid(row=1, column=0)
    
    def solve_button(self, event):
        self.do_solve = not self.do_solve
        self.solve()
    
    def quit_button(self, event):
        self.root.quit()

    def build_grid(self):
        for y in range(4):
            for x in range(4):
                text = tk.StringVar()
                text.set(0)
                label = tk.Label(
                    master=self.frm,
                    textvariable=text,
                    font=self.tile_font,
                    width=4,
                    height=2,
                    anchor="center",
                )
                label.grid(
                    column=x,
                    row=y,
                    padx=2,
                    pady=2
                )
                self.labels.append(label)
                self.tiles.append(text)
        self.update_grid()
    
    def update_grid(self):
        #väri testi [0,0,0,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
        new_tiles = self.board.get_list()
        for i in range(16):
            tile = new_tiles[i]
            f_color = "#f9f6f2"
            if tile == 0:
                self.tiles[i].set("")
                b_color = "#cdc1b4"
            else:
                self.tiles[i].set(tile)
                if new_tiles[i] in self.color_map:
                    f_color = self.color_map[tile][0]
                    b_color = self.color_map[tile][1]
                else:
                    b_color = "#3c3a33"
            self.labels[i].config(foreground = f_color)
            self.labels[i].config(background = b_color)
    
    def keypress(self, event):
        print(event)
        if event.keysym in self.move_map and not self.do_solve:
            self.handle_game(event.keysym)
    
    def handle_game(self, move):
        if self.move_map[move] in self.board.get_legal_moves():
            self.board.move(self.move_map[move])
            self.board.new_tile()
            self.update_grid()

        if max(self.board.get_list()) == 2048:
            showinfo(title="2048", message="Voitit Pelin!")
            self.root.quit()

        if self.board.get_legal_moves() is None:
            showinfo(title="2048", message="Hävisit Pelin!")
            self.root.quit()
    
    def solve(self, turn_time=10):
        result = Minimax(self.board, True).start()
        move = result[0]
        value = result[1]

        if max(self.board.get_list()) == 2048:
            showinfo(title="2048", message="Voitit Pelin!")
            self.root.quit()

        if move is None:
            showinfo(title="2048", message="Hävisit Pelin!")
            self.root.quit()
        else:
            self.board.move(move)
            self.board.new_tile()
            self.update_grid()
            if self.do_solve:
                self.root.after(turn_time, self.solve)

    def display(self):
        self.board.new_tile()
        self.board.new_tile()
        self.build_grid()
        self.root.bind('<KeyPress>',self.keypress)

        self.root.mainloop()

if __name__ == "__main__":
    UI().display()