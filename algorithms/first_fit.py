import sys
import os

# Ajouter le dossier racine du projet au chemin de recherche de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.bin import Bin



def first_fit(items, capacite):
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


if __name__ == "__main__":
    items = [0.5, 0.7, 0.3, 0.9, 0.4, 0.6]
    capacite = 1.0

    resultat = first_fit(items, capacite)
    print(f"Bacs utilisés: {len(resultat)}")
    for i, b in enumerate(resultat):
        print(f"  Bac {i + 1}: {b}")
