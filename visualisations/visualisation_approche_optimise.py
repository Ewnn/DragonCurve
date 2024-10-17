from implementations.approche_optimise.dragon_curve import DragonCurveGraph

def visualisation_approche_optimise():
    # Create an instance of the DragonCurveGraph
    dragon_curve_graph = DragonCurveGraph()

    # Draw the dragon curve with a specific number of iterations
    iterations = 25 
    dragon_curve_graph.draw_dragon_curve(iterations)
