import pygame
import sys
from utils import board, graph_board, grid_generator, color_background, screen, add_movement, player, check_winner, \
    replace_winner_img, draw


pygame.init()


def reset():
    """Resets the game afresh for a new start"""
    reset_board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    reset_graph_board = [[[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]]]

    screen.fill(color_background)
    pygame.display.update()
    grid_generator()
    pygame.display.update()

    return reset_board, reset_graph_board


def run(game_board, game_g_board, game_player):

    game_finished = False

    while True:
        grid_generator()
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                game_board, game_player = add_movement(game_board, game_g_board, game_player)

                if game_finished:  # set the game back to blanks
                    new_board, new_g_board = reset()
                    run(new_board, new_g_board, game_player)

                if check_winner(game_board):
                    winner, winner_idx = check_winner(game_board)
                    replace_winner_img(winner, winner_idx, game_g_board)
                    game_finished = True

                if draw(game_board):
                    game_finished = True

                pygame.display.update()


run(board, graph_board, player)
