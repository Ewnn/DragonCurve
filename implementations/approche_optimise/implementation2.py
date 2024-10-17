import matplotlib.pyplot as plt
import time

class DragonCurveGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, point1, point2):
        if point1 not in self.graph:
            self.graph[point1] = []
        if point2 not in self.graph:
            self.graph[point2] = []
        self.graph[point1].append(point2)
        self.graph[point2].append(point1)

    def generate_dragon_curve(self, iterations, update_interval=100):
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        directions = [0]
        current_point = (0, 0)

        for i in range(iterations):
            mirrored = [(d + 1) % 4 for d in reversed(directions)]
            directions.extend([1] + mirrored)

        x, y = [0], [0]
        plt.figure(figsize=(10, 10))
        plt.axis('equal')
        plt.title("Courbe de Dragon en Direct avec Graphe")

        for i, d in enumerate(directions):
            dx, dy = moves[d]
            next_point = (current_point[0] + dx, current_point[1] + dy)
            self.add_edge(current_point, next_point)
            x.append(next_point[0])
            y.append(next_point[1])
            current_point = next_point
            
            # Mise à jour tous les `update_interval` segments
            if i % update_interval == 0:
                plt.plot(x[-update_interval:], y[-update_interval:], color='blue', lw=0.7)
                plt.pause(0.01)  # Pause rapide pour afficher le lot

        # Affichage final pour le reste des segments non affichés
        plt.plot(x, y, color='blue', lw=0.7)
        plt.show()

# Exemple d'utilisation
iterations = 25  # Peut être augmenté pour plus de détails
dragon_graph = DragonCurveGraph()
dragon_graph.generate_dragon_curve(iterations, update_interval=50)
