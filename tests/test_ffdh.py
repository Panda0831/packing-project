import os
import sys

# Ajouter le dossier racine du projet au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms.two_d.ffdh import ffdh
from models.two_d.rectangle import Rectangle


def tester_ffdh():
    # Rectangles de test
    rects = [
        Rectangle(id="R1", largeur=4, hauteur=2),
        Rectangle(id="R2", largeur=2, hauteur=4),
        Rectangle(id="R3", largeur=4, hauteur=2),
        Rectangle(id="R4", largeur=1, hauteur=1),
    ]

    # Bac 5x5
    W, H = 5, 5

    print(f"Bac: {W}x{H}")
    print(f"Rectangles: {rects}")

    # Exécution FFDH
    resultat = ffdh(rects, W, H)

    # Affichage
    print(f"\nRésultat : {resultat}")
    for r in resultat.rectangles_places:
        print(f"  {r}")


if __name__ == "__main__":
    tester_ffdh()
