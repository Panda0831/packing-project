class Bin2D:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.rectangles_places = []

    def peut_placer(self, rectangle, x, y):
        # Vérifier les bords
        if x + rectangle.largeur > self.largeur or y + rectangle.hauteur > self.hauteur:
            return False
        
        # Vérifier les chevauchements
        for r in self.rectangles_places:
            if not (x + rectangle.largeur <= r.x or 
                    x >= r.x + r.largeur or 
                    y + rectangle.hauteur <= r.y or 
                    y >= r.y + r.hauteur):
                return False
        return True

    def ajouter_rectangle(self, rectangle, x, y):
        if self.peut_placer(rectangle, x, y):
            rectangle.x = x
            rectangle.y = y
            self.rectangles_places.append(rectangle)
            return True
        return False

    def __repr__(self):
        return f"Bin2D({self.largeur}x{self.hauteur}, rectangles={len(self.rectangles_places)})"
