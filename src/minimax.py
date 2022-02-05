from random import choice
from board import Board
from heuristic import Heuristic

class Minimax():

    def __init__(self, board=None):
        self.board = board
        self.big_number = 10**9

    def random_test(self):
        moves = self.board.get_legal_moves()
        return choice(moves) if moves is not None else None

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
    
    def start(self, depth:int=3):
        move = self.run(self.board.clone(), depth, None, True)[0]
        moves = self.board.get_legal_moves()
        if move is None:
            if moves is None:
                return None
            return choice(moves)
        return move

    def run(self, board:Board, depth:int, move:int, maximizer:bool):
        if depth == 0:
            return move, Heuristic(board).evaluate()

        if maximizer:
            value = -self.big_number
            moves = board.get_legal_moves()
            if moves is not None:
                for i in board.get_legal_moves():
                    prev_value = value
                    child = board.clone()
                    child.move(i)
                    child_values = self.run(child.clone(), depth-1, i, False)

                    value = max((value, child_values[1]))
                    if value > prev_value:
                        move = i

            return move, value
        
        else:
            b = board.clone()
            b.new_tile(1)
            return self.run(b.clone(), depth, move, True)
