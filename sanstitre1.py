# Création d'une grille de morpion (Tic-Tac-Toe) en Python

def game_board():
    return [["" for _ in range(3)] for _ in range(3)]
print

def print_game_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:  # Ne pas imprimer la ligne de séparation après la dernière ligne
            print("-" * 6)

# Initialiser et afficher la grille


# print(game_board())
def choose_symbol():
    while True:
        player1 = input("Joueur 1, choisissez votre symbole (X ou O) : ")
        if player1 in ["X", "O"]:
           if player1=='X':
               player2 ='O'
           else:
               player2='X'
           return player1, player2
        else:
            print("Choix invalide. Veuillez choisir X ou O.")
def check_winner(board, player):
    # Vérifie les lignes, colonnes et diagonales
    for row in board:
        # boucle qui parcour chaque ligne de la grille
        if all(cell == player for cell in row):
            # c'est boucle qui vas parcourir toutes les cels de la ligne qui vas verifier l'alignement grace a ALl
            return True
            # si cest le cas beh on a gagner
    for col in range(3):
        # parcourie les colone 
        if all(board[row][col] == player for row in range(3)):
            # parcourir les colone avec une boucle qui se repeter 
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False
def is_full(board):
    return all(cell != "" for row in board for cell in row)

def play_game():
    board = game_board()
    player1, player2 = choose_symbol()
    current_player = player1
    while True:
        print_game_board(board)
        try:
            row = int(input(f"Joueur {current_player}, entrez le numéro de la ligne (0, 1, 2) : "))
            col = int(input(f"Joueur {current_player}, entrez le numéro de la colonne (0, 1, 2) : "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Coordonnées invalides. Veuillez entrer des numéros entre 0 et 2.")
                continue
            if board[row][col] == "":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_game_board(board)
                    print(f"Félicitations, joueur {current_player} a gagné !")
                    break
                elif is_full(board):
                    print_game_board(board)
                    print("Match nul !")
                    break
                current_player = player2 if current_player == player1 else player1
            else:
                print("Cette case est déjà occupée. Essayez une autre.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer des numéros.")
print(play_game())