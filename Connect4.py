import random
import sys
import pygame
import numpy as np
import math

import settings
from settings import Settings
from button import Button
from play import Play
from board import Board
from aicomputer import AIcomputer


class Connect4:
    def __init__(self):
        pygame.init()
        self.myfont = pygame.font.SysFont("monospace", 75)
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.get_screen_width(), self.settings.get_screen_Height()))
        self.screen.fill(self.settings.get_back_ground_color())
        pygame.display.set_caption("Connect4")
        self.ply = Play(self)
        self.board = Board(self)
        self.ai = AIcomputer(self)
        self.play_button = Button(self.settings, image=None, pos=((self.settings.get_screen_width() / 2), 200),
                                  text_input="PLAY BUTTON",
                                  font=pygame.font.SysFont('Arial', 30), base_color='#d7fcd4', hovering_color='White')
        self.options_button = Button(self.settings, image=None, pos=(self.settings.get_screen_width() / 2, 400),
                                     text_input='OPTIONS',
                                     font=pygame.font.SysFont('Arial', 30), base_color='#d7fcd4',
                                     hovering_color='White')
        self.quit_button = Button(self.settings, image=None, pos=(self.settings.get_screen_width() / 2, 600),
                                  text_input='QUIT',
                                  font=pygame.font.SysFont('Arial', 30), base_color='#d7fcd4', hovering_color='White')

        self.one_player_button = Button(self.settings, image=None,
                                        pos=(self.settings.get_screen_width() / 2 - 100, 400),
                                        text_input='ONE PLAYER',
                                        font=pygame.font.SysFont('Arial', 30), base_color='#d7fcd4',
                                        hovering_color="White")

        self.two_players_button = Button(self.settings, image=None,
                                         pos=(self.settings.get_screen_width() / 2 + 100, 400),
                                         text_input='TWO PLAYERS',
                                         font=pygame.font.SysFont('Arial', 30), base_color='#d7fcd4',
                                         hovering_color="White")

    def run_game(self):
        while True:
            mouse_position = pygame.mouse.get_pos()

            # filling start screen with play, option and quits buttons
            if self.settings.get_num_player():
                self.one_player_button.clickedButtonColor()
                self.two_players_button.defaultButtonColor()
            else:
                self.one_player_button.defaultButtonColor()
                self.two_players_button.clickedButtonColor()

            if not self.settings.play_screen:
                for butt in [self.play_button, self.one_player_button, self.two_players_button, self.quit_button]:
                    butt.changeColor(mouse_position)
                    butt.update(self.screen)
            else:
                self.ply.back_button.changeColor(mouse_position)
                self.ply.back_button.update(self.screen)
            self.check_events()
            if self.settings.play_screen:
                self.check_wins()
                if self.settings.get_num_player() and self.ply.turn == 0:
                    self.ai_computer()
                self.check_wins()

            pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:

                # drawing rect over previous hovering piece
                pygame.draw.rect(self.screen, settings.BLACK,
                                 (0, settings.BACk_BUTTON_SIZE, self.settings.screen_width, settings.SQUARE_SIZE))
                pos_x = event.pos[0]
                if self.settings.play_screen:
                    # creating hovering pieces if p1(RED) = turn 1 p2(YELLOW) = turn 0
                    if self.ply.turn == 1:
                        pygame.draw.circle(self.screen, settings.RED,
                                           (pos_x, int(settings.BACk_BUTTON_SIZE + settings.SQUARE_SIZE / 2)),
                                           settings.CIRCLE_RADIUS)
                    else:
                        pygame.draw.circle(self.screen, settings.YELLOW,
                                           (pos_x, int(settings.BACk_BUTTON_SIZE + settings.SQUARE_SIZE / 2)),
                                           settings.CIRCLE_RADIUS)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # bools to check if buttons are clicked
                quit_button_clicked = self.quit_button.rect.collidepoint(mouse_pos)
                play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
                play_back_button_clicked = self.ply.back_button.rect.collidepoint(mouse_pos)
                one_player_clicked = self.one_player_button.rect.collidepoint(mouse_pos)
                two_players_clicked = self.two_players_button.rect.collidepoint(mouse_pos)

                if self.settings.play_screen:
                    pos_x, pos_y = event.pos
                    self.settings.column_input = pos_x

                    # getting what column to drop piece in from mouse click
                    col = int(math.floor(self.settings.column_input / settings.SQUARE_SIZE))
                    # player 1 turn
                    if self.ply.turn:
                        # check if the column the player want to drop is full if not full gets the next available row
                        if self.board.is_valid_location(self.board.game_board, col):
                            row = self.board.get_next_row(self.board.game_board, col)
                            self.board.drop_piece(self.board.game_board, col, row, 1)
                            # changing player turn
                            self.ply.turn = 0

                        print(np.flip(self.board.game_board, 0))

                    else:
                        if not self.settings.get_num_player():

                            if self.board.is_valid_location(self.board.game_board, col):
                                row = self.board.get_next_row(self.board.game_board, col)
                                self.board.drop_piece(self.board.game_board, col, row, 2)
                                # changing to player 2 turn
                                self.ply.turn = 1

                        print(np.flip(self.board.game_board, 0))

                    self.ply.draw_screen(self.board.game_board)  # updating screen
                    pygame.display.update()
                    # self.board.check_horizontal_win(self.board.game_board)
                    # self.board.check_vertical_win(self.board.game_board)
                    # self.board.check_Left_diagonal_win(self.board.game_board)
                    # self.board.check_Right_diagonal_win(self.board.game_board)

                    # checking if the win conditions have been met
                    # self.board.check_horizontal_win(self.board.game_board)
                    # self.board.check_vertical_win(self.board.game_board)
                    # self.board.check_Left_diagonal_win(self.board.game_board)
                    # self.board.check_Right_diagonal_win(self.board.game_board)
                    #
                    # # win conditions met print PLAYER Wins to screen
                    # if self.board.p1wins:
                    #     # draw black rect to cover the hovering piece, so it does not obstruct win screen
                    #     pygame.draw.rect(self.screen, settings.BLACK,
                    #                      (0, settings.BACk_BUTTON_SIZE, self.settings.screen_width,
                    #                       settings.SQUARE_SIZE))
                    #     label = self.myfont.render("Player 1 wins!", 1, settings.RED)
                    #     self.screen.blit(label, (40, 10))
                    #     pygame.display.update()
                    #     pygame.time.wait(1000)
                    #     pygame.quit()
                    #     sys.exit()
                    #
                    # if self.board.p2wins:
                    #     pygame.draw.rect(self.screen, settings.BLACK,
                    #                      (0, settings.BACk_BUTTON_SIZE, self.settings.screen_width,
                    #                       settings.SQUARE_SIZE))
                    #     label2 = self.myfont.render("Player 2 wins!", 1, settings.YELLOW)
                    #     self.screen.blit(label2, (40, 10))
                    #     pygame.display.update()
                    #     pygame.time.wait(1000)
                    #     pygame.quit()
                    #     sys.exit()

                # not in play screen check for play, quit and options button clicks
                if not self.settings.play_screen:
                    if quit_button_clicked:
                        pygame.quit()
                        sys.exit()
                    if play_button_clicked:
                        # setting up necessary variable for play
                        self.settings.play_screen = True
                        self.ply.game_start = True
                        self.board.p1wins = False
                        self.board.p2wins = False
                        self.board.game_board = self.board.create_board()
                        self.ply.draw_screen(self.board.game_board)
                    if one_player_clicked:
                        if self.settings.get_num_player():
                            break
                        else:
                            self.settings.change_num_players()

                    if two_players_clicked:
                        if self.settings.get_num_player():
                            self.settings.change_num_players()

                # if play back button clicked return to home screen
                if play_back_button_clicked:
                    self.ply.turn = 1
                    self.screen.fill("black")
                    self.settings.play_screen = False

    def ai_computer(self):
        pygame.time.wait(1000)
        col = self.ai.pick_best_move(2, self.board.game_board)
        if self.board.is_valid_location(self.board.game_board, col):
            row = self.board.get_next_row(self.board.game_board, col)

            self.board.drop_piece(self.board.game_board, col, row, 2)

            # changing to player 2 turn
        self.ply.draw_screen(self.board.game_board)
        pygame.display.update()
        self.ply.turn = 1
        print(np.flip(self.board.game_board, 0))

    def check_wins(self):
        self.board.check_horizontal_win(self.board.game_board)
        self.board.check_vertical_win(self.board.game_board)
        self.board.check_Left_diagonal_win(self.board.game_board)
        self.board.check_Right_diagonal_win(self.board.game_board)

        # win conditions met print PLAYER Wins to screen
        if self.board.p1wins:
            # draw black rect to cover the hovering piece, so it does not obstruct win screen
            pygame.draw.rect(self.screen, settings.BLACK,
                             (0, settings.BACk_BUTTON_SIZE, self.settings.screen_width,
                              settings.SQUARE_SIZE))
            label = self.myfont.render("Player 1 wins!", 1, settings.RED)
            self.screen.blit(label, (40, 10))
            pygame.display.update()
            pygame.time.wait(1000)
            pygame.quit()
            sys.exit()

        if self.board.p2wins:
            pygame.draw.rect(self.screen, settings.BLACK,
                             (0, settings.BACk_BUTTON_SIZE, self.settings.screen_width,
                              settings.SQUARE_SIZE))
            label2 = self.myfont.render("Player 2 wins!", 1, settings.YELLOW)
            self.screen.blit(label2, (40, 10))
            pygame.display.update()
            pygame.time.wait(1000)
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    c4 = Connect4()
    c4.run_game()
