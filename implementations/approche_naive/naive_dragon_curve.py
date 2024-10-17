import turtle

class DragonCurve:
    def __init__(self, depth, length, angle):
        """
        Initializes the DragonCurve with depth, segment length, and angle.
        """
        self.depth = depth
        self.length = length
        self.angle = angle

    def draw(self, n=None, sign=1):
        """
        Recursively draws the dragon curve.
        """
        if n is None:
            n = self.depth  # Start with the initial depth

        if n == 0:
            turtle.forward(self.length)  # Base case: draw a line
        else:
            self.draw(n - 1, 1)  # Draw first half with a left turn
            turtle.left(self.angle * sign)
            self.draw(n - 1, -1)  # Draw second half with a right turn

# Setup turtle environment
turtle.Screen().clear()
turtle.speed(0)
turtle.pensize(1)

# Initialize and draw the dragon curve
dragon_curve = DragonCurve(14, 5, 90)
turtle.penup()
turtle.goto(100, 200)
turtle.pendown()
dragon_curve.draw()

turtle.done()
