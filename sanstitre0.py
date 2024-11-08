# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:18:33 2024

@author: sedik
"""

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