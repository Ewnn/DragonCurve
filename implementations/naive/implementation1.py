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
turtle.pensize(1) # Set the pen size to x pixels

# Setup a starting point
turtle.penup()
turtle.goto(100,200)
turtle.pendown()

# Call function
Dragon(14, 5, 90)
turtle.done()