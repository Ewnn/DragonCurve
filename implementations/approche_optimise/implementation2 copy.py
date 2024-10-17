class DragonCurveGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, p1, p2):
        if p1 not in self.graph:
            self.graph[p1] = []

        if p2 not in self.graph:
            self.graph[p2] = []
        
        self.graph[p1].append(p2)
        self.graph[p2].append(p1)
