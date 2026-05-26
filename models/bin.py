class Bin:
    def __init__(self, capacite):
        self.capacite = capacite
        self.items = []
        self.charge_actuelle = 0

    def peut_contenir(self, item):
        return self.charge_actuelle + item <= self.capacite

    def ajouter_item(self, item):
        if self.peut_contenir(item):
            self.items.append(item)
            self.charge_actuelle += item
            return True
        return False

    def __str__(self):
        return f"Items: {self.items} (Total: {self.charge_actuelle:.2f}/{self.capacite})"
