import sys
import os

# Ajouter le dossier racine du projet au chemin de recherche de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.best_fit import best_fit
from algorithms.first_fit import first_fit
from algorithms.worst_fit import worst_fit
from models.two_d.rectangle import Rectangle
from models.two_d.triangle import TriangleIsocele
from algorithms.two_d.nfdh import nfdh
from algorithms.two_d.ffdh import ffdh
from algorithms.two_d.best_fit_2d import best_fit_2d
from algorithms.two_d.brute_force_rotation import brute_force_rotation_2d


def tester_contre_exemple_1d(nom, items, capacite, opt):
    algos = {"FF": first_fit, "BF": best_fit, "WF": worst_fit}

    resultat = algos[nom](items, capacite)
    nb_bacs = len(resultat)

    print(f"Test 1D {nom} - Items: {items}, Capacité: {capacite}")
    print(f"  Résultat: {nb_bacs} bacs | Optimal attendu: {opt}")
    if nb_bacs > opt:
        print(f"   ✅ SUCCÈS : Contre-exemple trouvé pour {nom} !")
    else:
        print(f"  ❌ ÉCHEC : {nom} a trouvé l'optimum.")
    print("-" * 20)


def tester_contre_exemple_2d(nom, rects, W, H, opt):
    algos = {"NFDH": nfdh, "FFDH": ffdh, "BF2D": best_fit_2d}

    resultat = algos[nom](rects, W, H)
    nb_places = len(resultat.rectangles_places)

    print(f"Test 2D {nom} - Bac: {W}x{H}, Rectangles: {len(rects)}")
    print(f"  Placés: {nb_places} | Optimal possible: {opt}")
    if nb_places < opt:
        print(f"   ✅ SUCCÈS : Contre-exemple trouvé pour {nom} !")
    else:
        print(f"  ❌ ÉCHEC : {nom} a trouvé l'optimum.")
    print("-" * 20)


if __name__ == "__main__":
    print("=== CONTRE-EXEMPLES 1D ===")
    
    # 1. First Fit (FF)
    tester_contre_exemple_1d("FF", [0.2, 0.5, 0.4, 0.7, 0.1, 0.3, 0.8], 1.0, 3)

    # 2. Best Fit (BF)
    tester_contre_exemple_1d("BF", [0.4, 0.4, 0.6, 0.6], 1.0, 2)

    # 3. Worst Fit (WF)
    tester_contre_exemple_1d("WF", [0.4, 0.4, 0.4, 0.4, 0.6, 0.6], 1.0, 3)

    print("\n=== CONTRE-EXEMPLES 2D ===")
    
    # 1. NFDH
    rects_nfdh = [
        Rectangle(id="N1", largeur=6, hauteur=5),
        Rectangle(id="N2", largeur=6, hauteur=5),
        Rectangle(id="N3", largeur=4, hauteur=5),
        Rectangle(id="N4", largeur=4, hauteur=5)
    ]
    tester_contre_exemple_2d("NFDH", rects_nfdh, 10, 10, 4)

    # 2. FFDH
    rects_ffdh = [Rectangle(id="F1", largeur=1, hauteur=10)] + \
                 [Rectangle(id=f"F{i}", largeur=9, hauteur=1) for i in range(2, 12)]
    tester_contre_exemple_2d("FFDH", rects_ffdh, 10, 10, 11)

    # 3. Best Fit 2D
    rects_bf2d = [
        Rectangle(id="B1", largeur=6, hauteur=7),
        Rectangle(id="B2", largeur=4, hauteur=10)
    ]
    tester_contre_exemple_2d("BF2D", rects_bf2d, 10, 10, 2)

    print("\n=== CONTRE-EXEMPLE AVEC ROTATION ===")
    # 4. Rotation (NFDH vs BF Rotation)
    t1 = TriangleIsocele(id="ROT_T1", base=5, hauteur_triangle=10)
    r1 = Rectangle(id="ROT_R1", largeur=10, hauteur=2)
    r2 = Rectangle(id="ROT_R2", largeur=10, hauteur=2)
    formes_rot = [t1, r1, r2]
    
    # Test NFDH
    res_nfdh = nfdh(formes_rot, 10, 10)
    print(f"NFDH (Sans rotation) - Placés: {len(res_nfdh.rectangles_places)}/3")
    
    # Test BF Rotation (On reset les x, y, pivote)
    for f in formes_rot:
        f.x, f.y = 0, 0
        if getattr(f, 'pivote', False): f.pivoter()
    
    res_bf_rot, _ = brute_force_rotation_2d(formes_rot, 10, 10)
    print(f"BF Rotation (Avec rotation) - Placés: {len(res_bf_rot.rectangles_places)}/3")
    
    if len(res_bf_rot.rectangles_places) > len(res_nfdh.rectangles_places):
        print("   ✅ SUCCÈS : Rotation a permis une solution optimale !")
    else:
        print("  ❌ ÉCHEC : La rotation n'a pas fait de différence.")
