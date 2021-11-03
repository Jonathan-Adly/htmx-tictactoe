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
    # if check_winner(board):
    # status= "--- have won the game"
    # return and terminate here
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
