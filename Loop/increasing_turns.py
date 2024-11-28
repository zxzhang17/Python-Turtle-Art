import turtle
import random


t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "green", "purple", "orange", "yellow", "pink", "cyan", "magenta"]

# Draw the pattern with random colors
for i in range(100):
    t.color(random.choice(colors))  # Pick a random color
    t.left(5 + i * 20)  # Gradually increase the angle
    t.forward(50)

# Keep the window open until closed
turtle.done()