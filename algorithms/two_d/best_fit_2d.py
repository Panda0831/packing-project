import os
import sys

# Ajouter le dossier racine du projet au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from models.two_d.bin_2d import Bin2D


def best_fit_2d(rectangles, bin_largeur, bin_hauteur):
    # Tri manuel par aire décroissante
    rects = list(rectangles)
    n = len(rects)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (rects[j].largeur * rects[j].hauteur) < (
                rects[j + 1].largeur * rects[j + 1].hauteur
            ):
                rects[j], rects[j + 1] = rects[j + 1], rects[j]

    bin = Bin2D(bin_largeur, bin_hauteur)

    # Liste des espaces libres: (x, y, largeur, hauteur)
    espaces_libres = [(0, 0, bin_largeur, bin_hauteur)]

    for r in rects:
        meilleur_espace = None
        index_espace = -1
        min_reste = float("inf")

        # Chercher le meilleur espace (celui qui gaspille le moins)
        for i, (ex, ey, ew, eh) in enumerate(espaces_libres):
            if r.largeur <= ew and r.hauteur <= eh:
                reste = (ew * eh) - (r.largeur * r.hauteur)
                if reste < min_reste:
                    min_reste = reste
                    meilleur_espace = (ex, ey, ew, eh)
                    index_espace = i

        if meilleur_espace:
            ex, ey, ew, eh = meilleur_espace
            # Placer le rectangle
            bin.ajouter_rectangle(r, ex, ey)

            # Supprimer l'espace utilisé et ajouter les deux nouveaux espaces libres
            espaces_libres.pop(index_espace)

            # Espace restant à droite du rectangle
            if ew > r.largeur:
                espaces_libres.append((ex + r.largeur, ey, ew - r.largeur, r.hauteur))
            # Espace restant en dessous du rectangle
            if eh > r.hauteur:
                espaces_libres.append((ex, ey + r.hauteur, ew, eh - r.hauteur))
        else:
            print(f"Rectangle {r.id} non placé (pas d'espace).")

    return bin
