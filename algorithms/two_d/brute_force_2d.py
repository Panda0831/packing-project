import os
import sys

# Ajouter le dossier racine du projet au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from models.two_d.bin_2d import Bin2D

def generer_permutations(liste):
    """
    Génère TOUTES les permutations d'une liste de manière récursive,
    sans utiliser de librairie externe.
    """
    if len(liste) <= 1:
        yield liste
        return

    for i in range(len(liste)):
        # On prend l'élément à la position i comme premier
        premier = liste[i]
        # Le reste sans cet élément
        reste = liste[:i] + liste[i + 1 :]

        # On génère les permutations du reste
        for perm in generer_permutations(reste):
            yield [premier] + perm

def brute_force_2d(rectangles, bin_largeur, bin_hauteur):
    """
    Implémentation brute force pour le packing 2D sans utiliser itertools.
    Teste toutes les permutations de rectangles et utilise une heuristique 
    (First Fit) pour tenter de les placer.
    """
    meilleur_bin = None
    min_rectangles_non_places = float('inf')

    # Génération de toutes les permutations possibles manuellement
    for perm in generer_permutations(rectangles):
        bin = Bin2D(bin_largeur, bin_hauteur)
        
        espaces_libres = [(0, 0, bin_largeur, bin_hauteur)]
        non_places = 0
        
        for r in perm:
            place = False
            for i, (ex, ey, ew, eh) in enumerate(espaces_libres):
                if r.largeur <= ew and r.hauteur <= eh:
                    bin.ajouter_rectangle(r, ex, ey)
                    espaces_libres.pop(i)
                    if ew > r.largeur:
                        espaces_libres.append((ex + r.largeur, ey, ew - r.largeur, r.hauteur))
                    if eh > r.hauteur:
                        espaces_libres.append((ex, ey + r.hauteur, ew, eh - r.hauteur))
                    place = True
                    break
            if not place:
                non_places += 1
        
        if non_places < min_rectangles_non_places:
            min_rectangles_non_places = non_places
            meilleur_bin = bin
            
    return meilleur_bin
