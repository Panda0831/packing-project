import sys
import os

# Ajouter le dossier racine du projet au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models.two_d.bin_2d import Bin2D

def nfdh(rectangles, bin_largeur, bin_hauteur):
    # 1. Tri manuel par hauteur décroissante (tri à bulles)
    rects = list(rectangles)
    n = len(rects)
    for i in range(n):
        for j in range(0, n - i - 1):
            if rects[j].hauteur < rects[j + 1].hauteur:
                rects[j], rects[j + 1] = rects[j + 1], rects[j]
    
    bin = Bin2D(bin_largeur, bin_hauteur)
    
    x_courant = 0
    y_courant = 0
    hauteur_niveau = 0
    
    for r in rects:
        # Si le rectangle ne rentre pas en largeur dans le niveau actuel
        if x_courant + r.largeur > bin_largeur:
            # On passe au niveau supérieur
            y_courant += hauteur_niveau
            x_courant = 0
            hauteur_niveau = 0
            
        # Si le rectangle ne rentre pas en hauteur dans le bac
        if y_courant + r.hauteur > bin_hauteur:
            print(f"Le rectangle {r.id} ne peut pas être placé (bac plein).")
            continue
            
        # Placement
        if bin.ajouter_rectangle(r, x_courant, y_courant):
            x_courant += r.largeur
            hauteur_niveau = max(hauteur_niveau, r.hauteur)
        else:
            print(f"Erreur placement {r.id}")
            
    return bin
