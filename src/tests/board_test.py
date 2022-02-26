from board import Board

def test_move_row():
    board = Board(board_state=[
        2,2,2,2,
        2,2,2,4,
        2,0,0,2,
        2,0,2,4
        ])

    board.move(1)

    assert board.get_list() == [
        0,0,4,4,
        0,2,4,4,
        0,0,0,4,
        0,0,4,4
    ]

def test_move_col():
    board = Board(board_state=[
        2,2,2,2,
        2,2,0,2,
        2,2,0,0,
        2,4,2,4
        ])

    board.move(2)

    assert board.get_list() == [
        0,0,0,0,
        0,2,0,0,
        4,4,0,4,
        4,4,4,4
    ]

def test_game_win():
    board = Board()
    board.insert_tile(1024,0)
    board.insert_tile(1024,1)
    board.move(0)

    assert board.won is True

def test_moves():
    board = Board()
    board.insert_tile(2,5)

    assert board.get_legal_moves() == [0,1,2,3]

def test_no_moves():
    board = Board(board_state=[
        2,4,2,4,
        4,2,4,2,
        2,4,2,4,
        4,2,4,2
        ])

    assert board.move(0) is False and not board.get_legal_moves()
    
def test_empty():
    board = Board(board_state=[
        2,2,2,2,
        2,2,2,2,
        0,0,0,0,
        0,0,0,0
        ])
    
    assert board.get_empty() == [8,9,10,11,12,13,14,15]

def test_new_tile():
    board_1 = Board()
    board_1.new_tile(1)
    board_2 = Board()
    board_2.new_tile(0)

    assert max(board_1.get_list()) == 2 and max(board_2.get_list()) == 4

def test_str():
    board = Board()

    assert str(board) == "0 | 0 | 0 | 0\n-------------\n0 | 0 | 0 | 0\n-------------\n0 | 0 | 0 | 0\n-------------\n0 | 0 | 0 | 0\n"

def test_neighbors():
    board = Board(board_state=[
        2,4,2,2,
        8,64,0,16,
        2,0,0,2,
        2,32,2,2
        ])
    
    assert sorted(board.get_neighbors(5)) == [4,8,16,32]