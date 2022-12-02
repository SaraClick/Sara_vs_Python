import pygame

player = "S"

# Array to track board position
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# Array to track the graphical board where for each cell we have [Image, Center position]
graph_board = [[[None, None], [None, None], [None, None]],
               [[None, None], [None, None], [None, None]],
               [[None, None], [None, None], [None, None]]]


# Define images for game
sara = pygame.image.load("files/sara.png")
python = pygame.image.load("files/python.png")
sara_win = pygame.image.load("files/sara_win.png")
python_win = pygame.image.load("files/python_win.png")


# Define screen, grid and caption
size = width, height = 600, 600
grid_width = 4
color_background = (239, 246, 191)
color_board = (0, 0, 0)
pygame.display.set_caption("Sara vs Python!")


# Display empty grid board
screen = pygame.display.set_mode(size)
screen.fill(color_background)


def grid_generator(screen_max=width, box_size=round((width/3))):
    """Given a board, generates a grid to have a board with 3x3 boxes"""
    for i in range(0, screen_max, box_size):
        pygame.draw.line(screen, color_board, (0, i), (screen_max, i), grid_width)  # screen, color, start, end, width
        pygame.draw.line(screen, color_board, (i, 0), (i, screen_max), grid_width)  # screen, color, start, end, width


# Rendering board function
def render_board(game_board, game_g_board):
    """Given position of mouse click within the board returns the [row][col] equivalent index within board"""
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == "S":
                # REFERENCE: graph_board[row][col][0] is the image, graph_board[row][col][1] is the center of the box
                game_g_board[i][j][0] = sara
                game_g_board[i][j][1] = sara.get_rect(center=(j*200+100, i*200+100))
                # center = center within the square cell
                # 600/3/2 = 100 for i=1 j=1 // 300 for i=1 j=1 // 500 for i=2 j=2
            elif game_board[i][j] == "P":
                game_g_board[i][j][0] = python
                game_g_board[i][j][1] = python.get_rect(center=(j*200+100, i*200+100))
                # center = center within the square cell
                # 600/3/2 = 100 for i=1 j=1 // 300 for i=1 j=1 // 500 for i=2 j=2


def convert_pos_to_idx(position):  # position is a tuple (x,y) obtained with pygame.mouse.get_pos()
    """Given position of mouse click within the board returns the [row][col] equivalent index within board"""
    # NOTE: X corresponds to the column value and Y to the row value
    # convert mouse position tuple onto indexes of board 0-5 for rows and cols
    ratio = 0.005  # max X value for row[1] = 200. Then:  200 * ratio = 1 /// row[0] = 199
    row_idx = int(position[1] * ratio)  # converts position X onto row index
    col_idx = int(position[0] * ratio)  # converts position Y onto col index
    return row_idx, col_idx


# Create mouse input
def add_movement(game_board, game_g_board, game_player):
    """Given a user click, assigns the box selection to the player, renders updated board and returns board & player"""
    mouse_position = pygame.mouse.get_pos()
    row, col = convert_pos_to_idx(mouse_position)
    if game_board[row][col] != "S" and game_board[row][col] != "P":
        game_board[row][col] = game_player
        if game_player == "S":
            game_player = "P"
        else:
            game_player = "S"

    render_board(game_board, game_g_board)  # updates the movement to the graph_board

    # Display the sara/python images on top of the board
    for i in range(3):
        for j in range(3):
            if game_g_board[i][j][0] is not None:
                screen.blit(game_g_board[i][j][0], game_g_board[i][j][1])

    return game_board, game_player


def check_winner(game_board):
    """Given a board array of [row][cols], checks for 3 of the same input to return winner, if no winner returns None"""

    if game_board[0][0] == game_board[1][1] == game_board[2][2]:
        winner = game_board[1][1]
        winner_idx = [[0, 0], [1, 1], [2, 2]]
        return winner, winner_idx
    if game_board[0][2] == game_board[1][1] == game_board[2][0]:
        winner = game_board[1][1]
        winner_idx = [[0, 2], [1, 1], [2, 0]]
        return winner, winner_idx

    row = 0
    col = 0
    # Checks rows
    while row < len(game_board):
        if game_board[row][0] == game_board[row][1] == game_board[row][2]:
            winner = game_board[row][0]
            winner_idx = [[row, 0], [row, 1], [row, 2]]
            return winner, winner_idx
        else:
            row += 1

    # Checks columns
    while col < len(game_board):
        if game_board[0][col] == game_board[1][col] == game_board[2][col]:
            winner = game_board[0][col]
            winner_idx = [[0, col], [1, col], [2, col]]
            return winner, winner_idx
        else:
            col += 1


def replace_winner_img(winner, winner_indexes, game_g_board):
    """Given a winner and the idx where winner combination is located, replaces the image on these locations"""
    img_winner = sara_win
    if winner == "P":
        img_winner = python_win

    for idx in winner_indexes:
        game_g_board[idx[0]][idx[1]][0] = img_winner

    # Display the updated images on the board
    for i in range(3):
        for j in range(3):
            if game_g_board[i][j][0] is not None:
                screen.blit(game_g_board[i][j][0], game_g_board[i][j][1])


def draw(game_board):
    """Given a board array of game plays, returns True if there are no more moves and no winner, otherwise False"""
    is_draw = True

    if check_winner(game_board):
        is_draw = False

    else:
        for row in range(len(game_board)):
            for col in range(len(game_board)):
                item = str(game_board[row][col])
                if item.isdigit():
                    is_draw = False

    return is_draw
