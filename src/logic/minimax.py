
from random import choice
from .board import Board
from .heuristic import Heuristic

class Minimax():
    """
    Etsii parhaan siirron.
    board : Board
        Arvioitava pelikenttä
    stop_at_2048 : Bool
        Kentät, jotka sisältävät 2048-laatan, saavat paljon lisäpisteitä
    """

    def __init__(self, board=None, stop_at_2048=True):
        self.board = board
        self.big_number = 10**9
        self.sa2 = stop_at_2048

    def start(self, depth:int=3, use_dynamic:bool=True):
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
        value = result[1]
        if move is None:
            moves = self.board.get_legal_moves()
            if moves is None:
                return None, value
            return choice(moves), value
        return move, value

    def run(self, board:Board, depth:int, move:int, alpha:int, beta:int, maximizer:bool):
        """
        Suorita minimax haku alfa-beeta karsinnalla.
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
        # Jos on päästy puun pohjalle, tai ei voida liikkua pysäytä haku.
        if depth == 0 or moves is None:
            if moves is None:
                return move, -self.big_number
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
                if max(child.get_list()) == 2048 and self.sa2:
                    value += 100
                alpha = max((value, alpha))
                if value > prev_value:
                    move = i
                if value > beta:
                    break

            return move, value

        value = self.big_number
        # Kokeillaan kaikki vapaat paikat kummallakin laatalla ja jatketaan hakua huonommalla
        for i in board.get_empty():
            child_2 = board.clone()
            child_4 = board.clone()

            child_2.insert_tile(2, i)
            child_4.insert_tile(4, i)

            if Heuristic(child_2).evaluate() < Heuristic(child_4).evaluate():
                child = child_2
            else:
                child = child_4

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
        board : Board
            Arvioitava pelikenttä
        """
        free = len(board.get_empty())

        if free <= 6:
            return 3
        if free <= 11:
            return 2
        return 1