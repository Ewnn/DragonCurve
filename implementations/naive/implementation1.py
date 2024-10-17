import turtle

class Dragon:
    def __init__(self, n, length, angle):
        self.n = n
        self.length = length
        self.angle = angle

    def draw(self):
        if self.n == 0:
            turtle.forward(self.length)
        else:
            self.draw(self.n - 1, self.length, 90)
            turtle.left(self.angle)
            self.draw(self.n - 1, self.length, -90)

# Setup environment
turtle.Screen().clear()
turtle.speed(0)
turtle.pensize(1)

# Create a Dragon object
dragon = Dragon(14, 5, 90)

# Setup a starting point
turtle.penup()
turtle.goto(100, 200)
turtle.pendown()

# Call the draw method on the Dragon object
dragon.draw()

turtle.done()