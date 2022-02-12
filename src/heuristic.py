from board import Board
from math import log2, log

class Heuristic():

    def __init__(self, board:Board):
        self.board = board.clone()

    def evaluate(self):
        """
        Palutta pelikentän heuristisen arvon (int)
        """
        mono = self.monotonicity() # kasvava järjestys
        smooth = self.smoothness() # samat laatat vierekkäin
        free = self.free_tiles()
        maxt = self.max_tile()
        score = self.score()

        mono_weight = 1
        smooth_weight = 0.1
        free_weight = 5
        max_weight = 5
        score_weight = 0

        return sum((
            mono * mono_weight,
            smooth * smooth_weight,
            free * free_weight,
            maxt * max_weight,
            score * score_weight
        ))

    def monotonicity(self):
        """
        Laske monotonisuus, eli kuinka hyvin kaikki laatat ovat kasvavassa järjestyksessä jonkin kulman suuntaan.
        Paras monotonisuus on 0.
        """
        # Kaikkien suuntien monotonisuudet
        mono_scores = [0,0,0,0] # vasen, oikea, ylös, alas

        rows = self.board.rows
        cols = self.board.cols
        lst = self.board.get_list()

        # Käy läpi rivit
        for row in rows:
            for i, loc in enumerate(row[:-1]):
                # Vertaa tätä ja seuraavaa laattaa 
                curTile = lst[loc]
                nextTile = lst[row[i+1]]

                # Laske log2
                curValue = self.log_zero(curTile)
                nextValue = self.log_zero(nextTile)

                # Vertaa kuinka paljon laatat eroavat
                if curValue > nextValue:
                    # Vähennä vasen arvoa
                    mono_scores[0] += nextValue - curValue
                elif nextValue > curValue:
                    # Vähennä oikea arvoa
                    mono_scores[1] += curValue - nextValue

        # Käy läpi sarakkeet
        for col in cols:
            for i, loc in enumerate(col[:-1]):
                curTile = lst[loc]
                nextTile = lst[col[i+1]]

                curValue = self.log_zero(curTile)
                nextValue = self.log_zero(nextTile)

                if curValue > nextValue:
                    # Vähennä ylös arvoa
                    mono_scores[2] += nextValue - curValue
                elif nextValue > curValue:
                    # Vähennä alas arvoa
                    mono_scores[3] += curValue - nextValue

        # Palauttaa parhaan kulman. Ensin oikea vai vasen, sitten ylös vai alas.
        return max([mono_scores[0], mono_scores[1]]) + max(mono_scores[2], mono_scores[3])
    
    def smoothness(self):
        """
        Laske kuinka tasainen pelikentta on, eli kuinka paljon naapurilaattojen arvot eroavat.
        Paras tasaisuus on 0.
        """
        smth_score = 0
        lst = self.board.get_list()

        for i, tile in enumerate(lst):
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
        Laske vapaiden laattojen logaritmi
        """
        free = len(self.board.get_empty())
        return log(free) if free != 0 else 0
    
    def score(self):
        """
        Laske pisteiden logaritmi
        """
        score = self.board.get_score()
        return log(score) if score != 0 else 0

    def log_zero(self, i):
        """
        i > 0 palauttaa log2(i)
        i = 0 palauttaa 0
        """
        return log2(i) if i != 0 else 0

    def tile_merges(self, location:int):
        """
        Palautaa saman arvoisten naapurien määrän (int)

        location : int
            laatan sijainti
        """
        merges = 0
        lst = self.board.get_list()

        for i in self.board.get_neighbors(location):
            if i == lst[location]:
                merges += 1
        
        return merges