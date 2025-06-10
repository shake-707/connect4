ROW_SIZE = 6
COL_SIZE = 7
SQUARE_SIZE = 100
BACk_BUTTON_SIZE = 50
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CIRCLE_RADIUS = int(SQUARE_SIZE / 2 - 5)
WIN_CON = 4
GREEN = (0, 255, 0)
DEPTH_SEARCH = 1

class Settings:

    def __init__(self):
        self.screen_width = SQUARE_SIZE * COL_SIZE
        self.screen_height = (ROW_SIZE + 1) * SQUARE_SIZE + BACk_BUTTON_SIZE

        self.bg_color = ("black")
        self.play_screen = False

        self.game_start = False
        self.column_input = 0
        self.p1_win_condition = False
        self.p2_win_condition = False
        self.one_player = True

    @staticmethod
    def get_screen_Height():
        return (ROW_SIZE + 1) * SQUARE_SIZE + BACk_BUTTON_SIZE

    def player1_wins(self):
        self.p1_win_condition = True

    def player2_wins(self):
        self.p2_win_condition = True

    @staticmethod
    def get_back_ground_color():
        return BLACK

    @staticmethod
    def get_row_size():
        return ROW_SIZE

    @staticmethod
    def get_column_size():
        return COL_SIZE

    @staticmethod
    def get_back_button_size():
        return BACk_BUTTON_SIZE

    @staticmethod
    def get_board_color():
        return BLUE

    @staticmethod
    def get_P1_color():
        return RED

    @staticmethod
    def get_P2_color():
        return YELLOW

    @staticmethod
    def get_empty_space_color():
        return BLACK

    @staticmethod
    def get_square_size():
        return SQUARE_SIZE

    @staticmethod
    def get_circle_radius():
        return CIRCLE_RADIUS

    @staticmethod
    def get_win_condition():
        return WIN_CON

    def get_screen_width(self):
        return self.screen_width

    def get_screen_height(self):
        return self.screen_height

    def in_play_screen(self):
        return self.play_screen

    # one player is default
    def get_num_player(self):
        return self.one_player

    def two_players(self):
        self.one_player = False

    def get_button_clicked_color(self):
        return GREEN

    def change_num_players(self):
        self.one_player = not self.one_player
