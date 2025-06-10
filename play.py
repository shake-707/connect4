import pygame
import settings

from button import Button
from board import Board


class Play:

    def __init__(self, c4game):
        self.screen = c4game.screen
        self.settings = c4game.settings
        self.board = Board(self)
        self.screen_rect = self.screen.get_rect()
        self.back_button = Button(self.settings, image=None, pos=(40, 20), text_input='BACK',
                                  font=pygame.font.SysFont('Arial', 30), base_color='#d7fcd4', hovering_color='White')
        self.game_start = False
        self.turn = 1

    # drawing the play screen
    def draw_screen(self, game_board):
        self.board.draw_board(self.settings.get_row_size(), self.settings.get_column_size(), self.settings.get_square_size(), self.settings.get_board_color(), game_board)
        mouse_position = pygame.mouse.get_pos()
        self.back_button.changeColor(mouse_position)
        self.back_button.update(self.screen)
