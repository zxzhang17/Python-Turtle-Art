import turtle

# Create a turtle instance
t = turtle.Turtle()
t.speed(0)
t.forward(50)
t.color("light blue")

for i in range(1000):
    t.circle(100, 60 - i)  # Draw a partial circle with a decreasing angle
    t.left(i)  # Turn left by an increasing angle

turtle.done()