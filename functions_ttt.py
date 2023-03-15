def initialise_board():
    """
    The function initialise_board takes in a list of nine items that each contain a . as a str to represent
    an initially empty cell on the board

    Arguments
    _________
    No inputs

    Returns
    _______
    Output 1: a list representing the board

    Notes
    _____
    The list will always have nine items
    """

    # Create a list and assign it to a variable named board.
    board = [".", ".", ".", ".", ".", ".", ".", ".", "."]

    return board


def display_board(board):
    """
    The function display_board displays to screen the 3 x 3 board using the print function

    Arguments
    _________
    Input 1: a list representing the board

    Returns
    _______
    No outputs

    Notes
    _____
    None
    """

    # Split the list into three rows by indexing and printing three elements at a time.
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

    return None


def get_current_turn_number(board):
    """
    The function get_current_turn_number uses the board to determine the current turn number by calculating the number
    of non-empty cells

    Arguments
    _________
    Input 1: a list representing the board

    Returns
    _______
    Output 1: an int equal to the current turn number

    Notes
    _____
    The first turn number is always 1 (e.g. when there is an empty board)
    """

    # This for loop iterates through each element in the list to find how many non-empty elements there are to determine
    # the turn. If the board is fully empty then the turn number is 1.
    turn = 1
    for i in range(len(board)):
        if board[i] != ".":
            turn += 1

    return turn


def get_current_player(board):
    """
    The function get_current_player uses the board to determine the current player which can be represented by an
    'X' for player 1 or an 'O' for player 2

    Arguments
    _________
    Input 1: a list representing the board

    Returns
    _______
    Output 1: a str representing the current player

    Notes
    _____
    - Player 1 ('X') always goes on the first turn
    - Players alternate i.e. the same player does not go twice in a row

    Examples
    ________
    board = [’.’, ’.’, ’.’, ’.’, ’.’, ’.’, ’.’, ’.’, ’.’]
    Current player: X

    board = [’O’, ’.’, ’X’, ’.’, ’X’, ’.’, ’.’, ’.’, ’.’]
    Current player: O
    """

    # Call the function get_turn_number to determine the turn number.
    turn = get_current_turn_number(board)

    # If the turn is odd the current player is X - Use the modulus function to determine if it is odd (e.g. the
    # remainder of the turn divided by 2 is not equal to zero).
    if turn % 2 != 0:
        current_player = "X"

    # If the turn is even the current player is O
    else:
        current_player = "O"

    return current_player


def play_turn(board, row, column):
    """
    The function play_turn attempts to play a turn, using a provided row and column, on the board

     Arguments
     _________
     Input 1: a list representing the board
     Input 2: an int representing the row number of the requested move (1 for top, 2 for middle, 3 for bottom)
     Input 3: an int representing the column number of the requested move (1 for the left, 2 for the middle, 3 for the
              right)

     Returns
     _______
     Output 1: a list representing the updated board. If the requested move was invalid, this will be identical to
               Input 1
     Output 2: a bool representing if the turn was valid (True for a valid move, False for an invalid move)

     Notes
     _____
     None
     """

    # Initialise the validity as false.
    validity = False

    # Requested row and column cannot be less than 1 or more than 3 to be valid.
    if (1 <= row <= 3) and (1 <= column <= 3):
        current_player = get_current_player(board)

        # Translate the requested row and column position in the 3 x 3 board into an index in the list.
        position = 3 * (row - 1) + column - 1

        # The position of the requested move must be empty to be valid. The empty cell is replaced with the current
        # player if the move is valid.
        if board[position] == ".":
            board[position] = current_player
            validity = True
        elif board[position] != ".":
            board[position] = board[position]
            validity = False

    return board, validity


def check_draw(board):
    """
    The function check_draw determines if the game has ended in a draw

     Arguments
     _________
     Input 1: a list representing the board

     Returns
     _______
     Output 1: a bool representing if the game is a draw (True) or not (False)

     Notes
     _____
     None
     """

    # Initialise the draw as true.
    draw = True

    # Count determines the amount of empty cells on the board.
    count = 0
    for i in range(len(board)):
        if board[i] == ".":
            count += 1

    # If the count is more than 0, the draw is false and immediately returned because more moves can be made to
    # potentially win.
    if count > 0:
        draw = False

        return draw

    # This for loop checks for the 8 possible winning patterns. If one of them are true, then the draw is false.
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
    """
    The function check_win determines if there is a winning player based on the board, and if so which player has
    won

     Arguments
     _________
     Input 1: a list representing the board

     Returns
     _______
     Output 1: a bool representing if the game has been won (True) or not (False)
     Output 2: a None-type if there is no winner, or a str representing the winning player (X or O) if there is one

     Notes
     _____
     The winning player is the first to get three in a row on the board
     """

    # Initialise the win as false and the winner as none.
    win = False
    winner = None

    # This for loop checks for 1 of the 8 winning patterns and makes sure that it is a valid win by all having the same
    # element (not a '.') and by not being a none-type .
    for i in range(0, 3):
        if ((board[3 * i] == board[3 * i + 1] == board[3 * i + 2] != '.')
                and (board[3 * i] is not None)):

            # Once a win has been found the conditional loop breaks and stores the result in the variables win and
            # winner and skips the remaining conditionals to improve efficiency.
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

    # Call the check draw function. If the draw is true, then the win is false and the winner is none.
    draw = check_draw(board)
    if draw is True:
        win = False
        winner = None

    return win, winner


def play_game():
    """
    The function play_game plays the game from start to finish

     Arguments
     _________
     No inputs

     Returns
     _______
     No outputs

     Notes
     _____
     No inputs or outputs as this function handles user interaction and provides the game with a very basic form of user
    interface
    """

    # Call the functions initialise_board, display_board, get_turn_number and get_turn_player to display the current
    # board, current turn and current player on each turn.
    board = initialise_board()

    display_board(board)

    turn = get_current_turn_number(board)
    print("Current turn number is: " + str(turn))

    current_player = get_current_player(board)
    print("Current player is: " + str(current_player))

    # Use the input command to obtain from a user the desired row and column number for their turn.
    row = input("Enter row: ")
    column = input("Enter column: ")

    # While the str input of the row and column is not a digit (e.g. 'e'), prompt the user to enter the values again.
    while (not row.isdigit()) or (not column.isdigit()):
        row = input("Enter row again: ")
        column = input("Enter column again: ")

    # Typecast the row and column values into int since the input command assigns values as str in variables.
    row = int(row)
    column = int(column)

    # Call the play_turn function to determine whether the row and column values obtained from the user are valid and to
    # store the updated board (only if move is valid).
    board, validity = play_turn(board, row, column)

    # If the requested turn is invalid the process is repeated until the game received a valid turn.
    while validity is False:
        row = input("Enter row again: ")
        column = input("Enter column again: ")

        while (not row.isdigit()) or (not column.isdigit()):
            row = input("Enter row again: ")
            column = input("Enter column again: ")

        row = int(row)
        column = int(column)

        board, validity = play_turn(board, row, column)

    # Check whether the draw or win is true by calling both functions.
    draw = check_draw(board)
    win, winner = check_win(board)

    # Display the updated board with the valid move on the screen.
    display_board(board)

    # Repeatedly take turns until either the game is won or ends in a draw (copy and paste the code from above).
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

    # Final result and final board is displayed. If the final result is a win, also display the winning player.
    if draw is True:
        print("Game is a Draw :(")
        display_board(board)
    else:
        print("Winner is " + winner + "!")
        display_board(board)

    print("----THE END----")
    return None
