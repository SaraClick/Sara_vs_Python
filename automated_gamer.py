# Identify risk combinations: 2 lined "S" in the same row/col/diagonal

idx_board = [[[0, 0], [0, 1], [0, 2]],
             [[1, 0], [1, 1], [1, 2]],
             [[2, 0], [2, 1], [2, 2]]]

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


def win_combinations(game_board, idx_board):
    """Given a board with possible pay positions and idx_board with the location indexes for row,col, returns
    dictionary with number of winner combinations as key and a list [winner combination, winner index locations] as
    values"""
    combinations = {}
    count = 1
    # ROWS CHECK
    for row in range(3):
        combinations[count] = [game_board[row], idx_board[row]]
        count += 1

    # ROW CHECK
    col = 0
    while col <= 2:
        column = []
        column_idx = []
        for row in range(3):
            column.append(game_board[row][col])
            column_idx.append([row, col])
        combinations[count] = [column, column_idx]
        col += 1
        count += 1

    # DIAGONAL CHECKS
    combinations[count] = [[game_board[0][0], game_board[1][1], game_board[2][2]],
                           [idx_board[0][0], idx_board[1][1], idx_board[2][2]]]
    count += 1
    combinations[count] = [[game_board[0][2], game_board[1][1], game_board[2][0]],
                           [idx_board[0][2], idx_board[1][1], idx_board[2][0]]]

    return combinations



# If risk combination is identified, move into the risk box to avoid "S" win
# If no risk combination is identified, check if "P" has any potential winning combinations
# If "P" has a potential winning combination, use "P" turn to move into that box
# Identify possible box that could in the future allow "P" to win
# If any possible box, move "P" there
# Else, random move to any empty cell
