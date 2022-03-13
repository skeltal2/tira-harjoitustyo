from math import log2, log
from .board import Board

class Heuristic():
    """
    Luo uusi Heuristic-olio.\n
    evaluate() laskee heuristisen arvon.

    board : Board
        arvioitava pelikenttä
    """

    def __init__(self, board:Board):
        self.board = board.clone()

    def evaluate(self):
        """
        Palutta pelikentän heuristisen arvon (int)
        """
        mono = self.monotonicity() # kasvava järjestys
        smooth = self.smoothness() # samat laatat vierekkäin
        free = self.free_tiles() # vapaat laatat
        maxt = self.max_tile() # suurin laatta
        force = self.force_corner() # suurin laatta kulmassa

        mono_weight = 1
        smooth_weight = 0.1
        free_weight = 2.5
        max_weight = 1
        force_corner_weight = 1.5

        return sum((
            mono * mono_weight,
            smooth * smooth_weight,
            free * free_weight,
            maxt * max_weight,
            force * force_corner_weight
        ))

    def monotonicity(self):
        """
        Laske monotonisuus, eli kuinka hyvin kaikki laatat ovat kasvavassa järjestyksessä.
        Paras monotonisuus on 0.
        """
        # Kaikkien suuntien monotonisuudet
        mono_scores = [0,0,0,0] # vasen, oikea, ylös, alas

        rows = self.board.rows
        cols = self.board.cols
        lst = self.board.get_list()

        # Käy läpi vasen ja oikea
        for row in rows:
            for i, loc in enumerate(row[:-1]):
                # Vertaa tätä ja seuraavaa laattaa
                cur_tile = lst[loc]
                next_tile = lst[row[i+1]]

                # Laske log2 (kuinka monta yhdistystä verrattavien laattojen välillä on)
                cur_value = self.log_zero(cur_tile)
                next_value = self.log_zero(next_tile)

                # Vertaa kuinka paljon laatat eroavat
                if cur_value > next_value:
                    # Vähennä vasen arvoa
                    mono_scores[0] += next_value - cur_value
                elif next_value > cur_value:
                    # Vähennä oikea arvoa
                    mono_scores[1] += cur_value - next_value

        # Käy läpi ylös ja alas
        for col in cols:
            for i, loc in enumerate(col[:-1]):
                cur_tile = lst[loc]
                next_tile = lst[col[i+1]]

                cur_value = self.log_zero(cur_tile)
                next_value = self.log_zero(next_tile)

                if cur_value > next_value:
                    # Vähennä ylös arvoa
                    mono_scores[2] += next_value - cur_value
                elif next_value > cur_value:
                    # Vähennä alas arvoa
                    mono_scores[3] += cur_value - next_value

        # Palauttaa parhaan kulman monotonisuuden. Ensin oikea vai vasen, sitten ylös vai alas.
        return max([mono_scores[0], mono_scores[1]]) + max(mono_scores[2], mono_scores[3])

    def smoothness(self):
        """
        Laske kuinka tasainen pelikenttä on, eli kuinka paljon naapurilaattojen arvot eroavat.
        Paras tasaisuus on 0.
        """
        smth_score = 0
        lst = self.board.get_list()

        for i, tile in enumerate(lst):
            if tile == 0:
                continue
            for neighbor in self.board.get_neighbors(i):
                if neighbor == 0:
                    continue
                smth_score -= abs(self.log_zero(tile)-self.log_zero(neighbor))

        return smth_score

    def max_tile(self):
        """
        Etsi suurin laatta, palauta sen log 2
        """
        return self.log_zero(max(self.board.get_list()))

    def free_tiles(self):
        """
        Laske vapaiden laattojen log e
        """
        free = len(self.board.get_empty())
        return log(free) if free > 0 else 0

    def force_corner(self):
        """
        Onko suurin laatta kulmassa?
        """
        lst = self.board.get_list()
        max_tile = max(lst)
        force_score = 0

        if len([i for i in lst if i == max_tile]) > 1:
            return 0
        for i, tile in enumerate(lst):
            if tile == max_tile:
                if len([n for n in self.board.get_neighbors(i) if n != 0]) > 2:
                    force_score -= self.log_zero(tile)

        return force_score

    @classmethod
    def log_zero(cls, i):
        """
        i > 0 palauttaa log2(i)\n
        i = 0 palauttaa 0
        """
        return log2(i) if i > 0 else 0
