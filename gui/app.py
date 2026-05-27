import tkinter as tk
import sys
import os

# Ajout de la racine du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import messagebox
from models.two_d.rectangle import Rectangle
from algorithms.two_d.nfdh import nfdh
from algorithms.two_d.best_fit_2d import best_fit_2d
from algorithms.two_d.brute_force_2d import brute_force_2d

class PackingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Packing 2D Visualizer")
        self.root.geometry("800x700")

        # Paramètres Bin
        frame_params = tk.Frame(root)
        frame_params.pack(pady=10)
        tk.Label(frame_params, text="Largeur Bin:").grid(row=0, column=0)
        self.entry_w = tk.Entry(frame_params, width=5)
        self.entry_w.insert(0, "10")
        self.entry_w.grid(row=0, column=1)
        tk.Label(frame_params, text="Hauteur Bin:").grid(row=0, column=2)
        self.entry_h = tk.Entry(frame_params, width=5)
        self.entry_h.insert(0, "10")
        self.entry_h.grid(row=0, column=3)

        # Formulaire Rectangles
        frame_rect = tk.Frame(root)
        frame_rect.pack(pady=10)
        tk.Label(frame_rect, text="ID:").grid(row=0, column=0)
        self.entry_id = tk.Entry(frame_rect, width=5)
        self.entry_id.grid(row=0, column=1)
        tk.Label(frame_rect, text="L:").grid(row=0, column=2)
        self.entry_rl = tk.Entry(frame_rect, width=5)
        self.entry_rl.grid(row=0, column=3)
        tk.Label(frame_rect, text="H:").grid(row=0, column=4)
        self.entry_rh = tk.Entry(frame_rect, width=5)
        self.entry_rh.grid(row=0, column=5)
        self.btn_add = tk.Button(frame_rect, text="Ajouter", command=self.ajouter_rectangle)
        self.btn_add.grid(row=0, column=6, padx=5)

        self.listbox = tk.Listbox(root, width=40, height=5)
        self.listbox.pack(pady=5)

        # Boutons Algorithmes
        frame_algo = tk.Frame(root)
        frame_algo.pack(pady=10)
        tk.Button(frame_algo, text="NFDH", command=lambda: self.run_algo("nfdh")).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_algo, text="Best Fit", command=lambda: self.run_algo("best_fit")).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_algo, text="Brute Force", command=lambda: self.run_algo("brute_force")).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_algo, text="Charger Test", command=self.charger_test).pack(side=tk.LEFT, padx=20)

        # Canvas
        self.canvas = tk.Canvas(root, width=500, height=400, bg="white", highlightbackground="black")
        self.canvas.pack(pady=10)

        self.rectangles = []

    def ajouter_rectangle(self):
        rid = self.entry_id.get()
        rw = self.entry_rl.get()
        rh = self.entry_rh.get()
        if rid and rw and rh:
            self.rectangles.append((rid, int(rw), int(rh)))
            self.listbox.insert(tk.END, f"{rid}: {rw}x{rh}")
            self.entry_id.delete(0, tk.END)
            self.entry_rl.delete(0, tk.END)
            self.entry_rh.delete(0, tk.END)

    def charger_test(self):
        from utils.test_cases import get_test_set_simple
        self.rectangles = []
        self.listbox.delete(0, tk.END)
        for r in get_test_set_simple():
            self.rectangles.append((r.id, r.largeur, r.hauteur))
            self.listbox.insert(tk.END, f"{r.id}: {r.largeur}x{r.hauteur}")

    def run_algo(self, algo_name):
        rect_objs = [Rectangle(r[0], r[1], r[2]) for r in self.rectangles]
        w, h = int(self.entry_w.get()), int(self.entry_h.get())
        
        if algo_name == "nfdh": resultat = nfdh(rect_objs, w, h)
        elif algo_name == "best_fit": resultat = best_fit_2d(rect_objs, w, h)
        else: resultat = brute_force_2d(rect_objs, w, h)
        
        self.afficher_resultat(resultat)

    def afficher_resultat(self, bin_res):
        self.canvas.delete("all")
        scale = 30
        for r in bin_res.rectangles_places:
            self.canvas.create_rectangle(r.x * scale, r.y * scale, (r.x + r.largeur) * scale, (r.y + r.hauteur) * scale, fill="lightblue", outline="black")
            self.canvas.create_text(r.x * scale + (r.largeur * scale / 2), r.y * scale + (r.hauteur * scale / 2), text=r.id)

if __name__ == "__main__":
    root = tk.Tk()
    app = PackingApp(root)
    root.mainloop()
