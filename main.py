from algorithms.first_fit import first_fit
from algorithms.best_fit import best_fit
from algorithms.worst_fit import worst_fit

def comparer_algorithmes(items, capacite):
    algos = {
        "First Fit": first_fit,
        "Best Fit": best_fit,
        "Worst Fit": worst_fit
    }

    print(f"--- Comparaison du Bin Packing 1D ---")
    print(f"Items: {items}")
    print(f"Capacité des bacs: {capacite}\n")

    for nom, algo in algos.items():
        resultat = algo(items, capacite)
        print(f"Algorithme: {nom}")
        print(f"  Nombre de bacs: {len(resultat)}")
        for i, b in enumerate(resultat):
            print(f"    Bac {i + 1}: {b}")
        print("-" * 30)

if __name__ == "__main__":
    # Jeu de test
    items_test = [0.5, 0.7, 0.3, 0.9, 0.4, 0.6, 0.2, 0.8]
    capacite_test = 1.0
    
    comparer_algorithmes(items_test, capacite_test)
