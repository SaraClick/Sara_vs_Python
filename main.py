import asyncio
import pygame
import sys
import asyncio


from utils import board, graph_board, grid_generator, color_background, screen, add_movement, player, check_winner, \
    replace_winner_img, draw, first_move


pygame.init()


def _reset_boards():
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


def end_game_check(game_finished, game_board, game_g_board, game_player):
    """Given if game is finished, game boards and player, returns player and True if game has a winner or is drawn"""

    if check_winner(game_board):
        winner, winner_idx = check_winner(game_board)
        replace_winner_img(winner, winner_idx, game_g_board)
        pygame.display.update()
        pygame.time.delay(600)
        # The below if statement ensures that the loser will always have the fist move in the next game
        if winner == "S":
            game_player = "P"
        else:
            game_player = "S"
        game_finished = True

    if draw(game_board):
        pygame.display.update()
        pygame.time.delay(600)
        game_finished = True

    return game_finished, game_player


async def main(game_board, game_g_board, game_player):

    game_finished = False

    while True:
        await asyncio.sleep(0)
        grid_generator()
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_player == "S":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_board, game_player = add_movement(game_board, game_g_board, game_player)

            else:  # if game_player == "P":
                if not first_move(game_board):
                    pygame.time.delay(600)
                game_board, game_player = add_movement(game_board, game_g_board, game_player)

            game_finished, game_player = end_game_check(game_finished, game_board, game_g_board, game_player)

            if game_finished:
                new_board, new_g_board = _reset_boards()
                await main(new_board, new_g_board, game_player)

            game_finished, game_player = end_game_check(game_finished, game_board, game_g_board, game_player)


            if game_finished:
                pygame.time.delay(600)
                new_board, new_g_board = _reset_boards()
                await main(new_board, new_g_board, game_player)

            pygame.display.update()
            await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main(board, graph_board, player))
