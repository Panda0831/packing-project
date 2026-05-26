from packing_project.models.bin import Bin


def best_fit(items, capacite):
    bins = []
    for item in items:
        meilleur_bin = None
        espace_minimum = capacite + 1

        for bin in bins:
            if bin.peut_contenir(item):
                espace_restant = bin.capacite - (bin.charge_actuelle + item)
                if espace_restant < espace_minimum:
                    espace_minimum = espace_restant
                    meilleur_bin = bin

        if meilleur_bin:
            meilleur_bin.ajouter_item(item)
        else:
            new_bin = Bin(capacite)
            new_bin.ajouter_item(item)
            bins.append(new_bin)
    return bins


if __name__ == "__main__":
    items = [0.5, 0.7, 0.3, 0.9, 0.4, 0.6]
    capacite = 1.0

    resultat = best_fit(items, capacite)
    print(f"Bacs utilisés (Best Fit): {len(resultat)}")
    for i, b in enumerate(resultat):
        print(f"  Bac {i + 1}: {b}")
