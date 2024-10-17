import turtle

# Function to draw dragon
def Dragon(n, length, angle):
    """
    Args:
        n: Recursion depth.
        length: Length of each line segment.
        angle: Angle of rotation.
    """ 
    if n == 0:
        # Base case: draw a straight line
        turtle.forward(length) 
    else:
        # Recursive case: divide and conquer
        Dragon(n - 1, length, 90) # Draw the left half
        turtle.left(angle) # Turn left
        Dragon(n - 1, length, -90) # Draw the right half

# Setup environment
turtle.Screen().clear() # Clear screen
turtle.speed(0) # Setup speed to fastest speed
turtle.pensize(2) # Set the pen size to 2 pixels

# Predefined parameters
n = 14
