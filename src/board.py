from random import choice, random

class Board:

    # Laattojen sijainnit:
    # 00 | 01 | 02 | 03
    # -----------------
    # 04 | 05 | 06 | 07
    # -----------------
    # 08 | 09 | 10 | 11
    # -----------------
    # 12 | 13 | 14 | 15

    def __init__(self, board_state=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], moves=0, score=0):
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
    
    def insert_tile(self, value, n): # luo uusi laatta
        self.board_state[n] = value
    
    def get_empty(self): # palauttaa tyhjät laatat
        empty = []
        for i in range(len(self.board_state)):
            if self.board_state[i] == 0:
                empty.append(i)
        return empty
    
    def get_moves(self): # palauttaa siirtojen määrän
        return self.moves

    def get_list(self): # palauttaa pelikentän listana
        return self.board_state.copy()
    
    def get_score(self):
        return self.score

    # 0: vasen, 1: oikea, 2: alas, 3: ylös
    def move(self,dir):
        legal = False # jos mikään laatta ei liiku, siirto on laiton
        # vasen ja oikea siirto käyttää rivejä, ylös ja alas sarakkeita
        if dir == 2 or dir == 3:
            loc_table = self.cols
        else:
            loc_table = self.rows
        for l in loc_table:
            lst = l.copy()
            if dir == 1 or dir == 2:
                lst.reverse()
            skip = False
            for i in range(len(lst)):
                if skip:
                    break
                j = i+1
                while j < len(lst):
                    tile_loc = lst[i]
                    tile = self.board_state[tile_loc]
                    match_loc = lst[j]
                    match = self.board_state[match_loc]
                    if match == 0 and j == len(lst)-1: # jos päästään loppuun asti ja lopussa on 0, muita siirtoja ei voi enää olla
                        skip = True
                        break
                    if match != 0:
                        if match == tile:
                            self.board_state[tile_loc] *= 2
                            self.board_state[match_loc] = 0
                            legal = True
                            self.score += self.board_state[tile_loc]
                            j += 1
                        elif tile == 0 and match != 0:
                            self.board_state[tile_loc] = match
                            self.board_state[match_loc] = 0
                            legal = True
                        else:
                            break
                    j += 1
                #print(self)
                #print(legal)
        self.moves += 1
        return True if legal else False # oliko siirto laillinen?
            

    def new_tile(self, odds=0.9): # luo uuden 2- tai 4-laatan (normaalisti 90% 2-laattoja)
        loc = choice(self.get_empty())
        if random() < odds:
            value = 2
        else:
            value = 4
        self.insert_tile(value, loc)

    def __str__(self):
        tile_width = len(str(max(self.board_state)))
        tiles = []
        for i in self.board_state:
            n = tile_width - len(str(i))
            tiles.append(n*" "+str(i))
        
        return_string = ""

        for i in range(len(tiles)):
            return_string += tiles[i]
            if i == 3 or i == 7 or i == 11:
                return_string += "\n" + "-"*(4*tile_width+9)+"\n"
            elif i != 15:
                return_string += " | "
            else:
                return_string += "\n"

        return return_string