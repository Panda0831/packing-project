class TriangleIsocele:
    def __init__(self, id, base, hauteur_triangle):
        self.id = id
        self.base = base
        self.hauteur_triangle = hauteur_triangle
        
        # On utilise son rectangle englobant pour simplifier le placement
        self.largeur = base
        self.hauteur = hauteur_triangle
        
        self.x = 0
        self.y = 0
        self.angle_rotation = 0 # 0, 90, 180, 270 degrés
        self.pivote = False

    def pivoter(self):
        """Rotation de 90 degrés (pi/2 radians)."""
        self.angle_rotation = (self.angle_rotation + 90) % 360
        # On inverse largeur et hauteur pour le rectangle englobant
        self.largeur, self.hauteur = self.hauteur, self.largeur
        # On marque comme 'pivote' si l'angle n'est pas 0 pour l'affichage GUI
        self.pivote = (self.angle_rotation != 0)

    def __repr__(self):
        return f"Triangle(id={self.id}, B={self.base}, H={self.hauteur_triangle} à {self.x},{self.y}, angle={self.angle_rotation}°)"
