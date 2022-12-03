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


def moves_aligned(player_to_check, num_moves, game_board, idx_board):
    """Given a player to check, num of moves for that player in a winning row, the current game board and idx board,
    returns the first combination and index locations that matches the player being checked and num of box already
    filled by that player where the remaining boxes are empty; otherwise returns False"""

    winner_lines = win_combinations(game_board, idx_board)

    for key, values in winner_lines.items():
        count = 0
        checks = 1
        count_empty = 0
        while count < num_moves and checks < len(winner_lines):
            for move in values[0]:
                if str(move).isdigit():
                    count_empty += 1
                else:
                    if move == player_to_check:
                        count += 1

                if count_empty != 3 and (3 - count - count_empty == 0) and count == num_moves:
                    return values[0], values[1]

            count = 0
            count_empty = 0
            checks += 1
    return False

# If risk combination is identified, move into the risk box to avoid "S" win
# If no risk combination is identified, check if "P" has any potential winning combinations
# If "P" has a potential winning combination, use "P" turn to move into that box
# Identify possible box that could in the future allow "P" to win
# If any possible box, move "P" there
# Else, random move to any empty cell
