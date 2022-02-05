from board import Board

class Heuristic():

    def __init__(self, board:Board):
        self.board = board

    def evaluate(self):
        value = self.board.get_score() + max(self.board.get_list())

        return value
