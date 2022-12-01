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
def render_board(main_board=None, s_img=sara, p_img=python):
    """Given position of mouse click within the board returns the [row][col] equivalent index within board"""
    if main_board is None:  # this is due to main_board being a mutable object
        main_board = board
    for i in range(3):
        for j in range(3):
            if main_board[i][j] == "S":
                # REFERENCE: graph_board[row][col][0] is the image, graph_board[row][col][1] is the center of the box
                graph_board[i][j][0] = s_img
                graph_board[i][j][1] = s_img.get_rect(center=(j*200+100, i*200+100))
                # center = center within the square cell
                # 600/3/2 = 100 for i=1 j=1 // 300 for i=1 j=1 // 500 for i=2 j=2
            elif main_board[i][j] == "P":
                graph_board[i][j][0] = p_img
                graph_board[i][j][1] = p_img.get_rect(center=(j*200+100, i*200+100))
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
def add_movement(main_board=None, g_board=None, turn=player):
    """Given a user click, assigns the box selection to the player, renders updated board and returns board & player"""
    if main_board is None:
        main_board = board
    if g_board is None:
        g_board = graph_board
    mouse_position = pygame.mouse.get_pos()
    row, col = convert_pos_to_idx(mouse_position)
    if main_board[row][col] != 'S' and main_board[row][col] != 'P':
        main_board[row][col] = turn
        if turn == 'S':
            turn = 'P'
        else:
            turn = 'S'

    render_board(main_board, sara, python)  # updates the movement to the graph_board

    # Display the sara/python images on top of the board
    for i in range(3):
        for j in range(3):
            if g_board[i][j][0] is not None:
                screen.blit(g_board[i][j][0], g_board[i][j][1])

    return board, turn


def check_winner(board_arr):
    """Given a board array of [row][cols], checks for 3 of the same input to return winner, if no winner returns None"""

    winner = None
    winner_idx = None

    if board_arr[0][0] == board_arr[1][1] == board_arr[2][2]:
        winner = board_arr[1][1]
        winner_idx = [[0, 0], [1, 1], [2, 2]]
        return winner, winner_idx
    if board_arr[0][2] == board_arr[1][1] == board_arr[2][0]:
        winner = board_arr[1][1]
        winner_idx = [[0, 2], [1, 1], [2, 0]]
        return winner, winner_idx

    row = 0
    col = 0
    # Checks rows
    while row < len(board_arr):
        if board_arr[row][0] == board_arr[row][1] == board_arr[row][2]:
            winner = board_arr[row][0]
            winner_idx = [[row, 0], [row, 1], [row, 2]]
            return winner, winner_idx
        else:
            row += 1

    # Checks columns
    while col < len(board_arr):
        if board_arr[0][col] == board_arr[1][col] == board_arr[2][col]:
            winner = board_arr[0][col]
            winner_idx = [[0, col], [1, col], [2, col]]
            return winner, winner_idx
        else:
            col += 1


