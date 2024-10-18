## Courbe du Dragon : Implémentations récursive et graphique 

### Introduction

La courbe du dragon est une fractale célèbre pour sa structure complexe et auto-similaire. Ce projet présente deux implémentations de cet algorithme en Python, offrant une comparaison entre une approche récursive classique et une approche plus structurée utilisant des graphes.

### Objectifs

* **Comprendre la récursivité :** Illustrer l'utilisation de la récursivité pour résoudre des problèmes géométriques.
* **Explorer les structures de données :** Démontrer l'intérêt des graphes pour représenter des objets fractals.
* **Comparer les performances :** Évaluer les avantages et les inconvénients de chaque approche en termes de temps d'exécution et d'utilisation de la mémoire.
* **Visualiser les résultats :** Créer des représentations graphiques de la courbe du dragon pour différentes itérations.

### Visualisations de l'algorithme

![alt text](ressources/approche_naive.gif)

### Implémentations

#### Version récursive

* **Principe :** L'algorithme se divise en deux appels récursifs à lui-même, chacun représentant une moitié de la courbe.
* **Avantages :** Simplicité du code et facilité de compréhension.
* **Inconvénients :** Potentiel de dépassement de pile pour de grandes valeurs d'itération et inefficacité pour les calculs intermédiaires.

Pour suivre le chemin suivant : `./implementations/approche_naive`

**Fichier : dragon_curve.py**
```python
import turtle

class NaiveDragonCurve:
    def __init__(self, depth, length, angle):
        """
        Args:
            depth (int): La profondeur de la courbe.
            length (float): La longueur de chaque segment.
            angle (float): L'angle entre les segments.
        """
        self.depth = depth
        self.length = length
        self.angle = angle

    def draw(self, n=None, sign=1):
        """
        Args:
            n (int, optional): Le niveau de profondeur actuel. Si None, commence avec la profondeur initiale.
            sign (int, optional): La direction du tournant (1 pour à gauche, -1 pour à droite).
        """
        if n is None:
            n = self.depth  # Commencer avec la profondeur initiale

        if n == 0:
            # Cas de base : dessiner une ligne
            turtle.forward(self.length)
        else:
            # Cas récursif : dessiner la moitié gauche puis la moitié droite
            self.draw(n - 1, 1)  # Dessiner la moitié gauche avec un tournant à gauche
            turtle.left(self.angle * sign)
            self.draw(n - 1, -1)  # Dessiner la moitié droite avec un tournant à droite
```

**Fichier : turtle_setup.py**
```python
import turtle

def setup_turtle():
    turtle.Screen().clear()  # Efface l'écran
    turtle.speed(0)  # Définit la vitesse de la tortue au maximum (0)
    turtle.pensize(1)  # Définit la taille du stylo à 1 pixel
    turtle.bgcolor("white")  # Définit la couleur de fond à blanc
    turtle.title("Courbe du dragon")  # Définit le titre de la fenêtre à "Courbe du dragon"
```

Pour suivre le chemin suivant : `./visualisations/visualisation_approche_naive.py`

```python
import turtle
from implementations.approche_naive.dragon_curve import NaiveDragonCurve
from implementations.approche_naive.turtle_setup import setup_turtle

def visualisation_approche_naive():
    setup_turtle()  # Configure l'environnement de la tortue

    naive_dragon_curve = NaiveDragonCurve(14, 5, 90)  # Crée une courbe du dragon avec une profondeur de 14, longueur de 5, et angle de 90 degrés
    turtle.penup()  # Lève le stylo pour éviter de dessiner
    turtle.goto(100, 200)  # Déplace la tortue à la position de départ
    turtle.pendown()  # Abaisse le stylo pour commencer à dessiner
    naive_dragon_curve.draw()  # Dessine la courbe du dragon

    turtle.done()  # Garde la fenêtre de la tortue ouverte jusqu'à ce qu'elle soit fermée
```

**Comment l'appeler ?** Allez dans le fichier `main` puis exécutez-le. Une fois dans le menu, sélectionnez 1.

#### Version graphique

* **Structure de données :** Un graphe est utilisé pour représenter la courbe, chaque nœud correspondant à un segment.
* **Algorithme :** Un parcours en profondeur du graphe permet de construire la courbe itérativement.
* **Avantages :** Meilleure gestion de la mémoire, possibilité d'ajouter des fonctionnalités avancées (animations, couleurs).
* **Inconvénients :** Complexité accrue de l'implémentation.

Pour suivre le chemin suivant : `./implementations/approche_optimise`

**Fichier : dragon_curve.py**
```python
import matplotlib.pyplot as plt
import numpy as np
from .graph import Graph

class DragonCurveGraph(Graph):  # Hérite de la classe Graph
    def generate_dragon_curve(self, iterations):
        directions = [0]  # Commence vers la droite

        for _ in range(iterations):
            new_directions = [(d + 1) % 4 for d in reversed(directions)]
            directions = directions + [1] + new_directions 
        return directions

    def draw_dragon_curve(self, iterations):  # Ajoutez 'self' ici
        # Génère la séquence de directions pour la courbe du dragon
        directions = self.generate_dragon_curve(iterations)  # Ajoutez 'self' ici

        # Définit les mouvements possibles (droite, haut, gauche, bas)
        moves = np.array([(1, 0), (0, 1), (-1, 0), (0, -1)])

        # Initialise le point de départ et des listes vides pour les coordonnées
        current_point = np.array([0, 0])
        x, y = [current_point[0]], [current_point[1]]  # Utilise des listes pour stocker les coordonnées

        # Configure le tracé
        plt.figure(figsize=(10, 10))
        plt.axis('equal')
        plt.title("Courbe du Dragon")

        # Itère sur les directions
        for i, d in enumerate(directions):
            # Calcule le mouvement en fonction de la direction actuelle
            dx, dy = moves[d]
            next_point = current_point + np.array([dx, dy])

            # Met à jour dynamiquement les coordonnées en utilisant des listes
            x.append(next_point[0])  # Ajoute à la liste au lieu d'utiliser np.append
            y.append(next_point[1])  # Ajoute à la liste au lieu d'utiliser np.append

            # Calcule une couleur basée sur l'indice d'itération pour la visualisation
            color = (i / len(directions), 0, 1 - (i / len(directions)))

            # Trace le segment de ligne et fait une pause pour un bref effet d'animation
            plt.plot(x[-2:], y[-2:], color=color, lw=0.7)
            plt.pause(0.01)

            # Met à jour le point actuel pour la prochaine itération
            current_point = next_point

        # Affiche le tracé final
        plt.show()
```

**Fichier : graph.py**
```python
class Graph:
    def __init__(self):
        # Initialise un dictionnaire pour stocker les arêtes (connexions) entre les points (nœuds)
        self.graph = {}

    def add_edge(self, point1, point2):
        # Ajoute une arête entre deux points dans le graphe
        if point1 not in self.graph:
            self.graph[point1] = []
        if point2 not in self.graph:
            self.graph[point2] = []
        self.graph[point1].append(point2)
        self.graph[point2].append(point1)
```

Pour suivre le chemin suivant : `./visualisations/visualisation_approche_optimise.py`

```python
from implementations.approche_optimise.dragon_curve import DragonCurveGraph

def visualisation_approche_optimise():
    # Crée une instance de DragonCurveGraph
    dragon_curve_graph = DragonCurveGraph()

    # Dessine la courbe du dragon avec un nombre spécifique d'itérations
    iterations = 25 
    dragon_curve_graph.draw_dragon_curve(iterations)
```

**Comment l'appeler ?** Allez dans le fichier `main`, puis exécutez-le. Une fois dans le menu, sélectionnez 2.

### Analyse

* **Complexité algorithmique :**
    * **Récursive :** Analyse de la complexité en temps et en espace.
    * **Graphique :** Analyse de la complexité en fonction de la structure du graphe.
* **Optimisations possibles :**
    * **Mémoïsation :** Pour réduire le nombre de calculs redondants dans la version récursive.
    * **Structures de données optimisées :** Pour améliorer les performances de la version graphique.

### Conclusion

Les deux implémentations présentent des avantages et des inconvénients. Le choix de l'une ou l'autre dépendra des contraintes du projet et des

 fonctionnalités souhaitées. La version récursive est plus simple à mettre en œuvre mais peut être limitée en termes de performance. La version graphique offre plus de flexibilité mais nécessite une conception plus élaborée.

### Perspectives

* **Généralisations :** Étendre l'algorithme à d'autres courbes fractales.
* **Applications :** Explorer les applications de la courbe du dragon dans d'autres domaines (art, science des matériaux, etc.).
* **Optimisations parallèles :** Implémenter des versions parallèles des algorithmes pour tirer parti des architectures multi-cœurs.

### Installation et utilisation

* **Prérequis :** Python et les bibliothèques utilisées (Numpy, Matplotlib, Turtle, etc.).
* **Installation :** Installer les dépendances avec pip install -r requirements.txt.