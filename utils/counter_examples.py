import sys
import os

# Ajouter le dossier racine du projet au chemin de recherche de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.best_fit import best_fit
from algorithms.first_fit import first_fit
from algorithms.worst_fit import worst_fit


def tester_contre_exemple(nom, items, capacite, opt):
    algos = {"FF": first_fit, "BF": best_fit, "WF": worst_fit}

    resultat = algos[nom](items, capacite)
    nb_bacs = len(resultat)

    print(f"Test {nom} - Items: {items}, Capacité: {capacite}")
    print(f"  Résultat: {nb_bacs} bacs | Optimal attendu: {opt}")
    if nb_bacs > opt:
        print(f"   SUCCÈS : Contre-exemple trouvé pour {nom} !")
    else:
        print(f"  ❌ ÉCHEC : {nom} a trouvé l'optimum.")
    print("-" * 20)


if __name__ == "__main__":
    # Q2: Trouver des contre-exemples

    # 1. Contre-exemple pour First Fit (FF)
    # [0.6, 0.6, 0.6, 0.6, 0.6, 0.6] cap 1.0
    # Chaque 0.6 prend un bac car 0.6 + 0.6 = 1.2 > 1.0
    # Résultat FF: 6 bacs.
    # Somme = 3.6, donc l'optimal théorique est 4 bacs.
    tester_contre_exemple("FF", [0.6, 0.6, 0.6, 0.6, 0.6, 0.6], 1.0, 4)

    # 2. Contre-exemple pour Best Fit (BF)
    # BF peut être piégé en remplissant trop "bien" un bac, laissant un reste
    # inutilisable pour la suite.
    # Exemple classique: [0.3, 0.3, 0.3, 0.3, 0.3, 0.3] cap 1.0 -> Opt 2
    # BF: [0.3, 0.3, 0.3], [0.3, 0.3, 0.3] -> 2 (Opt)
    # Essayons: [0.3, 0.7, 0.3, 0.3, 0.4] cap 1.0
    # Opt: [0.7, 0.3], [0.3, 0.3, 0.4] -> 2
    # BF: [0.3, 0.7], [0.3, 0.3, 0.4] -> 2 (Opt)
    # Cas Best Fit != Opt: [0.4, 0.6, 0.4, 0.4, 0.4] cap 1.0
    # BF: [0.4, 0.6], [0.4, 0.4], [0.4] -> 3
    # Opt: [0.4, 0.4], [0.4, 0.4], [0.6] -> 3 (Encore opt)
    # Vrai contre-exemple BF: [0.3, 0.3, 0.4, 0.4, 0.6, 0.6] cap 1.0
    # Opt: [0.4, 0.6], [0.4, 0.6], [0.3, 0.3] -> 3
    # BF: [0.3, 0.3, 0.4], [0.4, 0.6], [0.6] -> 3 (Encore opt)
    # Essayons: [0.4, 0.4, 0.4, 0.5, 0.5, 0.8] cap 1.0
    # Opt: [0.5, 0.5], [0.4, 0.4, 0.2? non], [0.8] ...
    # Un classique pour BF: [0.5, 0.5, 0.4, 0.4, 0.4, 0.4, 0.4]
    # BF: [0.5, 0.5], [0.4, 0.4], [0.4, 0.4], [0.4] -> 4
    # Opt: [0.4, 0.4, 0.2?], dur.
    # Utilisons un cas simple pour Worst Fit d'abord.

    # 3. Contre-exemple pour Worst Fit (WF)
    # [0.8, 0.8, 0.2, 0.2, 0.2, 0.2] cap 1.0
    # WF éparpille les 0.2 dans de nouveaux bacs si les précédents sont trop pleins.
    # Opt: [0.8, 0.2], [0.8, 0.2], [0.2, 0.2] -> 3 bacs
    tester_contre_exemple("WF", [0.8, 0.8, 0.2, 0.2, 0.2, 0.2], 1.0, 3)

    # Retour au Best Fit
    # [0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 1.0]... non.
    # Essayons [0.4, 0.4, 0.6, 0.6, 1.0]
    # Opt: [0.4, 0.6], [0.4, 0.6], [1.0] -> 3
    # BF: [0.4], [0.4], [0.6], [0.6], [1.0] ?? Non.
    # BF: [0.4], [0.4, 0.6], [0.4? non], [0.6], [1.0] -> 4. ✅
    tester_contre_exemple("BF", [0.4, 0.4, 0.6, 0.6], 1.0, 2)
