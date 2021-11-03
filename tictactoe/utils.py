import numpy as np


def computer_move(user):
    board = user.board
    if user.player == "X":
        computer = 2  # computer symbol is O, which is 2
    else:
        computer = 1  # computer symbol is X, which is 1

    for index, row in enumerate(board):
        for idx, col in enumerate(row):
            if col == 0:
                user.board[index][idx] = computer
                user.save()
                return None
    # game is full
    return "game board is full"


def check_status(board):
    if check_winner(board) != 0:
        status = f"The {check_winner(board)} player have won the game"
        return status
    flat_list = []
    for row in board:
        for col in row:
            flat_list.append(col)

    if 1 in flat_list or 2 in flat_list:
        if 0 in flat_list:
            return "game in progress"
        else:
            return "game has no winner"

    else:
        return None


def check_rows(board):
    for row in board:
        if len(set(row)) == 1:
            if row[0] == 1:
                return "X"
            elif row[0] == 2:
                return "O"
            else:
                return row[0]
    return 0


def check_diagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        if board[0][0] == 1:
            return "X"
        elif board[0][0] == 2:
            return "O"
        else:
            return board[0][0]
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        if board[0][len(board) - 1] == 1:
            return "X"
        elif board[0][len(board) - 1] == 2:
            return "O"
        else:
            return board[0][len(board) - 1]
    return 0


def check_winner(board):
    # transposition to check rows, then columns
    for new_board in [board, np.transpose(board)]:
        result = check_rows(new_board)
        if result:
            return result
    return check_diagonals(board)
