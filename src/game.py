from board import Board
from minimax import Minimax
from time import time

class Game:
    def __init__(self, player=True, print_to_terminal=True):
        self.player = player
        self.ptt = print_to_terminal

        self.arrows = {0:"←", 1:"→", 2:"↓", 3:"↑"}
    
    def play(self):
        self.board = Board()

        if self.player:
            return self.player_loop()
        else:
            return self.algorithm_loop()

    def player_loop(self):
        self.board.new_tile()
        while self.board.won is False:
            self.board.new_tile()
            if self.ptt:
                print(f"Siirtoja: {str(self.board.get_moves())}\nPisteet: {self.board.get_score()}\n")
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
        begin_time = time()
        self.board.new_tile()
        while True:
            self.board.new_tile()
            if self.ptt:
                print(self.board)
            move = Minimax(self.board).start(4)
            if move is None:
                break
            if self.ptt:
                print(self.arrows[move])
            self.board.move(move)

        finish_time = time() - begin_time
        if self.ptt:
            print(f"Siirrot: {self.board.get_moves()}\nPisteet: {self.board.get_score()}\nAika: {round(finish_time, 2)} s\nVoitto: {self.board.won}")
        
        return self.board.get_moves(), self.board.get_score(), finish_time, max(self.board.get_list())
