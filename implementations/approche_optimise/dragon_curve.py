import matplotlib.pyplot as plt
import numpy as np
from .graph import Graph

class DragonCurveGraph(Graph):  # Inherit from the Graph class
    def generate_dragon_curve(self, iterations):
        directions = [0]  # Start at the right

        for _ in range(iterations):
            new_directions = [(d + 1) % 4 for d in reversed(directions)]
            directions = directions + [1] + new_directions 
        return directions

    def draw_dragon_curve(self, iterations):  # Ajoutez 'self' ici
        # Generate the sequence of directions for the dragon curve
        directions = self.generate_dragon_curve(iterations)  # Ajoutez 'self' ici

        # Define the possible moves (right, up, left, down)
        moves = np.array([(1, 0), (0, 1), (-1, 0), (0, -1)])

        # Initialize the starting point and empty lists for coordinates
        current_point = np.array([0, 0])
        x, y = [current_point[0]], [current_point[1]]  # Utilisez des listes pour stocker les coordonnées

        # Set up the plot
        plt.figure(figsize=(10, 10))
        plt.axis('equal')
        plt.title("Dragon Curve")

        # Iterate over the directions
        for i, d in enumerate(directions):
            # Calculate the movement based on the current direction
            dx, dy = moves[d]
            next_point = current_point + np.array([dx, dy])

            # Dynamically update the coordinates using lists
            x.append(next_point[0])  # Append instead of using np.append
            y.append(next_point[1])  # Append instead of using np.append

            # Calculate a color based on the iteration index for visualization
            color = (i / len(directions), 0, 1 - (i / len(directions)))

            # Plot the line segment and pause for a brief animation effect
            plt.plot(x[-2:], y[-2:], color=color, lw=0.7)
            plt.pause(0.01)

            # Update the current point for the next iteration
            current_point = next_point

        # Display the final plot
        plt.show()
