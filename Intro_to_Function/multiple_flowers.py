# flower.py
import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.setworldcoordinates(-500, -500, 500, 500)
t = turtle.Turtle()
t.speed(0)

def draw_petal():
    t.circle(50, 60)
    t.left(120)
    t.circle(50, 60)
    t.left(120)

# also define how many petals in turtle
def draw_flower(petals):
    for _ in range(petals):
        draw_petal()
        t.left(360 / petals)

def draw_trunk():
    t.right(90)
    t.forward(100)
    t.backward(100)
    t.left(90)

# Drawing multiple flowers by moving the turtle manually each time
# Flower 1
t.penup()
t.goto(-200, 0)
t.pendown()
t.color("green")
draw_trunk()
t.color("red")
draw_flower(6)

# Flower 2
t.penup()
t.goto(0, 0)
t.pendown()
t.color("green")
draw_trunk()
t.color("red")
draw_flower(8)

# Flower 3
t.penup()
t.goto(200, 0)
t.pendown()
t.color("green")
draw_trunk()
t.color("red")
draw_flower(10)

turtle.done()
