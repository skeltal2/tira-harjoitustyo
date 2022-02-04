from board import Board

class Game:
    def __init__(self, terminal=True, board=Board()):
        self.terminal = terminal
        self.board = board

        if self.terminal:
            self.terminal_loop()
        else:
            self.algorithm_loop()

    def terminal_loop(self):
        self.board.new_tile()
        while self.board.won is False:
            print(f"Siirtoja: {str(self.board.get_moves())}\nPisteet: {self.board.get_score()}\n")
            self.board.new_tile()

            print(self.board)

            if not self.board.get_legal_moves():
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
        print("Voitit pelin!")
        print(self.board)
        return True

    def algorithm_loop(self):
        pass