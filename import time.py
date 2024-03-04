import time
import random
import os

def generate_random_char():
    # Génère un caractère aléatoire (lettres, chiffres et symboles)
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+"
    return random.choice(chars)

def create_matrix_effect(num_rows, num_cols, speed):
    matrix = [[" " for _ in range(num_cols)] for _ in range(num_rows)]

    while True:
        # Décale les lignes vers le bas
        for row in range(num_rows - 1, 0, -1):
            matrix[row] = matrix[row - 1][:]

        # Ajoute de nouveaux caractères aléatoires à la première ligne
        matrix[0] = [generate_random_char() for _ in range(num_cols)]

        # Efface l'écran (pour Windows)
        os.system("cls" if os.name == "nt" else "clear")

        # Affiche la matrice
        for row in matrix:
            print("".join(row))
        time.sleep(speed / 1000.0)

if __name__ == "__main__":
    num_rows = 30
    num_cols = 50
    speed = 100  # Ajustez la vitesse (en millisecondes)

    create_matrix_effect(num_rows, num_cols, speed)
