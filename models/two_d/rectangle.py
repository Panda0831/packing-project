class Rectangle:
    def __init__(self, id, largeur, hauteur):
        self.id = id
        self.largeur = largeur
        self.hauteur = hauteur
        self.pivote = False

        self.x = 0  # C'est la distance horizontale depuis le bord gauche.
        self.y = 0  # C'est la distance verticale depuis le bord haut.

    def pivoter(self):
        self.largeur, self.hauteur = self.hauteur, self.largeur
        self.pivote = not self.pivote

    def __repr__(self):
        status = " (Pivoté)" if self.pivote else ""
        return f"Rect(id={self.id}, {self.largeur}x{self.hauteur} at {self.x},{self.y}{status})"
