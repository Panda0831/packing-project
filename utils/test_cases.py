from models.two_d.rectangle import Rectangle

def get_test_set_simple():
    """Jeu de test simple : quelques rectangles qui tiennent dans un bac 10x10."""
    return [
        Rectangle(id="R1", largeur=3, hauteur=3),
        Rectangle(id="R2", largeur=4, hauteur=2),
        Rectangle(id="R3", largeur=2, hauteur=5),
        Rectangle(id="R4", largeur=3, hauteur=2)
    ]

def get_test_set_dense():
    """Jeu de test dense : rectangles remplissant presque tout le bac 10x10."""
    return [
        Rectangle(id="R1", largeur=5, hauteur=5),
        Rectangle(id="R2", largeur=5, hauteur=5),
        Rectangle(id="R3", largeur=5, hauteur=5),
        Rectangle(id="R4", largeur=5, hauteur=5)
    ]
