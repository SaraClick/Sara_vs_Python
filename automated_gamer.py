# Identify risk combinations: 2 lined "S" in the same row/col/diagonal

def win_combinations(game_board):
    combinations = []

    # ROWS CHECK
    for row in game_board:
        combinations.append(row)

    # COLUMNS CHECK
    col = 0
    column = []
    while col <= 2:
        while len(column) < 3:
            for row in range(3):
                column.append(game_board[row][col])
            combinations.append(column)
        column = []
        col += 1

    # DIAGONAL CHECKS
    combinations.append([game_board[0][0], game_board[1][1], game_board[2][2]])
    combinations.append([game_board[0][2], game_board[1][1], game_board[2][0]])

    return combinations




# If risk combination is identified, move into the risk box to avoid "S" win
# If no risk combination is identified, check if "P" has any potential winning combinations
# If "P" has a potential winning combination, use "P" turn to move into that box
# Identify possible box that could in the future allow "P" to win
# If any possible box, move "P" there
# Else, random move to any empty cell
