import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter.messagebox import showinfo
from board import Board

class UI():

    def __init__(self):
        self.root = tk.Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        self.tile_font = Font(family="Clear Sans", size=20, weight="bold")
        self.labels = []
        self.tiles = []
        #[0,0,0,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
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
            65:0,
            68:1,
            83:2,
            87:3,
            # Nuolet
            37:0,
            39:1,
            40:2,
            38:3,
        }

        self.board = Board()
        self.board.new_tile()

    def build_grid(self):
        i = 0
        for y in range(4):
            for x in range(4):
                text = tk.StringVar()
                text.set(0)
                label = ttk.Label(
                    master=self.frm,
                    textvariable=text,
                    padding=20,
                    font=self.tile_font,
                    width=5,
                    anchor="center"
                )
                label.grid(column=x,row=y)
                self.labels.append(label)
                self.tiles.append(text)
                i += 1
        self.update_grid()
    
    def update_grid(self):
        new_tiles = self.board.get_list()
        for i in range(16):
            tile = new_tiles[i]
            f_color = "#f9f6f2"
            if tile == 0:
                self.tiles[i].set("")
                b_color = "#eee4da"
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
        if event.keycode in self.move_map:
            self.handle_game(event.keycode)
    
    def handle_game(self,move):
        moves = self.board.get_legal_moves()
        if max(self.board.get_list()) == 2048:
            showinfo(title="2048", message="Voitit Pelin!")
            self.root.quit()
        if moves is None:
            showinfo(title="2048", message="Hävisit Pelin!")
            self.root.quit()
        elif self.move_map[move] in moves:
            self.board.move(self.move_map[move])
            self.board.new_tile()
            self.update_grid()
    
    def display(self):
        self.build_grid()
        self.root.bind('<KeyPress>',self.keypress)

        self.root.mainloop()
        

if __name__ == "__main__":
    UI().display()