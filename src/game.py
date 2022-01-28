from board import Board

class Game:
    def __init__(self, mode=0, board=Board()):
        self.mode = mode
        self.board = board

    def loop(self):
        self.board.new_tile()
        while self.board.won == False:
            print("Siirtoja: "+str(self.board.get_moves())+"\n")
            self.board.new_tile()

            test_board = Board(self.board.get_list())
            if self.up(test_board) == self.down(test_board) == self.left(test_board) == self.right(test_board) == False:
                print("Ei laillisia siirtoja, hävisit pelin!")
                print("Suurin laatta: "+str(max(self.board.get_list())))
                return False
            
            while True:
                print(self.board)

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
        return True
    
    def left(self, board):
        return board.move(0)

    def right(self, board):
        return board.move(1)

    def down(self, board):
        return board.move(2)
    
    def up(self, board):
        return board.move(3)