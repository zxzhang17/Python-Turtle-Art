import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Colors for the gradient effect
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]

# Draw the colorful crescent rings
for i in range(36):  # 36 iterations to complete a circle
    t.color(colors[i % len(colors)])  # Repeat colors in a cycle
    t.begin_fill()
    t.circle(100, 180)  # Half-circle
    t.left(60)
    t.circle(100, 180)
    t.left(10)
    t.end_fill()

turtle.done()