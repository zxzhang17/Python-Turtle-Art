import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.setup(800, 800)
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.colormode(255)  # Allow RGB color mode with values 0-255


def draw_rhombus(center_x, center_y, width, height, direction, color):
    """Draws a rhombus given center, width, height, direction, and color."""
    t.penup()
    t.goto(center_x, center_y)
    t.setheading(direction)
    t.pendown()
    t.color(color)
    t.begin_fill()
    # Calculate the vertices of the rhombus
    t.forward(width / 2)
    t.left(120)
    t.forward(height)
    t.left(120)
    t.forward(width)
    t.left(120)
    t.forward(height)
    t.left(120)
    t.forward(width / 2)
    t.end_fill()


# Draw 50 random rhombuses
for _ in range(50):
    center_x = random.uniform(-300, 300)
    center_y = random.uniform(-300, 300)
    width = random.uniform(50, 150)
    height = random.uniform(50, 150)
    direction = random.uniform(0, 360)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    draw_rhombus(center_x, center_y, width, height, direction, color)

turtle.done()
