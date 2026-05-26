from models.two_d.rectangle import Rectangle
from algorithms.two_d.nfdh import nfdh

# Définition des rectangles
rects = [
    Rectangle(id="R1", largeur=3, hauteur=2),
    Rectangle(id="R2", largeur=2, hauteur=4),
    Rectangle(id="R3", largeur=4, hauteur=2),
    Rectangle(id="R4", largeur=1, hauteur=1)
]

# Paramètres du bac
W, H = 5, 5

print(f"Test NFDH : Rangement de {len(rects)} rectangles dans un bac {W}x{H}")
resultat = nfdh(rects, W, H)

print(f"\nRésultat : {resultat}")
for r in resultat.rectangles_places:
    print(f"  {r}")
