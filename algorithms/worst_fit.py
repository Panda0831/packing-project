import sys
import os

# Ajouter le dossier racine du projet au chemin de recherche de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.bin import Bin



def worst_fit(items, capacite):
    bins = []
    for item in items:
        pire_bin = None
        espace_maximum = -1

        for bin in bins:
            if bin.peut_contenir(item):
                espace_restant = bin.capacite - bin.charge_actuelle
                if espace_restant > espace_maximum:
                    espace_maximum = espace_restant
                    pire_bin = bin

        if pire_bin:
            pire_bin.ajouter_item(item)
        else:
            new_bin = Bin(capacite)
            new_bin.ajouter_item(item)
            bins.append(new_bin)
    return bins


if __name__ == "__main__":
    items = [0.5, 0.7, 0.3, 0.9, 0.4, 0.6]
    capacite = 1.0

    resultat = worst_fit(items, capacite)
    print(f"Bacs utilisés (Worst Fit): {len(resultat)}")
    for i, b in enumerate(resultat):
        print(f"  Bac {i + 1}: {b}")
