import sys
import pygame
import numpy as np

pygame.init()

#Couleurs
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#Formats
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARDS_ROWS = 3
BOARDS_COLUMNS = 3
SQUARE_SIZE = WIDTH // BOARDS_COLUMNS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BLACK)

board = np.zeros((BOARDS_ROWS, BOARDS_COLUMNS))

def draw_lines(color=WHITE):
    for i in range(1, BOARDS_ROWS):
        pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i))
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, WIDTH))

def draw_figures(color=WHITE):
    for row in range(BOARDS_ROWS):
        for col in range(BOARDS_COLUMNS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), CROSS_WIDTH)
                pygame.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full(check_board=board):
    return not any(check_board[row][col] == 0 for row in range(BOARDS_ROWS) for col in range(BOARDS_COLUMNS))

def check_win(player, check_board=board):
    for col in range(BOARDS_COLUMNS):
        if all(check_board[row][col] == player for row in range(BOARDS_ROWS)):
            return True
    for row in range(BOARDS_ROWS):
        if all(check_board[row][col] == player for col in range(BOARDS_COLUMNS)):
            return True
    return check_board[0][0] == player == check_board[1][1] == check_board[2][2] or check_board[0][2] == player == check_board[1][1] == check_board[2][0]

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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // SQUARE_SIZE
            mouseY = event.pos[1] // SQUARE_SIZE

            if available_square(mouseY, mouseX):
                mark_square(mouseY, mouseX, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                if not game_over:
                    if best_move():
                        if check_win(2):
                            game_over = True
                        player = player % 2 + 1 
                
                if not game_over:
                    if is_board_full():
                        game_over = True 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_over = False 
                player = 1

    if not game_over:
        draw_figures()
    else:
        if check_win(1):
            draw_figures(color=GREEN)
            draw_lines(color=GREEN)
        elif check_win(2):
            draw_figures(color=RED)
            draw_lines(color=RED)
        else:
            draw_figures(color=GRAY)
            draw_lines(color=GRAY)

    pygame.display.update()

                    
                    
                    
    
    

                