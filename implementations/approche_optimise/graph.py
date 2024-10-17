class Graph:
    def __init__(self):
        # Initialize a dictionary to store edges (connections) between points (nodes)
        self.graph = {}

    def add_edge(self, point1, point2):
        # Add an edge between two points in the graph
        if point1 not in self.graph:
            self.graph[point1] = []
        if point2 not in self.graph:
            self.graph[point2] = []
        self.graph[point1].append(point2)
        self.graph[point2].append(point1)
