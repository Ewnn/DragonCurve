import matplotlib.pyplot as plt
from .graph import Graph

class DragonCurveGraph(Graph):  # Inherit from the Graph class
    def generate_dragon_curve(self, iterations):
        # Generate the sequence of directions for the dragon curve
        directions = [0]  # Start by going right
        
        for _ in range(iterations):
            mirrored = [(d + 1) % 4 for d in reversed(directions)]
            directions.extend([1] + mirrored)
            
        return directions

    def draw_dragon_curve(self, iterations):
        # Draw the dragon curve using the generated directions
        directions = self.generate_dragon_curve(iterations)
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Directions: right, up, left, down

        current_point = (0, 0)  # Starting point
        x, y = [current_point[0]], [current_point[1]]  # Lists to store x and y coordinates
        
        plt.figure(figsize=(10, 10))  # Set up the plot
        plt.axis('equal')  # Maintain aspect ratio
        plt.title("Dragon Curve")  # Title of the plot
        
        for i, d in enumerate(directions):
            dx, dy = moves[d]  # Get the movement corresponding to the current direction
            next_point = (current_point[0] + dx, current_point[1] + dy)  # Calculate the next point
            
            self.add_edge(current_point, next_point)  # Add the edge to the graph
            x.append(next_point[0])  # Append the x-coordinate of the next point
            y.append(next_point[1])  # Append the y-coordinate of the next point
            
            # Calculate dynamic color based on the iteration index
            color = (i / len(directions), 0, 1 - (i / len(directions)))  # Change from red to blue
            
            # Draw the segment in real-time
            plt.plot(x[-2:], y[-2:], color=color, lw=0.7)  # Plot the line segment
            plt.pause(0.01)  # Pause to display the animation
            
            current_point = next_point  # Update the current point

        plt.show()  # Show the final plot