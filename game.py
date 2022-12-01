import pygame
import sys
from utils import board, graph_board, grid_generator, color_background, screen, add_movement, player, check_winner, \
    replace_winner_img


pygame.init()
game_finished = False


while True:
    grid_generator()
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            board, player = add_movement(board, graph_board, player)

            if game_finished:  # set the game back to blanks
                board = [[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]]

                graph_board = [[[None, None], [None, None], [None, None]],
                               [[None, None], [None, None], [None, None]],
                               [[None, None], [None, None], [None, None]]]

                turn = "S"
                game_finished = False

                screen.fill(color_background)
                pygame.display.update()
                grid_generator()
                pygame.display.update()

            if check_winner(board):
                winner, winner_idx = check_winner(board)
                replace_winner_img(winner, winner_idx)
                game_finished = True

            pygame.display.update()
