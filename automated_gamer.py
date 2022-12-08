import itertools
import random
from itertools import chain
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


def movements_left(game_board):
    board_movements = []
    for item in game_board:
        board_movements.extend(item)
    for item in board_movements:
        if str(item).isdigit():
            return True
    else:
        return False


def _random_move_selector(game_board):
    """Given a board, return a random move list [row, col] indexes"""
    row_col = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    empty_idx = []
    for row in game_board:
        for item in row:
            if str(item).isdigit():
                empty_idx.append(item - 1)

    random_idx = random.choice(empty_idx)

    return row_col[random_idx]


def _selector_coordinates(combinations, combinations_idx):
    idx_row_col = []
    for i in range(3):
        if str(combinations[i]).isdigit():
            idx_row_col = i
    return combinations_idx[idx_row_col]


def automated_player(game_board, idx_board):
    # If a potential winner combination with 2 moves can let the payer win, move into that position
    if moves_aligned("P", 2, game_board, idx_board):
        comb, idx_comb = moves_aligned("P", 2, game_board, idx_board)
        return _selector_coordinates(comb, idx_comb)

    # If risk combination is identified, move into the risk box to avoid "S" win
    elif moves_aligned("S", 2, game_board, idx_board):
        comb, idx_comb = moves_aligned("S", 2, game_board, idx_board)
        return _selector_coordinates(comb, idx_comb)

    # If board is empty, select a box randomly
    elif not moves_aligned("S", 1, game_board, idx_board) and not moves_aligned("P", 1, game_board, idx_board):
        return _random_move_selector(game_board)

    # if we have at 1 move aligned on S and either 1 or none for P, random for python to either move into an
    # aligned position for Python or block the other player
    elif (not moves_aligned("P", 1, game_board, idx_board) and moves_aligned("S", 1, game_board, idx_board)) or \
            (moves_aligned("P", 1, game_board, idx_board) and moves_aligned("S", 1, game_board, idx_board)):
        # Detect the move to block S from winning
        sara_align = moves_aligned("S", 1, game_board, idx_board)
        sara_block = _selector_coordinates(sara_align[0], sara_align[1])
        # Select a random move without specific intention of blocking S
        random_move = _random_move_selector(game_board)

        # Chose randomly from blocking S or a random move
        possible_moves = [sara_block, random_move]
        return random.choice(possible_moves)

    # if we have 1 move aligned for Python and none for S, Python moves to get 2 aligned
    elif moves_aligned("P", 1, game_board, idx_board) and not moves_aligned("S", 1, game_board, idx_board):
        comb, idx_comb = moves_aligned("P", 1, game_board, idx_board)
        return _selector_coordinates(comb, idx_comb)

    else:
        return _random_move_selector(game_board)

