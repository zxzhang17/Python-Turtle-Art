import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(500, 500)
screen.setworldcoordinates(-500, -500, 500, 500)

def self_defined_shape(size, angle, increment, color):
    t.color(color)
    for _ in range(200):
    # while True:
        t.forward(size)
        t.right(angle)
        # size = size + increment
        size += increment

# use
# self_defined_shape(10, 144, 1, "purple") # star
t.speed(0)  # Fastest speed
while True:
    self_defined_shape(50, 170, 2, "blue")
    t.home()
    self_defined_shape(50, 70, 1.5, "red")
    t.home()
    self_defined_shape(30,100, 2, "green")
    t.home()
    self_defined_shape(20, 130, 5, "yellow" )
    t.home()
    self_defined_shape(70, 200, 0.5, "magenta")
    t.home()
    self_defined_shape(10, 50, 2, "brown")
    t.home()
