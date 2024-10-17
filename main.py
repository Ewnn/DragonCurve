import turtle
from implementations.approche_naive.dragon_curve import NaiveDragonCurve
from implementations.approche_naive.turtle_setup import setup_turtle


def naive_dragon_curve_approach():
    setup_turtle()

    naive_dragon_curve = NaiveDragonCurve(14, 5, 90)
    turtle.penup()
    turtle.goto(100, 200)
    turtle.pendown()
    naive_dragon_curve.draw()

    turtle.done()

if __name__ == "__main__":
    naive_dragon_curve_approach()