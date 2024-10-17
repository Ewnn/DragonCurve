import turtle
from implementations.approche_naive.dragon_curve import NaiveDragonCurve
from implementations.approche_naive.turtle_setup import setup_turtle

def naive_dragon_curve_approach():
    setup_turtle()  # Configures the Turtle environment

    naive_dragon_curve = NaiveDragonCurve(14, 5, 90)  # Creates a Dragon Curve with depth 14, length 5, and angle 90 degrees
    turtle.penup()  # Lifts the pen to prevent drawing
    turtle.goto(100, 200)  # Moves the Turtle to the starting position
    turtle.pendown()  # Lowers the pen to start drawing
    naive_dragon_curve.draw()  # Draws the Dragon Curve

    turtle.done()  # Keeps the Turtle window open until it's closed