

class Graphe:
    def __init__(self, nom):
        self.nom = nom
        self.noeuds = {}

    def ajout_noeud(self, nom_noeud):
        if nom_noeud not in self.noeuds:
            self.noeuds[nom_noeud] = Noeud(nom_noeud)

    def ajout_liaison(self, noeud1, noeud2):
        
        if noeud1 not in self.noeuds:
            self.ajout_noeud(noeud1)
        if noeud2 not in self.noeuds:
            self.ajout_noeud(noeud2)
        
        self.noeuds[noeud1].ajout_voisin(noeud2)
        self.noeuds[noeud2].ajout_voisin(noeud1)

    def afficher_graphe(self):
        print(f"Graphe : {self.nom}")
        for noeud in self.noeuds.values():
            print(noeud)

class Noeud:
    def __init__(self, nom):
        self.nom = nom
        self.voisins = []

    def ajout_voisin(self, voisin):
        if voisin not in self.voisins:
            self.voisins.append(voisin)

    def __repr__(self):
        return f"{self.nom}, voisins : {self.voisins}"

# Création d'un objet Graphe
g1 = Graphe("g1")

liaisons = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for liaison in liaisons:
    noeud1, noeud2 = liaison[0], liaison[1]
    g1.ajout_liaison(noeud1, noeud2)

g1.afficher_graphe()
