from ast import Continue
from random import choice, random

class Board:
    """
    Pelilauta luokka. Luo uuden pelilaudan kutsuessa.

    board_state : list
        Pelilaudan laattojen arvot
    moves : int
        Siirtojen määrä
    score : int
        Pisteiden määrä
    """

    # Laattojen sijainnit:
    # 00 | 01 | 02 | 03
    # -----------------
    # 04 | 05 | 06 | 07
    # -----------------
    # 08 | 09 | 10 | 11
    # -----------------
    # 12 | 13 | 14 | 15

    def __init__(self, board_state:list=None, moves:int=0, score:int=0):
        """
        Asettaa pelilaudan arvot

        board_state : list
            Pelilaudan laattojen arvot
        moves : int
            Siirtojen määrä
        score : int
            Pisteiden määrä
        """
        if board_state is None or len(board_state) != 16:
            self.board_state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        else:
            self.board_state = board_state
        self.moves = moves
        self.score = score

        self.won = False
        self.rows = [
            [0,1,2,3],
            [4,5,6,7],
            [8,9,10,11],
            [12,13,14,15]
        ]

        self.cols = [
            [0,4,8,12],
            [1,5,9,13],
            [2,6,10,14],
            [3,7,11,15]
        ]

    def insert_tile(self, value:int, location:int):
        """
        Luo uuden laatan

        value : int
            Laatan arvo
        location : int
            Laatan sijainti (0-15)
        """
        self.board_state[location] = value

    def get_empty(self):
        """
        Etsii tyhjät laatat ja palauttaa niiden sijainnit (list)
        """
        empty = []
        for i in enumerate(self.board_state):
            if self.board_state[i[0]] == 0:
                empty.append(i[0])
        return empty

    def get_moves(self):
        """
        Palauttaa tehtyjen siirtojen määrän (int)
        """
        return self.moves

    def get_list(self):
        """
        Palauttaa kopion pelikentän laattojen arvoista (list)
        """
        return self.board_state.copy()

    def get_score(self):
        """
        Palauttaa pisteet (int)
        """
        return self.score

    def get_neighbors(self, loc:int):
        """
        Palauttaa laatan ensimmäisen viereisen laatan kaikkiin suuntiin (list)

        loc : int
            laatan sijainti
        """
        left = 0
        right = 0
        up = 0
        down = 0

        for row in self.rows:
            if loc in row:
                for i in row:
                    if self.board_state[i] == 0:
                        continue
                    if i < loc:
                        left = self.board_state[i]
                    elif i > loc:
                        right = self.board_state[i]
                        break
                break
                    
        for col in self.cols:
            if loc in col:
                for i in col:
                    if self.board_state[i] == 0:
                        continue
                    if i < loc:
                        up = self.board_state[i]
                    elif i > loc:
                        down = self.board_state[i]
                        break
                break

        return left,right,up,down

    def move(self, direction:int):
        """
        Siirtää kaikkia laattoja valittuun suuntaan. Palauttaa True jos siirto oli laillinen, muuten False.

        direction : int
            Suunta, mihin laattoja siirretään
            0: Vasen
            1: Oikea
            2: Alas
            3: Ylös
        """
        legal = False # jos mikään laatta ei liiku, siirto on laiton
        # vasen ja oikea siirto käyttää rivejä, ylös ja alas sarakkeita
        if direction in (2, 3):
            loc_table = self.cols
        else:
            loc_table = self.rows
        for location in loc_table:
            lst = location.copy()
            if direction in (1, 2):
                lst.reverse()
            skip = False
            for i in enumerate(lst):
                # käy läpi jokaisen laatan rivillä/sarakkeella
                current = i[0]
                if skip:
                    break
                j = current+1
                while j < len(lst):
                    # käy läpi laatan "edessä" olevat laatat
                    tile_loc = lst[current]
                    tile = self.board_state[tile_loc]
                    match_loc = lst[j]
                    match = self.board_state[match_loc]
                    # jos päästään loppuun asti ja lopussa on 0, muita siirtoja ei voi enää olla
                    if match == 0 and j == len(lst)-1:
                        skip = True
                        break
                    # yhdistä laatta samaan laattaan
                    if match == tile and match != 0:
                        self.board_state[tile_loc] *= 2
                        self.board_state[match_loc] = 0
                        legal = True
                        self.score += self.board_state[tile_loc]
                        if self.board_state[tile_loc] == 2048:
                            self.won = True
                        j += 1
                        break
                    # siirrä laatta tyhjään tilaan
                    if tile == 0 and match != 0:
                        self.board_state[tile_loc] = match
                        self.board_state[match_loc] = 0
                        legal = True
                    # laattaa ei voitu siirtää
                    elif match == 0:
                        j += 1
                    else:
                        break
        self.moves += 1
        return legal

    def new_tile(self, odds:int=0.9):
        """
        Luo uusi 2- tai 4-laatta satunnaiseen sijaintiin

        odds : int
            Todennäköisyys, että laattan arvo on 2 (normaali 0.9)
        """
        loc = choice(self.get_empty())
        if random() < odds:
            value = 2
        else:
            value = 4
        self.insert_tile(value, loc)

    def get_legal_moves(self):
        """
        Kokeilee kaikkia siirtoja ja palauttaa listan laillisista siirroista (list)
        """
        moves = []
        for i in range(4):
            board_copy = Board(board_state=self.get_list())
            if board_copy.move(i):
                moves.append(i)
        return moves if len(moves) > 0 else None

    def clone(self):
        """
        Luo uuden Board-olion samoilla arvoilla ja palauttaa sen (Board)
        """
        return Board(self.get_list(), self.get_moves(), self.get_score())

    def __str__(self):
        """
        Palauttaa pelikenttä listana (list)
        """
        tile_width = len(str(max(self.board_state)))
        tiles = []
        for i in self.board_state:
            extra = tile_width - len(str(i))
            tiles.append(extra*" "+str(i))

        return_string = ""

        for i in enumerate(tiles):
            return_string += tiles[i[0]]
            if i[0] in (3, 7, 11):
                return_string += "\n" + "-"*(4*tile_width+9)+"\n"
            elif i[0] != 15:
                return_string += " | "
            else:
                return_string += "\n"

        return return_string
