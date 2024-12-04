import tkinter as tk
import numpy as np

# Couleurs
WHITE = "white"
GRAY = "gray"
RED = "red"
GREEN = "green"
BLACK = "black"

# Formats
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARDS_ROWS = 3
BOARDS_COLUMNS = 3
SQUARE_SIZE = WIDTH // BOARDS_COLUMNS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

# Tableau graphique
board = np.zeros((BOARDS_ROWS, BOARDS_COLUMNS))

# Création de la fenêtre principale
root = tk.Tk()
root.title("TIC TAC TOE")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BLACK)
canvas.pack()

def draw_lines():
    for i in range(1, BOARDS_ROWS):
        canvas.create_line(0, SQUARE_SIZE * i, WIDTH, SQUARE_SIZE * i, fill=WHITE, width=LINE_WIDTH)
        canvas.create_line(SQUARE_SIZE * i, 0, SQUARE_SIZE * i, HEIGHT, fill=WHITE, width=LINE_WIDTH)

def draw_figures():
    for row in range(BOARDS_ROWS):
        for col in range(BOARDS_COLUMNS):
            if board[row][col] == 1:
                canvas.create_oval(col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4,
                                   col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4,
                                   outline=WHITE, width=CIRCLE_WIDTH)
            elif board[row][col] == 2:
                canvas.create_line(col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4,
                                   col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4,
                                   fill=WHITE, width=CROSS_WIDTH)
                canvas.create_line(col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4,
                                   col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4,
                                   fill=WHITE, width=CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    return not any(board[row][col] == 0 for row in range(BOARDS_ROWS) for col in range(BOARDS_COLUMNS))

def check_win(player):
    for col in range(BOARDS_COLUMNS):
        if all(board[row][col] == player for row in range(BOARDS_ROWS)):
            return True
    for row in range(BOARDS_ROWS):
        if all(board[row][col] == player for col in range(BOARDS_COLUMNS)):
            return True
    return board[0][0] == player == board[1][1] == board[2][2] or board[0][2] == player == board[1][1] == board[2][0]

def minimax(minimax_board, depth, is_maximizing):
    if check_win(2):
        return float("inf")
    elif check_win(1):
        return float('-inf')
    elif is_board_full():
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
    canvas.delete("all")
    draw_lines()
    global game_over, player
    game_over = False
    player = 1
    board.fill(0)

def click(event):
    global player, game_over
    if game_over:
        return
    mouseX, mouseY = event.x // SQUARE_SIZE, event.y // SQUARE_SIZE
    if available_square(mouseY, mouseX):
        mark_square(mouseY, mouseX, player)
        draw_figures()
        if check_win(player):
            game_over = True
        player = player % 2 + 1
        if not game_over:
            if best_move():
                draw_figures()
                if check_win(2):
                    game_over = True
                player = player % 2 + 1
        if not game_over and is_board_full():
            game_over = True

def key(event):
    if event.char == 'r':
        restart_game()

canvas.bind("<Button-1>", click)
root.bind("<Key>", key)

draw_lines()
player, game_over = 1, False

root.mainloop()