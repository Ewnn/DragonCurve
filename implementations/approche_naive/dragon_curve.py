import turtle

class NaiveDragonCurve:
    def __init__(self, depth, length, angle):
        self.depth = depth
        self.length = length
        self.angle = angle

    def draw(self, n=None, sign=1):
        if n is None:
            n = self.depth  # Start with the initial depth

        if n == 0:
            turtle.forward(self.length)  # Base case: draw a line
        else:
            self.draw(n - 1, 1)  # Draw first half with a left turn
            turtle.left(self.angle * sign)
            self.draw(n - 1, -1)  # Draw second half with a right turn
