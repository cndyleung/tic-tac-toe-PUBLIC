from functions_ttt import *


def test_check_game_win_tricky_board():
    board = ["O", "O", "X", "O", "X", "X", "X", ".", "."]
    is_win, player = check_win(board)
    assert (player == "X")


def test_get_current_turn_number():
    board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
    turn = get_current_turn_number(board)
    assert (turn == 1)


def test_get_current_player():
    board = ["X", "X", "O", ".", ".", ".", ".", "O", "X"]
    player = get_current_player(board)
    assert (player == "O")


def test_play_turn():
    board = ["X", "X", "O", ".", ".", ".", ".", "O", "X"]
    row = 1
    column = 1
    board, validity = play_turn(board, row, column)
    assert (board == ["X", "X", "O", ".", ".", ".", ".", "O", "X"])
    assert (validity is False)


def test_check_draw():
    board = ["O", "X", "O", "O", "X", "X", "X", "O", "O"]
    draw = check_draw(board)
    assert (draw is True)


def text_check_win():
    board = ["X", "O", ".", ".", "X", "O", ".", ".", "X"]
    win, winner = check_win(board)
    assert (win is True)
    assert (winner is "X")