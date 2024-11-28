import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.setworldcoordinates(-500, -500, 500, 500)
t = turtle.Turtle()
t.speed(0)

def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.right(120)

def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)


t.color("blue")
draw_square()
t.penup()
t.goto(150, 0)
t.pendown()
draw_triangle()
t.penup()
t.goto(-150, -150)
t.pendown()
draw_star(100)
turtle.done()
