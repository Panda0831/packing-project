import sys
import os

# Ajouter le dossier racine du projet au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models.two_d.bin_2d import Bin2D

def ffdh(rectangles, bin_largeur, bin_hauteur):
    # 1. Tri manuel par hauteur décroissante
    rects = list(rectangles)
    n = len(rects)
    for i in range(n):
        for j in range(0, n - i - 1):
            if rects[j].hauteur < rects[j + 1].hauteur:
                rects[j], rects[j + 1] = rects[j + 1], rects[j]
    
    bin = Bin2D(bin_largeur, bin_hauteur)
    
    # Stocker les niveaux : chaque niveau est (y_base, hauteur_max, largeur_utilisee)
    niveaux = []
    
    for r in rects:
        place = False
        
        # Essayer de placer dans un niveau existant (First-Fit)
        for i in range(len(niveaux)):
            y_base, h_niveau, largeur_util = niveaux[i]
            
            # Vérifier si ça rentre dans la largeur restante du niveau
            if largeur_util + r.largeur <= bin_largeur:
                if bin.ajouter_rectangle(r, largeur_util, y_base):
                    niveaux[i] = (y_base, h_niveau, largeur_util + r.largeur)
                    place = True
                    break
        
        # Si pas placé, créer un nouveau niveau
        if not place:
            y_base = sum(niv[1] for niv in niveaux)
            if y_base + r.hauteur <= bin_hauteur and r.largeur <= bin_largeur:
                if bin.ajouter_rectangle(r, 0, y_base):
                    niveaux.append((y_base, r.hauteur, r.largeur))
                    place = True
        
        if not place:
            print(f"Le rectangle {r.id} ne peut pas être placé.")
            
    return bin
