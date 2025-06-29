import turtle

# Create a turtle object
wn = turtle.Screen()
skk = turtle.Turtle()

# Set up the turtle's appearance
skk.speed(0)
skk.color("red")
skk.pensize(3)

# # Draw a square
# for i in range(4):
#     skk.forward(50)
#     skk.right(90)

# # Draw a triangle
# for i in range(3):
#     skk.forward(50)
#     skk.right(120)

# # Draw "A"
# skk.left(120)
# skk.forward(100)
# skk.right(240)
# skk.forward(100)
# skk.back(50)
# skk.right(240)
# skk.forward(50)


colors = ["red", "purple", "blue", "green", "orange", "yellow"]
t = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()

wn.mainloop()
