import numpy as np

class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)

    def get_alpha_beta_move(self, board):
        _, move = self.alpha_beta(board, depth=3, alpha=-float('inf'), beta=float('inf'), maximizing_player=True)
        if move is None:
            move = np.random.choice(self.get_valid_moves(board))
        return move

    def alpha_beta(self, board, depth, alpha, beta, maximizing_player):
        valid_moves = self.get_valid_moves(board)
        is_terminal = self.is_terminal_node(board)

        if depth == 0 or is_terminal:
            return self.evaluation_function(board), None

        if maximizing_player:
            value = -float('inf')
            best_move = None
            for move in valid_moves:
                new_board = self.make_move(board, move, self.player_number)
                new_score, _ = self.alpha_beta(new_board, depth-1, alpha, beta, False)
                if new_score > value:
                    value = new_score
                    best_move = move
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value, best_move
        else:
            value = float('inf')
            best_move = None
            opponent = 2 if self.player_number == 1 else 1
            for move in valid_moves:
                new_board = self.make_move(board, move, opponent)
                new_score, _ = self.alpha_beta(new_board, depth-1, alpha, beta, True)
                if new_score < value:
                    value = new_score
                    best_move = move
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value, best_move

    def get_expectimax_move(self, board):
        _, move = self.expectimax(board, depth=3, maximizing_player=True)
        if move is None:
            move = np.random.choice(self.get_valid_moves(board))
        return move

    def expectimax(self, board, depth, maximizing_player):
        valid_moves = self.get_valid_moves(board)
        is_terminal = self.is_terminal_node(board)

        if depth == 0 or is_terminal:
            return self.evaluation_function(board), None

        if maximizing_player:
            value = -float('inf')
            best_move = None
            for move in valid_moves:
                new_board = self.make_move(board, move, self.player_number)
                new_score, _ = self.expectimax(new_board, depth-1, False)
                if new_score > value:
                    value = new_score
                    best_move = move
            return value, best_move
        else:
            value = 0
            opponent = 2 if self.player_number == 1 else 1
            probability = 1 / len(valid_moves)
            for move in valid_moves:
                new_board = self.make_move(board, move, opponent)
                new_score, _ = self.expectimax(new_board, depth-1, True)
                value += probability * new_score
            return value, None

    def evaluation_function(self, board):
        score = 0
        center_column = board[:, board.shape[1] // 2]
        center_count = np.count_nonzero(center_column == self.player_number)
        score += center_count * 10
        score += self.evaluate_windows(board, window_length=4, immediate_check=True)
        return score

    def evaluate_windows(self, board, window_length, immediate_check=False):
        score = 0
        for row in range(board.shape[0]):
            for col in range(board.shape[1] - window_length + 1):
                window = board[row, col:col + window_length]
                score += self.evaluate_window(window, immediate_check)
        for col in range(board.shape[1]):
            for row in range(board.shape[0] - window_length + 1):
                window = board[row:row + window_length, col]
                score += self.evaluate_window(window, immediate_check)
        for row in range(board.shape[0] - window_length + 1):
            for col in range(board.shape[1] - window_length + 1):
                window = [board[row + i, col + i] for i in range(window_length)]
                score += self.evaluate_window(window, immediate_check)
        for row in range(window_length - 1, board.shape[0]):
            for col in range(board.shape[1] - window_length + 1):
                window = [board[row - i, col + i] for i in range(window_length)]
                score += self.evaluate_window(window, immediate_check)
        return score

    def evaluate_window(self, window, immediate_check):
        score = 0
        if np.count_nonzero(window == self.player_number) == 4:
            score += 1000000
        elif np.count_nonzero(window == self.player_number) == 3 and np.count_nonzero(window == 0) == 1:
            score += 5000 if immediate_check else 1000
        elif np.count_nonzero(window == self.player_number) == 2 and np.count_nonzero(window == 0) == 2:
            score += 500 if immediate_check else 100

        opponent = 2 if self.player_number == 1 else 1
        if np.count_nonzero(window == opponent) == 4:
            score -= 1000000
        elif np.count_nonzero(window == opponent) == 3 and np.count_nonzero(window == 0) == 1:
            score -= 5500 if immediate_check else 1100
        elif np.count_nonzero(window == opponent) == 2 and np.count_nonzero(window == 0) == 2:
            score -= 750 if immediate_check else 150

        return score

    def get_valid_moves(self, board):
        return [col for col in range(board.shape[1]) if 0 in board[:, col]]

    def is_terminal_node(self, board):
        return len(self.get_valid_moves(board)) == 0 or self.check_winner(board, self.player_number) or self.check_winner(board, 2 if self.player_number == 1 else 1)

    def make_move(self, board, col, player):
        new_board = board.copy()
        for row in range(board.shape[0] - 1, -1, -1):
            if new_board[row, col] == 0:
                new_board[row, col] = player
                break
        return new_board

    def check_winner(self, board, player):
        for row in range(board.shape[0]):
            for col in range(board.shape[1] - 3):
                if all(board[row, col + i] == player for i in range(4)):
                    return True

        for col in range(board.shape[1]):
            for row in range(board.shape[0] - 3):
                if all(board[row + i, col] == player for i in range(4)):
                    return True

        for row in range(board.shape[0] - 3):
            for col in range(board.shape[1] - 3):
                if all(board[row + i, col + i] == player for i in range(4)):
                    return True

        for row in range(3, board.shape[0]):
            for col in range(board.shape[1] - 3):
                if all(board[row - i, col + i] == player for i in range(4)):
                    return True

        return False

class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'random'
        self.player_string = 'Player {}:random'.format(player_number)

    def get_move(self, board):
        valid_cols = [col for col in range(board.shape[1]) if 0 in board[:, col]]
        return np.random.choice(valid_cols)

class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'human'
        self.player_string = 'Player {}:human'.format(player_number)

    def get_move(self, board):
        valid_cols = [col for col in range(board.shape[1]) if 0 in board[:, col]]
        print(f"Valid columns: {valid_cols}")
        move = int(input('Enter your move (0-based index for column): '))
        while move not in valid_cols:
            print('Invalid move. Column full or out of range, choose from: {}'.format(valid_cols))
            move = int(input('Enter your move (0-based index for column): '))
        return move