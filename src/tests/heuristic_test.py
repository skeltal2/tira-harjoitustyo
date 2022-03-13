from math import log
from logic.board import Board
from logic.heuristic import Heuristic

def test_mono():
    board = Board(board_state=[
        8,16,32,64,
        4,8,16,32,
        2,4,8,16,
        0,2,4,8
    ])

    assert Heuristic(board).monotonicity() == 0

def test_smooth():
    board = Board(board_state=[
        8,0,8,0,
        8,8,0,8,
        8,0,8,8,
        0,8,0,8
    ])

    assert Heuristic(board).smoothness() == 0

def test_max_tile():
    board = Board()
    board.insert_tile(2048, 0)
    board.insert_tile(1024, 1)

    assert Heuristic(board).max_tile() == 11

def test_free_tiles():
    board = Board()
    for i in range(6):
        board.insert_tile(2,i)
    
    assert Heuristic(board).free_tiles() == log(10)

def test_corner():
    board = Board(board_state=[
        256,0,0,512,
        0,0,0,0,
        0,0,0,0,
        2048,0,0,1024
    ])

    assert Heuristic(board).force_corner() == 0

def test_not_corner():
    board = Board(board_state=[
        256,0,0,512,
        2,0,0,0,
        2048,2,0,0,
        128,0,0,1024
    ])

    assert Heuristic(board).force_corner() == -log(2048, 2)

def test_double_corner():
    board = Board(board_state=[
        128,0,0,512,
        0,0,0,0,
        2048,2,0,0,
        2048,0,0,1024
    ])

    assert Heuristic(board).force_corner() == 0

def test_eval():
    board = Board(board_state=[
        8,8,8,8,
        8,8,8,8,
        8,8,8,8,
        8,8,8,8
    ])

    assert Heuristic(board).evaluate() == 3