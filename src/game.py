from time import time
from board import Board
from minimax import Minimax

class Game:
    """
    Pelilogiikka luokka.

    Pelaaja-tilassa palauttaa True, jos peli voitettiin, muuten False.
    Algoritmi-tilassa palauttaa pelin tilastot.

    player : bool
        Luodaanko pelattava peli? Jos False, algoritmi pelaa.
    print_to_terminal : bool
        Tulostetaanko terminaaliin pelilauta joka vuoro?
    stop_when_win : bool
        Lopetetaanko peli, kun 2048-laatta on saavutettu.
    """
    def __init__(self, player=True, print_to_terminal=True, stop_when_win=False):
        self.player = player
        self.ptt = print_to_terminal
        self.sws = stop_when_win

        self.board = Board()
        self.arrows = {0:"←", 1:"→", 2:"↓", 3:"↑"}

    def play(self):
        """
        Aloita peli
        """

        if self.player:
            return self.player_loop()
        return self.algorithm_loop()

    def player_loop(self):
        """
        Pelilogiikka, jossa pelaaja tekee siirrot.
        """
        self.board.new_tile()
        while self.board.won is False:
            self.board.new_tile()
            if self.ptt:
                print(f"""Siirtoja: {
                    str(self.board.get_moves())
                    }\nPisteet: {self.board.get_score()}\n""")
                print(self.board)

            if not self.board.get_legal_moves():
                if self.ptt:
                    print("Ei laillisia siirtoja, hävisit pelin!")
                    print("Suurin laatta: "+str(max(self.board.get_list())))
                return False
            while True:

                move = input("Siirto (w,a,s,d):")
                legal = False

                if move == "w":
                    legal = self.board.move(3)
                elif move == "s":
                    legal = self.board.move(2)
                elif move == "a":
                    legal = self.board.move(0)
                elif move == "d":
                    legal = self.board.move(1)

                if not legal:
                    print("Laiton siirto!")
                else:
                    break
        if self.ptt:
            print("Voitit pelin!")
            print(self.board)
        return True

    def algorithm_loop(self):
        """
        Pelilogiikka, jossa algoritmi tekee siirrot
        """
        begin_time = time()
        self.board.new_tile()
        while True:
            if self.sws and self.board.won:
                break
            self.board.new_tile()
            if self.ptt:
                print(self.board)
            move = Minimax(self.board).start()
            if move is None:
                break
            if self.ptt:
                print(self.arrows[move])
            self.board.move(move)

        finish_time = time() - begin_time
        if self.ptt:
            print(f"""Siirrot: {self.board.get_moves()
            }\nPisteet: {self.board.get_score()
            }\nAika: {round(finish_time, 2)
            } s\nVoitto: {self.board.won}""")

        return (
            self.board.get_moves(), self.board.get_score(), finish_time, max(self.board.get_list())
            )
