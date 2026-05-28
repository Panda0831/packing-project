import os
import sys
import time

# Ajouter le dossier racine du projet au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms.two_d.brute_force_2d import brute_force_2d
from models.two_d.rectangle import Rectangle


def tester_brute_force_10_rects():
    # 10 rectangles de test
    rects = [
        Rectangle(id=f"R{i}", largeur=i % 3 + 1, hauteur=i % 2 + 1) for i in range(10)
    ]

    # Bac 10x10
    W, H = 10, 10

    print(f"Bac: {W}x{H}")
    print(f"Nombre de rectangles: {len(rects)}")

    start_time = time.time()

    # Exécution Brute Force
    resultat = brute_force_2d(rects, W, H)

    end_time = time.time()

    # Affichage
    print(f"\nTemps d'exécution : {end_time - start_time:.2f} secondes")
    print(f"Résultat : {resultat}")


if __name__ == "__main__":
    tester_brute_force_10_rects()
