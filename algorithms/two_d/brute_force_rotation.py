import os
import sys

# Ajouter le dossier racine du projet au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from models.two_d.bin_2d import Bin2D


def generer_permutations(liste):
    if len(liste) <= 1:
        yield liste
        return
    for i in range(len(liste)):
        premier = liste[i]
        reste = liste[:i] + liste[i + 1 :]
        for perm in generer_permutations(reste):
            yield [premier] + perm


def brute_force_rotation_2d(rectangles, bin_largeur, bin_hauteur):
    meilleur_bin = None
    min_non_places = float("inf")
    n = len(rectangles)
    combinaisons_testees = 0

    # On teste chaque permutation
    for perm in generer_permutations(rectangles):
        # Pour chaque permutation, on teste les 2^n combinaisons de rotations
        # On utilise un entier comme masque binaire pour les rotations
        for i in range(1 << n):
            combinaisons_testees += 1
            # Appliquer les rotations selon le masque i
            for j in range(n):
                doit_pivoter = (i >> j) & 1
                # Si l'état actuel (pivote) est différent de ce qu'on veut, on pivote
                if perm[j].pivote != bool(doit_pivoter):
                    perm[j].pivoter()

            # Tenter le placement (Heuristique de placement dans les coins/espaces)
            bin_test = Bin2D(bin_largeur, bin_hauteur)
            espaces_libres = [(0, 0, bin_largeur, bin_hauteur)]
            non_places = 0

            for r in perm:
                place = False
                for idx, (ex, ey, ew, eh) in enumerate(espaces_libres):
                    if r.largeur <= ew and r.hauteur <= eh:
                        bin_test.ajouter_rectangle(r, ex, ey)
                        espaces_libres.pop(idx)
                        # On divise l'espace restant en deux rectangles
                        if ew > r.largeur:
                            espaces_libres.append(
                                (ex + r.largeur, ey, ew - r.largeur, r.hauteur)
                            )
                        if eh > r.hauteur:
                            espaces_libres.append(
                                (ex, ey + r.hauteur, ew, eh - r.hauteur)
                            )
                        place = True
                        break
                if not place:
                    non_places += 1

            # On garde le meilleur résultat
            if non_places < min_non_places:
                min_non_places = non_places
                # On fait une copie profonde manuelle du bin et de ses rectangles placés
                # car ils partagent les mêmes objets Rectangle
                meilleur_bin = bin_test
                # Si on a tout placé, c'est une solution optimale (pour ce bin)
                if min_non_places == 0:
                    return meilleur_bin, combinaisons_testees

    return meilleur_bin, combinaisons_testees
