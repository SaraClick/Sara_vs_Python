import pygame
import sys
from utils import board, graph_board, grid_generator, sara, python, render_board, size, color_background, screen, \
    add_movement, player
from random import randint


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
