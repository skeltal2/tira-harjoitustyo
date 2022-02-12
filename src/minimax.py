from random import choice
from board import Board
from heuristic import Heuristic

class Minimax():

    def __init__(self, board=None):
        self.board = board
        self.big_number = 10**9

    def score_test(self):
        moves = self.board.get_legal_moves()
        if moves is None:
            return None
        
        scores = {}

        for direction in range(4):
            test_board = Board(board_state=self.board.get_list())
            test_board.move(direction)

            scores[direction] = test_board.get_score()
        
        best_moves = [d for d, v in scores.items() if v == max(scores.values())]

        return choice(best_moves)
    
    def start(self, depth:int=3, use_dynamic=True):
        """
        Aloita haku. Palauttaa parhaan siirron.

        depth : int
            Syvyys
        use_dynamic : bool
            Käyttää dynaamista syvyytta staattisen sijaan. Syvyys riippuu vapaiden laattojen määrästä.
        """
        if use_dynamic:
            depth = self.dynamic_depth(self.board)
        result = self.run(self.board.clone(), depth, None, -self.big_number, self.big_number, True)
        move = result[0]
        if move is None:
            moves = self.board.get_legal_moves()
            if moves is None:
                return None
            return choice(moves)
        return move

    def run(self, board:Board, depth:int, move:int, alpha:int, beta:int, maximizer:bool):
        moves = board.get_legal_moves()
        free = len(board.get_empty())
        if depth == 0 or moves is None or (free > 5 and depth < 2):
            return move, Heuristic(board).evaluate()

        if maximizer:
            value = -self.big_number
            for i in moves:
                prev_value = value
                child = board.clone()
                child.move(i)
                child_values = self.run(child.clone(), depth-1, i, alpha, beta, False)

                value = max((value, child_values[1]))
                alpha = max((value, alpha))
                if value > prev_value:
                    move = i
                if value > beta:
                    break

            return move, value
        
        else:
            value = self.big_number

            for i in board.get_empty():
                for tile in [2,4]:
                    child = board.clone()
                    child.insert_tile(tile, i)
                    child_values = self.run(child.clone(), depth, move, alpha, beta, True)

                    value = min((value, child_values[1]))
                    beta = min((value, beta))
                    if value < alpha:
                        break
            return move, value
    
    def dynamic_depth(self, board):
        """
        Palauttaa syvyysarvon, joka riippuu tyhjien laattojen määrästä (int)

        0 - 2 : 4
        3 - 5 : 3
        6 - 9 : 2
        10+   : 1

        board : Board
            Arvioitava pelikenttä
        """
        free = len(board.get_empty())

        lookup = {
            0:4,
            1:4,
            2:4,
            3:3,
            4:3,
            5:3,
            10:1,
            11:1,
            12:1,
            13:1,
            14:1,
            15:1
        }

        if free in lookup:
            return lookup[free]
        else:
            return 2
