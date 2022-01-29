from board import Board

class Game:
    def __init__(self, terminal=True, board=Board()):
        self.terminal = terminal
        self.board = board

        if self.terminal:
            self.terminal_loop()
        else:
            pass

    def terminal_loop(self):
        self.board.new_tile()
        while self.board.won == False:
            print(f"Siirtoja: {str(self.board.get_moves())}\nPisteet: {self.board.get_score()}\n")
            self.board.new_tile()

            print(self.board)

            test_board = Board(self.board.get_list())
            if self.up(test_board) == self.down(test_board) == self.left(test_board) == self.right(test_board) == False: # kokeile voiko mitään siirtoa tehdä
                print("Ei laillisia siirtoja, hävisit pelin!")
                print("Suurin laatta: "+str(max(self.board.get_list())))
                return False
            
            while True:

                move = input("Siirto (w,a,s,d):")
                legal = False

                if move == "w":
                    legal = self.up(self.board)
                elif move == "s":
                    legal = self.down(self.board)
                elif move == "a":
                    legal = self.left(self.board)
                elif move == "d":
                    legal = self.right(self.board)

                if legal:
                    break
                else:
                    print("Laiton siirto!")
                    
        print("Voitit pelin!")
        print(self.board)
        return True
    
    def left(self, board):
        return board.move(0)

    def right(self, board):
        return board.move(1)

    def down(self, board):
        return board.move(2)
    
    def up(self, board):
        return board.move(3)