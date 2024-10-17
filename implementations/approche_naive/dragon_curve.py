import turtle

class NaiveDragonCurve:
    def __init__(self, depth, length, angle):
        """
        Args:
            depth (int): The depth of the curve.
            length (float): The length of each segment.
            angle (float): The angle between segments.
        """
        self.depth = depth
        self.length = length
        self.angle = angle

    def draw(self, n=None, sign=1):
        """
        Args:
            n (int, optional): The current depth level. If None, starts with the initial depth.
            sign (int, optional): The direction of the turn (1 for left, -1 for right).
        """
        if n is None:
            n = self.depth  # Start with the initial depth

        if n == 0:
            turtle.forward(self.length)  # Base case: draw a line
        else:
            self.draw(n - 1, 1)  # Draw first half with a left turn
            turtle.left(self.angle * sign)
            self.draw(n - 1, -1)  # Draw second half with a right turn
