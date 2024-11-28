import turtle
import random

# Create a turtle instance
t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "green", "purple", "orange", "yellow", "pink", "cyan", "magenta"]

# Draw a spiral pattern with circles and random colors
for i in range(1000):
    t.color(random.choice(colors))  # Randomly pick a color
    t.circle(100, 60 - i)
    t.left(i)

# Keep the window open until closed
turtle.done()