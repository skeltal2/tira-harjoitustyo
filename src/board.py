from random import choice, random

class Board:

    # 00 | 01 | 02 | 03
    # -----------------
    # 04 | 05 | 06 | 07
    # -----------------
    # 08 | 09 | 10 | 11
    # -----------------
    # 12 | 13 | 14 | 15

    def __init__(self, board_state=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], moves=0):
        self.board_state = board_state
        self.moves = moves
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
    
    def insert_tile(self, value, n):
        self.board_state[n] = value
    
    def get_free(self):
        free = []
        for i in range(len(self.board_state)):
            if self.board_state[i] == 0:
                free.append(i)
        return free
    
    def get_moves(self):
        return self.moves

    def get_list(self):
        return self.board_state.copy()

    # 0: vasen, 1: oikea, 2: alas, 3: ylös
    def move(self,dir):
        legal_move = False
        if dir == 2 or dir == 3:
            loc_table = self.cols
        else:
            loc_table = self.rows

        for l in loc_table:
            lst = l.copy()
            if dir == 1 or dir == 2:
                lst.reverse()
            merge = -1
            free = -1
            for i in range(len(lst)):
                tile_loc = lst[i]
                tile = self.board_state[tile_loc]

                if tile == 0:
                    if free == -1:
                        free = tile_loc
                else:
                    if merge == -1 and free == -1:
                        merge = tile_loc
                        continue
                    else:
                        if tile == self.board_state[merge] and merge != -1:
                            self.board_state[merge] *= 2
                            self.board_state[tile_loc] = 0
                            legal_move = True
                            merge = -1
                            if free == -1:
                                free = tile_loc
                        else:
                            merge = tile_loc
                            if free == -1:
                                continue
                            merge = free
                            self.board_state[free] = tile
                            self.board_state[tile_loc] = 0
                            legal_move = True
                            free = tile_loc
            
        if not legal_move:
            return False
        else:
            self.moves += 1
            return True
    
    def new_tile(self, odds=0.9):
        loc = choice(self.get_free())
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

if __name__ == "__main__":
    b = Board()
    b.insert_tile(2,3)
    print(b)
    print(b.move(1))
    print(b)
    print(b.move(2))
    print(b)
    print(b.move(3))
    print(b)