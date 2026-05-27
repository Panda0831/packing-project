import sys
import os

# Ajouter le dossier racine du projet au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.two_d.rectangle import Rectangle
from algorithms.two_d.brute_force_2d import brute_force_2d

def tester_brute_force_2d():
    print("=== Démarrage du test Brute Force 2D ===")
    
    # Rectangles de test
    rects = [
        Rectangle(id="R1", largeur=3, hauteur=2),
        Rectangle(id="R2", largeur=2, hauteur=4),
        Rectangle(id="R3", largeur=4, hauteur=2),
        Rectangle(id="R4", largeur=1, hauteur=1)
    ]

    # Bac 5x5
    W, H = 5, 5

    print(f"Bac: {W}x{H}")
    print(f"Rectangles: {rects}")
    
    # Exécution Brute Force
    resultat = brute_force_2d(rects, W, H)

    # Affichage
    print(f"\nRésultat : {resultat}")
    if resultat:
        for r in resultat.rectangles_places:
            print(f"  {r}")
    else:
        print("Aucun résultat retourné.")
    
    print("=== Fin du test ===")

if __name__ == "__main__":
    tester_brute_force_2d()
