import random
import math
import settings

WINDOW_COUNT = 4
EMPTY_SPACE = 0


class AIcomputer:
    def __init__(self, c4game):
        self.settings = c4game.settings
        self.board = c4game.board

    def score_position(self, piece, board):
        opp_piece = 1
        score = 0
        # scores horizontal
        center_column = self.settings.get_column_size()//2
        center_array = [int(i) for i in list(board[:, center_column])]
        center_piece = center_array.count(piece) * 6
        score += center_piece

        for row in range(self.settings.get_row_size()):
            row_array = [int(i) for i in list(board[row, :])]
            for column in range(self.settings.get_column_size() - 3):
                window = row_array[column:column + WINDOW_COUNT]
                score += self.eval_window(window, piece)

        # score vertical
        for column in range(self.settings.get_column_size()):
            col_array = [int(i) for i in list(board[:, column])]
            for row in range(self.settings.get_row_size() - 3):
                window = col_array[row:row + WINDOW_COUNT]
                score += self.eval_window(window, piece)

        # score upwards diagonal
        for row in range(self.settings.get_row_size() - 3):

            for column in range(self.settings.get_column_size() - 3):
                window = [board[row + i][column + i] for i in range(WINDOW_COUNT)]
                score += self.eval_window(window, piece)

        # score downwards diagonals
        for row in range(self.settings.get_row_size() - 3):

            for column in range(self.settings.get_column_size() - self.settings.get_win_condition(),
                                self.settings.get_column_size()):
                window = [board[row + i][column - i] for i in range(WINDOW_COUNT)]
                score += self.eval_window(window, piece)

        return score

    def pick_best_move(self, piece, board):

        valid_locations = self.board.get_valid_locations(board)
        best_score = -10000000000000000000000
        best_col = random.choice(valid_locations)

        for column in valid_locations:
            row = self.board.get_next_row(board, column)
            temp_board = board.copy()
            self.board.drop_piece(temp_board, column, row, piece)
            score = self.score_position(piece, temp_board)
            score += self.minimax(temp_board, settings.DEPTH_SEARCH, False)
            if score > best_score:
                best_score = score
                best_col = column

        return best_col

    def terminal_node(self, board):
        if self.board.get_valid_locations(board) == 0 or self.board.getp1wins() or self.board.getp2wins():
            return True

        return False

    def minimax(self, board, depth, minimaxplayer):
        valid_locations = self.board.get_valid_locations(board)
        terminal_node = self.terminal_node(board)
        if depth == 0 or terminal_node:
            if terminal_node:
                if self.board.p2wins():
                    return 1000000000000000
                elif self.board.p1wins():
                    return -1000000000000000
                else:
                    return 0
            else:
                return self.score_position(2, board)

        if minimaxplayer:
            score = -math.inf
            for column in valid_locations:
                row = self.board.get_next_row(board, column)
                temp_board = board.copy()
                self.board.drop_piece(temp_board, column, row, 2)
                score = max(score, self.minimax(temp_board, depth - 1, False))

            return score
        else:
            score = math.inf
            for column in valid_locations:
                row = self.board.get_next_row(board, column)
                temp_board = board.copy()
                self.board.drop_piece(temp_board, column, row, 1)
                score = min(score, self.minimax(temp_board, depth - 1, True))

            return score

    def eval_window(self, window, piece):
        opp_piece = 1
        score = 0
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY_SPACE) == 1:
            score += 30
        elif window.count(opp_piece) == 3 and window.count(EMPTY_SPACE) == 1:
            score -= 80

        return score
