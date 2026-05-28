import os
import sys
import tkinter as tk
from tkinter import messagebox

# Ajout de la racine du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms.two_d.best_fit_2d import best_fit_2d
from algorithms.two_d.brute_force_2d import brute_force_2d
from algorithms.two_d.brute_force_rotation import brute_force_rotation_2d
from algorithms.two_d.ffdh import ffdh
from algorithms.two_d.nfdh import nfdh

from models.two_d.rectangle import Rectangle
from models.two_d.cercle import Cercle
from models.two_d.triangle import TriangleIsocele

class ApplicationPacking:
    def __init__(self, racine):
        self.racine = racine
        self.racine.title("Visualiseur de Packing 2D")
        self.racine.geometry("900x900")

        # Paramètres du Conteneur (Bin)
        cadre_parametres = tk.Frame(racine)
        cadre_parametres.pack(pady=10)
        tk.Label(cadre_parametres, text="Largeur Bac:").grid(row=0, column=0)
        self.entree_w = tk.Entry(cadre_parametres, width=5)
        self.entree_w.insert(0, "15")
        self.entree_w.grid(row=0, column=1)
        tk.Label(cadre_parametres, text="Hauteur Bac:").grid(row=0, column=2)
        self.entree_h = tk.Entry(cadre_parametres, width=5)
        self.entree_h.insert(0, "15")
        self.entree_h.grid(row=0, column=3)

        # Formulaire d'ajout de formes
        cadre_formes = tk.Frame(racine)
        cadre_formes.pack(pady=10)
        
        tk.Label(cadre_formes, text="Type:").grid(row=0, column=0)
        self.type_forme = tk.StringVar(racine)
        self.type_forme.set("Rectangle")
        self.menu_type = tk.OptionMenu(cadre_formes, self.type_forme, "Rectangle", "Cercle", "Triangle", command=self.maj_champs_saisie)
        self.menu_type.grid(row=0, column=1, padx=5)

        tk.Label(cadre_formes, text="ID:").grid(row=0, column=2)
        self.entree_id = tk.Entry(cadre_formes, width=5)
        self.entree_id.grid(row=0, column=3)
        
        self.label_param1 = tk.Label(cadre_formes, text="L:")
        self.label_param1.grid(row=0, column=4)
        self.entree_p1 = tk.Entry(cadre_formes, width=5)
        self.entree_p1.grid(row=0, column=5)
        
        self.label_param2 = tk.Label(cadre_formes, text="H:")
        self.label_param2.grid(row=0, column=6)
        self.entree_p2 = tk.Entry(cadre_formes, width=5)
        self.entree_p2.grid(row=0, column=7)

        self.btn_ajouter = tk.Button(cadre_formes, text="Ajouter", command=self.ajouter_forme)
        self.btn_ajouter.grid(row=0, column=8, padx=5)

        # Liste des formes ajoutées
        self.liste_visuelle = tk.Listbox(racine, width=50, height=5)
        self.liste_visuelle.pack(pady=5)

        # Boutons pour les algorithmes
        cadre_algos = tk.Frame(racine)
        cadre_algos.pack(pady=10)
        tk.Button(cadre_algos, text="NFDH", command=lambda: self.lancer_algo("nfdh")).pack(side=tk.LEFT, padx=5)
        tk.Button(cadre_algos, text="FFDH", command=lambda: self.lancer_algo("ffdh")).pack(side=tk.LEFT, padx=5)
        tk.Button(cadre_algos, text="Best Fit", command=lambda: self.lancer_algo("best_fit")).pack(side=tk.LEFT, padx=5)
        tk.Button(cadre_algos, text="Brute Force", command=lambda: self.lancer_algo("brute_force")).pack(side=tk.LEFT, padx=5)
        tk.Button(cadre_algos, text="BF Rotation", command=lambda: self.lancer_algo("bf_rot")).pack(side=tk.LEFT, padx=5)
        tk.Button(cadre_algos, text="Charger Test", command=self.charger_test).pack(side=tk.LEFT, padx=20)
        tk.Button(cadre_algos, text="Vider", command=self.vider_formes).pack(side=tk.LEFT, padx=5)

        # Zone de dessin (Canvas)
        self.canevas = tk.Canvas(racine, width=600, height=400, bg="white", highlightbackground="black")
        self.canevas.pack(pady=10)

        # Zone de Logs
        tk.Label(racine, text="Historique / Logs:").pack()
        self.zone_logs = tk.Text(racine, height=10, width=90)
        self.zone_logs.pack(pady=5)

        self.formes = [] # Liste d'objets (Rectangle, Cercle, TriangleIsocele)
        self.compteur_id = 1
        self.entree_id.insert(0, str(self.compteur_id))

    def maj_champs_saisie(self, *args):
        """Met à jour les labels en fonction de la forme choisie."""
        choix = self.type_forme.get()
        if choix == "Cercle":
            self.label_param1.config(text="Rayon:")
            self.label_param2.grid_remove()
            self.entree_p2.grid_remove()
        elif choix == "Triangle":
            self.label_param1.config(text="Base:")
            self.label_param2.config(text="Hauteur:")
            self.label_param2.grid()
            self.entree_p2.grid()
        else: # Rectangle
            self.label_param1.config(text="L:")
            self.label_param2.config(text="H:")
            self.label_param2.grid()
            self.entree_p2.grid()

    def log(self, message):
        self.zone_logs.insert(tk.END, message + "\n")
        self.zone_logs.see(tk.END)
        self.racine.update_idletasks()

    def ajouter_forme(self):
        fid = self.entree_id.get()
        p1 = self.entree_p1.get()
        p2 = self.entree_p2.get()
        choix = self.type_forme.get()

        try:
            if choix == "Rectangle":
                forme = Rectangle(fid, int(p1), int(p2))
                msg = f"Rectangle {fid}: {p1}x{p2}"
            elif choix == "Cercle":
                forme = Cercle(fid, int(p1))
                msg = f"Cercle {fid}: Rayon {p1}"
            elif choix == "Triangle":
                forme = TriangleIsocele(fid, int(p1), int(p2))
                msg = f"Triangle {fid}: Base {p1}, Haut {p2}"
            
            self.formes.append(forme)
            self.liste_visuelle.insert(tk.END, msg)
            
            # Incrément ID
            self.compteur_id += 1
            self.entree_id.delete(0, tk.END)
            self.entree_id.insert(0, str(self.compteur_id))
            self.entree_p1.delete(0, tk.END)
            self.entree_p2.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")

    def vider_formes(self):
        self.formes = []
        self.liste_visuelle.delete(0, tk.END)
        self.compteur_id = 1
        self.entree_id.delete(0, tk.END)
        self.entree_id.insert(0, str(self.compteur_id))
        self.log("Liste des formes vidée.")

    def charger_test(self):
        # Charge des rectangles par défaut pour le moment
        from utils.test_cases import get_test_set_simple
        self.vider_formes()
        max_id = 0
        for r in get_test_set_simple():
            rect = Rectangle(r.id, r.largeur, r.hauteur)
            self.formes.append(rect)
            self.liste_visuelle.insert(tk.END, f"Rect {r.id}: {r.largeur}x{r.hauteur}")
            try:
                nid = int(r.id)
                if nid > max_id: max_id = nid
            except: pass
        self.compteur_id = max_id + 1
        self.entree_id.delete(0, tk.END)
        self.entree_id.insert(0, str(self.compteur_id))
        self.log("Jeu de test chargé.")

    def lancer_algo(self, nom_algo):
        if not self.formes:
            messagebox.showwarning("Attention", "Ajoutez d'abord des formes !")
            return

        w = int(self.entree_w.get())
        h = int(self.entree_h.get())
        self.log(f"--- Lancement de {nom_algo.upper()} ---")

        combinaisons = None
        # On utilise une copie des objets car les algos modifient x, y, pivote
        # Pour les algos existants, ils s'attendent à des objets avec .largeur et .hauteur
        if nom_algo == "nfdh":
            resultat = nfdh(self.formes, w, h)
        elif nom_algo == "ffdh":
            resultat = ffdh(self.formes, w, h)
        elif nom_algo == "best_fit":
            resultat = best_fit_2d(self.formes, w, h)
        elif nom_algo == "bf_rot":
            resultat, combinaisons = brute_force_rotation_2d(self.formes, w, h)
        else:
            resultat = brute_force_2d(self.formes, w, h)

        if combinaisons is not None:
            self.log(f"Combinaisons testées : {combinaisons}")

        places = len(resultat.rectangles_places)
        self.log(f"Résultat : {places}/{len(self.formes)} formes placées.")
        
        for f in resultat.rectangles_places:
            rot = " [Pivoté]" if getattr(f, 'pivote', False) else ""
            self.log(f"  > ID {f.id} ({type(f).__name__}): ({f.x}, {f.y}){rot}")

        self.afficher_resultat(resultat)

    def afficher_resultat(self, bin_res):
        self.canevas.delete("all")
        echelle = 30
        
        # Dessiner le Bac
        w_bac = int(self.entree_w.get()) * echelle
        h_bac = int(self.entree_h.get()) * echelle
        self.canevas.create_rectangle(0, 0, w_bac, h_bac, outline="red", dash=(4, 4))

        for f in bin_res.rectangles_places:
            couleur = "orange" if getattr(f, 'pivote', False) else "lightblue"
            x1, y1 = f.x * echelle, f.y * echelle
            x2, y2 = (f.x + f.largeur) * echelle, (f.y + f.hauteur) * echelle
            
            if isinstance(f, Rectangle):
                self.canevas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")
            
            elif isinstance(f, Cercle):
                # Un cercle est dessiné dans sa boîte englobante
                self.canevas.create_oval(x1, y1, x2, y2, fill=couleur, outline="black")
            
            elif isinstance(f, TriangleIsocele):
                # Dessin du triangle selon sa rotation
                points = []
                if f.angle_rotation == 0: # Pointe en haut
                    points = [x1 + (f.largeur * echelle / 2), y1, x1, y2, x2, y2]
                elif f.angle_rotation == 90: # Pointe à droite
                    points = [x1, y1, x2, y1 + (f.hauteur * echelle / 2), x1, y2]
                elif f.angle_rotation == 180: # Pointe en bas
                    points = [x1, y1, x2, y1, x1 + (f.largeur * echelle / 2), y2]
                else: # 270 - Pointe à gauche
                    points = [x1 + f.largeur * echelle, y1, x1 + f.largeur * echelle, y2, x1, y1 + (f.hauteur * echelle / 2)]
                
                self.canevas.create_polygon(points, fill=couleur, outline="black")

            # Texte ID
            cx, cy = x1 + (f.largeur * echelle / 2), y1 + (f.hauteur * echelle / 2)
            self.canevas.create_text(cx, cy, text=str(f.id), font=("Arial", 10, "bold"))

            # Ajout d'une flèche indicatrice de rotation
            if getattr(f, 'pivote', False) or (isinstance(f, TriangleIsocele) and f.angle_rotation != 0):
                taille_fleche = 10
                if isinstance(f, TriangleIsocele):
                    # La flèche suit la pointe du triangle
                    if f.angle_rotation == 90: # Droite
                        self.canevas.create_line(cx-5, cy, cx+taille_fleche, cy, arrow=tk.LAST, fill="red", width=2)
                    elif f.angle_rotation == 180: # Bas
                        self.canevas.create_line(cx, cy-5, cx, cy+taille_fleche, arrow=tk.LAST, fill="red", width=2)
                    elif f.angle_rotation == 270: # Gauche
                        self.canevas.create_line(cx+5, cy, cx-taille_fleche, cy, arrow=tk.LAST, fill="red", width=2)
                
                elif isinstance(f, Rectangle) and f.pivote:
                    # Pour un rectangle pivoté, on indique le sens de la hauteur
                    if f.hauteur > f.largeur:
                        self.canevas.create_line(cx, cy-5, cx, cy+taille_fleche, arrow=tk.BOTH, fill="red", width=2)
                    else:
                        self.canevas.create_line(cx-5, cy, cx+taille_fleche, cy, arrow=tk.BOTH, fill="red", width=2)


if __name__ == "__main__":
    racine = tk.Tk()
    app = ApplicationPacking(racine)
    racine.mainloop()
