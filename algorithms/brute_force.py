import os
import sys

# Ajouter le dossier racine du projet au chemin de recherche de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.bin import Bin


def first_fit_permutation(items, capacite):
    bins = []
    for item in items:
        placee = False
        for bin in bins:
            if bin.peut_contenir(item):
                bin.ajouter_item(item)
                placee = True
                break
        if not placee:
            new_bin = Bin(capacite)
            new_bin.ajouter_item(item)
            bins.append(new_bin)
    return bins


def generer_permutations(liste):
    if len(liste) <= 1:
        yield liste
        return

    for i in range(len(liste)):
        # On prend l'élément à la position i comme premier
        premier = liste[i]
        # Le reste sans cet élément
        reste = liste[:i] + liste[i + 1 :]

        # On génère les permutations du reste
        for permutation in generer_permutations(reste):
            yield [premier] + permutation


def brute_force_1d(items, capacite):
    if not items:
        return {"nb_bacs": 0, "permutation": [], "solution": []}

    meilleur_nb_bacs = float("inf")
    meilleure_permutation = None
    meilleure_solution = None

    # Génère et teste chaque permutation manuellement
    for permutation in generer_permutations(items):
        solution = first_fit_permutation(permutation, capacite)
        nb_bacs = len(solution)

        if nb_bacs < meilleur_nb_bacs:
            meilleur_nb_bacs = nb_bacs
            meilleure_permutation = permutation
            meilleure_solution = solution

    return {
        "nb_bacs": meilleur_nb_bacs,
        "permutation": meilleure_permutation,
        "solution": meilleure_solution,
    }
