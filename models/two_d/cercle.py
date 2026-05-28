class Cercle:
    def __init__(self, id, rayon):
        self.id = id
        self.rayon = rayon
        # Un cercle occupe un carré de côté (2 * rayon) pour le placement
        self.largeur = rayon * 2
        self.hauteur = rayon * 2
        self.x = 0
        self.y = 0
        self.pivote = False # La rotation d'un cercle ne change pas ses dimensions au sol

    def pivoter(self):
        # Faire pivoter un cercle parfait n'a pas d'impact sur son encombrement
        pass

    def __repr__(self):
        return f"Cercle(id={self.id}, R={self.rayon} à {self.x},{self.y})"
