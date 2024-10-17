import matplotlib.pyplot as plt

class DragonCurveGraph:
    def __init__(self):
        self.graph = {} # Stores the graph as a dictionary
    
    def add_edge(self, p1, p2):
        if p1 not in self.graph:
            self.graph[p1] = [] # Create a new list for point p1 if it doesn't exist

        if p2 not in self.graph:
            self.graph[p2] = [] # Create a new list for point p2 if it doesn't exist
        
        self.graph[p1].append(p2) # Add p2 to the list of neighbors of p1
        self.graph[p2].append(p1) # Add p1 to the list of neighbors of p2

    def generate_dragon_curve(self, iterations):
        directions = [0]  # Start with a single direction

        for _ in range(iterations):
            mirrored = [(d + 1) % 4 for d in reversed(directions)] # Mirror the directions
            directions.extend([1] + mirrored) # Add the new directions
        return directions

    def draw_dragon_curve(self, iterations):
        directions = self.generate_dragon_curve(iterations)
        moves = [(1,0),(0,1),(-1,0),(0,-1)] # Directions : Right / Top / Left / Bottom

        inital_move = (0,0) # Starting Point
        x, y = [inital_move[0]],[inital_move[1]] # List to store position x , y

        plt.figure(figsize=(10, 10))  # Define figure height
        plt.axis('equal')  # Contain aspect ratio
        plt.title("Courbe de Dragon")  # Title of the graphic

        for d in directions:
            dx, dy = moves[d]  # Get the movement corresponding to the direction
            next_point = (current_point[0] + dx, current_point[1] + dy)  # Calculate the next point
            
            self.add_edge(current_point, next_point)  # Add the edge to the graph
            x.append(next_point[0])  # Append the x-coordinate of the next point
            y.append(next_point[1])  # Append the y-coordinate of the next point
            
            # Draw the segment in real-time
            plt.plot(x[-2:], y[-2:], color='blue', lw=0.7)  # Plot the segment
            plt.pause(0.01)  # Pause to display the animation
            
            current_point = next_point  # Update the current point

        plt.show()  # Display the graphic



