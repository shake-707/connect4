import pygame
import settings
import numpy as np


class Board:

    def __init__(self, c4game):
        self.settings = c4game.settings
        self.screen = c4game.screen
        self.game_board = self.create_board()
        self.p1wins = False
        self.p2wins = False

    # create 2d array to hold player1 and player 2 positions
    def create_board(self):
        board = np.zeros((self.settings.get_row_size(), self.settings.get_column_size()))
        return board

    # check if the column the player want to drop is full returning bool
    def is_valid_location(self, board, column):
        print(type(self.settings.get_row_size()))
        print(type(column))

        return board[self.settings.get_row_size() - 1][column] == 0

    def get_valid_locations(self, board):
        valid_locations = []
        for column in range(self.settings.get_column_size()):
            if self.is_valid_location(board, column):
                valid_locations.append(column)
        return valid_locations

    def getp1wins(self):
        return self.p1wins

    def getp2wins(self):
        return self.p2wins

    def p1wins(self):
        self.p1wins = True

    def p2wins(self):
        self.p2wins = True
    # placing piece on board
    def drop_piece(self, board, column, row, piece):

        board[row][column] = piece

    # getting first available row in a column
    def get_next_row(self, board, column):

        for row in range(self.settings.get_row_size()):
            if board[row][column] == 0:
                return row

    def check_horizontal_win(self, board):

        for i in range(self.settings.get_row_size()):
            for j in range((self.settings.get_column_size() - self.settings.get_win_condition()) + 1):
                if board[i][j] == 1 and board[i][j + 1] == 1 and board[i][j + 2] == 1 and board[i][j + 3] == 1:
                    print('player one wins')
                    self.p1wins = True
                if board[i][j] == 2 and board[i][j + 1] == 2 and board[i][j + 2] == 2 and board[i][j + 3] == 2:
                    print('player two wins')
                    self.p2wins = True

    def check_vertical_win(self, board):

        for i in range((settings.ROW_SIZE - settings.WIN_CON) + 1):
            for j in range(settings.COL_SIZE):
                if board[i][j] == 1 and board[i + 1][j] == 1 and board[i + 2][j] == 1 and board[i + 3][j] == 1:
                    print('player one wins')
                    self.p1wins = True
                if board[i][j] == 2 and board[i + 1][j] == 2 and board[i + 2][j] == 2 and board[i + 3][j] == 2:
                    print('player two wins')
                    self.p2wins = True

    def check_Right_diagonal_win(self, board):
        for i in range((settings.ROW_SIZE - settings.WIN_CON) + 1):
            for j in range((settings.COL_SIZE - settings.WIN_CON) + 1):
                if board[i][j] == 1 and board[i + 1][j + 1] == 1 and board[i + 2][j + 2] == 1 and board[i + 3][
                    j + 3] == 1:
                    print('player one wins')
                    self.p1wins = True
                if board[i][j] == 2 and board[i + 1][j + 1] == 2 and board[i + 2][j + 2] == 2 and board[i + 3][
                    j + 3] == 2:
                    print('player two wins')
                    self.p2wins = True

    def check_Left_diagonal_win(self, board):

        for i in range(self.settings.get_row_size() - self.settings.get_win_condition() + 1):
            for j in range(self.settings.get_column_size() - self.settings.get_win_condition(),
                           self.settings.get_column_size()):
                if board[i][j] == 1 and board[i + 1][j - 1] == 1 and board[i + 2][j - 2] == 1 and board[i + 3][
                    j - 3] == 1:
                    print('player one wins')
                    self.p1wins = True
                if board[i][j] == 2 and board[i + 1][j - 1] == 2 and board[i + 2][j - 2] == 2 and board[i + 3][
                    j - 3] == 2:
                    print('player two wins')
                    self.p2wins = True

    # drawing the board and pieces to the screen
    def draw_board(self, row_size, col_size, square_size, board_color, board):

        for c in range(col_size):
            for r in range(row_size):
                pygame.draw.rect(self.screen, board_color, (c * square_size,
                                                            r * square_size + square_size + self.settings.get_back_button_size(),
                                                            square_size, square_size))

                pygame.draw.circle(self.screen, settings.BLACK,
                                   (int(c * square_size + square_size / 2),
                                    int(r * square_size + square_size + settings.BACk_BUTTON_SIZE + square_size / 2)),
                                   self.settings.get_circle_radius())

        for c in range(col_size):
            for r in range(row_size):
                if board[r][c] == 1:
                    # height = settings.Settings.get_screen_Height()
                    height = self.settings.get_screen_Height()

                    pygame.draw.circle(self.screen, self.settings.get_P1_color(),
                                       (int(c * square_size + square_size / 2),
                                        (height + square_size + self.settings.get_back_button_size()) - int(
                                            (r * square_size) + square_size + self.settings.get_back_button_size() + (
                                                    square_size / 2))),
                                       self.settings.get_circle_radius())
                elif board[r][c] == 2:
                    # height = settings.Settings.get_screen_Height()
                    height = self.settings.get_screen_Height()
                    pygame.draw.circle(self.screen, self.settings.get_P2_color(),
                                       (int(c * square_size + square_size / 2),
                                        (height + square_size + settings.BACk_BUTTON_SIZE) - int(
                                            r * square_size + square_size + self.settings.get_back_button_size() + square_size / 2)),
                                       self.settings.get_circle_radius())
