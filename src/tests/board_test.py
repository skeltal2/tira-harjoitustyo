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

def test_illegal_move():
    board = Board(board_state=[
        2,4,2,4,
        4,2,4,2,
        2,4,2,4,
        4,2,4,2
        ])

    assert board.move(0) is False and not board.get_legal_moves()
    