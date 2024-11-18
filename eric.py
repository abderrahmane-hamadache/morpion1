def minimax(minimax_board, depth, is_maximizing):
    if check_win(2, minimax_board):
        return float("inf")
    elif check_win(1, minimax_board):
        return float('-inf')
    elif is_board_full(minimax_board):
        return 0
    best_score = -1000 if is_maximizing else 1000
    for row in range(BOARDS_ROWS):
        for col in range(BOARDS_COLUMNS):
            if minimax_board[row][col] == 0:
                minimax_board[row][col] = 2 if is_maximizing else 1
                score = minimax(minimax_board, depth + 1, not is_maximizing)
                minimax_board[row][col] = 0
                best_score = max(score, best_score) if is_maximizing else min(score, best_score)
    return best_score

def best_move():
    best_score, move = -1000, (-1, -1)
    for row in range(BOARDS_ROWS):
        for col in range(BOARDS_COLUMNS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score, move = score, (row, col)
    if move != (-1, -1):
        mark_square(move[0], move[1], 2)
        return True
    return False

def restart_game():
    screen.fill(BLACK)
    draw_lines()
    global game_over, player
    game_over = False
    player = 1
    board.fill(0)

draw_lines()
player, game_over = 1, False