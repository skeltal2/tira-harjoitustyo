from random import choice
from board import Board
from heuristic import Heuristic

class Minimax():
    """
    Etsii parhaan siirron.

    board : Board
        Arvioitava pelikenttä
    """

    def __init__(self, board=None):
        self.board = board
        self.big_number = 10**9

    def start(self, depth:int=3, use_dynamic=True):
        """
        Aloita haku. Palauttaa parhaan siirron.

        depth : int
            Syvyys
        use_dynamic : bool
            Käyttää dynaamista syvyyttä staattisen sijaan.
            Syvyys riippuu vapaiden laattojen määrästä.
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
        """
        Suorita minimax haku.

        board : Board
            Arvioitava pelikenttä
        depth : int
            Haun syvyys
        move : int
            Paras siirto
        alpha : int
            Alfa arvo
        beta : int
            Beeta arvo
        maximizer : bool
            Kumman vuoro? (max vai min)
        """
        moves = board.get_legal_moves()
        free = len(board.get_empty())
        # Jos on päästy puun pohjalle, tai ei voida liikkua tai vapaita laattoja on paljon
        # pysäytä haku.
        if depth == 0 or moves is None or (free > 5 and depth < 2):
            return move, Heuristic(board).evaluate()

        if maximizer:
            value = -self.big_number
            # Kokeillaan kaikki mahdolliset siirrot
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

        value = self.big_number

        # Kokeillaan kaikki mahdolliset 2- ja 4-laattojen sijainnit
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

    @classmethod
    def dynamic_depth(cls, board):
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

        if free >= 10:
            return 1
        if free >= 6:
            return 2
        if free >= 3:
            return 3
        if free >= 0:
            return 4
        return 2
