def initialise_board():
    """ The function initialise_board takes in a list of nine items that each contain a . as a str to represent
    an initially empty cell on the board

    Arguments
    _________
    No inputs

    Returns
    _______
    Output 1: a list representing the board

    Notes
    _____
    None """

    board = [".", ".", ".", ".", ".", ".", ".", ".", "."]

    return board


def display_board(board):
    """ The function display_board displays to screen the 3 x 3 board

    Arguments
    _________
    Input 1: a list representing the board

    Returns
    _______
    No outputs

    Notes
    _____
    None """

    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

    return None


def get_current_turn_number(board):
    """ The function get_turn_number uses the board to determine the current number by calculating the number of
        non-empty cells

    Arguments
    _________
    Input 1: a list representing the board

    Returns
    _______
    Output 1: an int equal to the current turn number

    Notes
    _____
    None """

    turn = 1
    for i in range(len(board)):
        if board[i] != ".":
            turn += 1

    return turn


def get_current_player(board):
    """The function get_current_player uses the board to determine the current player which can be represented by an 'X'
       for player 1 (who always goes on the first turn) or an 'O' for player 2

    Arguments
    _________
    Input 1: a list representing the board

    Returns
    _______
    Output 1: a str representing the current player

    Notes
    _____
    None

    Examples
    ________
    board = [’.’, ’.’, ’.’, ’.’, ’.’, ’.’, ’.’, ’.’, ’.’]
    Current player: X

    board = [’O’, ’.’, ’X’, ’.’, ’X’, ’.’, ’.’, ’.’, ’.’]
    Current player: O """

    turn = get_current_turn_number(board)
    if turn % 2 != 0:
        current_player = "X"
    else:
        current_player = "O"

    return current_player


def play_turn(board, row, column):

    validity = False
    if (1 <= row <= 3) and (1 <= column <= 3):
        current_player = get_current_player(board)
        position = 3 * (row - 1) + column - 1
        if board[position] == ".":
            board[position] = current_player
            validity = True
        elif board[position] != ".":
            board[position] = board[position]
            validity = False

    return board, validity


def check_draw(board):

    draw = True
    count = 0
    for i in range(len(board)):
        if board[i] == ".":
            count += 1

    if count > 0:
        draw = False

        return draw

    for i in range(0, 3):
        if board[3 * i] == board[3 * i + 1] == board[3 * i + 2]:
            draw = False

        if board[i] == board[i + 3] == board[i + 6]:
            draw = False

        if board[0] == board[4] == board[8]:
            draw = False

        if board[2] == board[4] == board[6]:
            draw = False

    return draw


def check_win(board):

    win = False
    winner = None

    for i in range(0, 3):
        if ((board[3 * i] == board[3 * i + 1] == board[3 * i + 2] != '.')
                and (board[3 * i] is not None)):
            win = True
            winner = board[3 * i]
            break

        elif ((board[i] == board[i + 3] == board[i + 6] != '.')
                and (board[i] is not None)):
            win = True
            winner = board[i]
            break

        elif ((board[0] == board[4] == board[8] != '.')
              or (board[2] == board[4] == board[6] != '.')
                and (board[4] is not None)):
            win = True
            winner = board[4]
            break

    draw = check_draw(board)
    if draw is True:
        win = False
        winner = None

    return win, winner


def play_game():

    board = initialise_board()

    display_board(board)

    turn = get_current_turn_number(board)
    print("Current turn number is: " + str(turn))

    current_player = get_current_player(board)
    print("Current player is: " + str(current_player))

    row = input("Enter row: ")
    column = input("Enter column: ")

    while (not row.isdigit()) or (not column.isdigit()):
        row = input("Enter row again: ")
        column = input("Enter column again: ")

    row = int(row)
    column = int(column)

    board, validity = play_turn(board, row, column)

    while validity is False:
        row = input("Enter row again: ")
        column = input("Enter column again: ")

        while (not row.isdigit()) or (not column.isdigit()):
            row = input("Enter row again: ")
            column = input("Enter column again: ")

        row = int(row)
        column = int(column)

        board, validity = play_turn(board, row, column)

    draw = check_draw(board)
    win, winner = check_win(board)

    display_board(board)

    while (draw is False) and (win is False):
        turn = get_current_turn_number(board)
        print("Current turn number is: " + str(turn))

        current_player = get_current_player(board)
        print("Current player is: " + str(current_player))

        row = input("Enter row: ")
        column = input("Enter column: ")

        while (not row.isdigit()) or (not column.isdigit()):
            row = input("Enter row again: ")
            column = input("Enter column again: ")

        row = int(row)
        column = int(column)

        board, validity = play_turn(board, row, column)

        while validity is False:
            row = input("Enter row again: ")
            column = input("Enter column again: ")

            while (not row.isdigit()) or (not column.isdigit()):
                row = input("Enter row again: ")
                column = input("Enter column again: ")

            row = int(row)
            column = int(column)

            board, validity = play_turn(board, row, column)

        draw = check_draw(board)
        win, winner = check_win(board)

        display_board(board)

    if draw is True:
        print("Game is a Draw :(")
        display_board(board)
    else:
        print("Winner is " + winner + "!")
        display_board(board)

    print("----THE END----")
    return None
