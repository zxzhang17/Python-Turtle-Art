"""Go to random places with random colors
    drawing multiple shapes
"""

import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.setup(500, 500)  # Set the screen size to 500x500 pixels
screen.setworldcoordinates(-500, -500, 500, 500)  # Set coordinate system from -500 to 500
t = turtle.Turtle()
t.speed(0)  # Set turtle speed to the maximum
turtle.colormode(255)  # Use RGB color mode with values ranging from 0 to 255

def draw_square():
    """Draws a square at a random position with a random color."""
    t.color(random_color())  # Set a random color
    t.penup()
    t.goto(random_position())  # Move to a random position on the screen
    t.pendown()
    t.begin_fill()  # Begin filling the shape with color
    for _ in range(4):  # Draw a square by repeating 4 sides
        t.forward(100)  # Move forward by 100 units
        t.right(90)  # Turn right by 90 degrees
    t.end_fill()  # End filling the shape

"""
The program doesn't know what random_color and random_position are,
so we need to define them in separate functions.
"""
def random_color():
    """Generate a random color in RGB format."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_position():
    """Generate a random position within the screen limits."""
    return (random.uniform(-200, 200), random.uniform(-200, 200))


# Drawing multiple shapes
for _ in range(5):
    draw_square()  # Draw 5 random squares

turtle.done()  # Complete the drawing and keep the window open
