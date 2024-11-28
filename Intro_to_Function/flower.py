# flower.py
import turtle

# setup screen and default setting
screen = turtle.Screen()
screen.setup(500, 500)
screen.setworldcoordinates(-500, -500, 500, 500)
t = turtle.Turtle()
t.speed(0)

# define how to draw petal
def draw_petal():
    t.circle(50, 60)
    t.left(120)
    t.circle(50, 60)
    t.left(120)

# define how many flowers in the petal
def draw_flower(petals):
    for _ in range(petals):
        draw_petal()
        t.left(360 / petals)

# define how to draw trunk
def draw_trunk():
    t.right(90)
    t.forward(100)
    t.backward(100)
    t.left(90)

# Example usage
t.color("green")
draw_trunk()
t.color("red")
draw_flower(8)
turtle.done()
