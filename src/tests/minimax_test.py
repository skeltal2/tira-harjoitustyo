from logic.minimax import Minimax
from logic.board import Board

def test_search_merges():
    board = Board(board_state=[
        0,0,2,64,
        0,0,64,128,
        0,0,2,64,
        0,0,4,64
    ])

    move = Minimax(board).start(3,False)[0]

    assert move == 2

def test_win():
    board = Board(board_state=[
        1024,2,4,2,
        512,4,2,4,
        256,2,4,1024,
        128,128,2,1024
    ])

    move = Minimax(board).start(3,False)[0]

    assert move in [2,3]