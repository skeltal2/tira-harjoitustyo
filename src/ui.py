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
        self.root.resizable(0, 0)

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

        self.score_font = Font(
            family="Clear Sans",
            size=15,
            weight="bold"
        )

        self.arrow_font = Font(
            family="Source Code Pro Black",
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
        self.game_over = False

        self.arrows = {0:"←", 1:"→", 2:"↓", 3:"↑"}

        self.board = Board()
        self.setup_controls()

    def setup_controls(self):
        start_button = tk.Button(
            master=self.control_frm,
            text="Ratkaise!",
            width=20,
            height=3
        )

        new_game_button = tk.Button(
            master=self.control_frm,
            text="Uusi Peli",
            width=20,
            height=3
        )

        exit_button = tk.Button(
            master=self.control_frm,
            text="Lopeta",
            width=20,
            height=3
        )

        self.move_display = tk.StringVar()
        self.move_display.set("-")

        move_label = tk.Label(
            master=self.control_frm,
            textvariable=self.move_display,
            font=self.arrow_font,
            width=6,
            #height=2
        )

        self.score_display = tk.StringVar()
        self.score_display.set("Pisteet:\n0"+"Siirto:\n0")

        score_label = tk.Label(
            master=self.control_frm,
            textvariable=self.score_display,
            font=self.score_font,
            width=6,
            height=4,
        )

        self.turn_timer = tk.Scale(
            master=self.control_frm,
            orient="horizontal",
            from_=1,
            to=1000,
        )
        self.turn_timer.set(25)

        self.stop_at_2048 = tk.BooleanVar()
        self.stop_at_2048.set(True)
        win_condition = tk.Checkbutton(
            master=self.control_frm,
            text="2048 voittaa pelin",
            variable=self.stop_at_2048,
            onvalue=True,
            offvalue=False
        )

        start_button.bind('<ButtonRelease>', self.solve_button)
        new_game_button.bind('<ButtonRelease>', self.new_game_button)
        exit_button.bind('<ButtonRelease>', self.quit_button)

        move_label.grid(row=3, pady=2)
        score_label.grid(row=4, pady=2)
        start_button.grid(row=0, pady=2)
        new_game_button.grid(row=5, pady=2)
        exit_button.grid(row=6, pady=2)
        self.turn_timer.grid(row=1, pady=2)
        win_condition.grid(row=2, pady=2)

    def solve_button(self, event):
        self.do_solve = not self.do_solve
        if self.game_over:
            self.new_game_button(None)
            self.do_solve = True
        self.solve()

    def quit_button(self, event):
        self.root.quit()

    def new_game_button(self, event):
        if not self.do_solve or self.game_over:
            self.board.__init__()
            self.game_over = False
            self.do_solve = False
            self.board.new_tile()
            self.board.new_tile()
            self.update_grid()

    def build_grid(self):
        for board_y in range(4):
            for board_x in range(4):
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
                    column=board_x,
                    row=board_y,
                    padx=2,
                    pady=2
                )
                self.labels.append(label)
                self.tiles.append(text)
        self.update_grid()

    def update_grid(self):
        #väri testi [0,0,0,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
        self.score_display.set(
            "Pisteet:\n"+
            str(self.board.get_score())+
            "\nSiirto:\n"+
            str(self.board.get_moves())
        )
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
        if event.keysym in self.move_map and not self.do_solve:
            self.handle_game(event.keysym)

    def handle_game(self, move_c):
        if self.game_over:
            return
        move = self.move_map[move_c]

        if self.board.move(move):
            self.move_display.set(self.arrows[move])
            self.board.new_tile()
            self.update_grid()

        if max(self.board.get_list()) == 2048 and not self.game_over and self.stop_at_2048.get():
            self.game_over = True
            showinfo(title="2048", message="Voitit Pelin!")
            return

        if self.board.get_legal_moves() is None:
            self.game_over = True
            showinfo(title="2048", message="Hävisit Pelin!")
            return

    def solve(self):
        result = Minimax(self.board, stop_at_2048=self.stop_at_2048.get()).start()
        move = result[0]
        value = result[1]
        print(value)

        if max(self.board.get_list()) == 2048 and not self.game_over and self.stop_at_2048.get():
            self.game_over = True
            showinfo(title="2048", message="Voitit Pelin!")
            return

        if move is None:
            self.game_over = True
            showinfo(title="2048", message="Hävisit Pelin!")
            return

        self.board.move(move)
        self.move_display.set(self.arrows[move])
        self.board.new_tile()
        self.update_grid()
        if self.do_solve:
            self.root.after(self.turn_timer.get(), self.solve)

    def display(self):
        self.board.new_tile()
        self.board.new_tile()
        self.build_grid()
        self.root.bind('<KeyPress>',self.keypress)

        self.root.mainloop()

if __name__ == "__main__":
    UI().display()
