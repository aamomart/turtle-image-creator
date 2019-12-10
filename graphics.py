import turtle as t

grid = (
    ("","","","","","","",""),
    ("","","","","","","",""),
    ("","","black","red","","","",""),
    ("","","","","","red","",""),
    ("","","","","","","",""),
    ("","yellow","","","","","",""),
    ("","","","","","","",""),
    ("","","","","","","black","black")
)

size = 20

t.tracer(0,0)
t.hideturtle()

t.penup()
t.goto(-4 * size, 3 * size)
t.pendown()

for y in range(8):
    print(grid[y])
    for x in range(8):
        t.color(grid[y][x])
        t.begin_fill()
        for i in range(4):
            t.forward(size)
            t.left(90)
        t.end_fill()
        t.color('black')
        for i in range(4):
            t.forward(size)
            t.left(90)
        t.forward(size)

    t.penup()
    t.right(90)
    t.forward(size)
    t.left(90)
    t.backward(8 * size)
    t.pendown()

    t.update()

t.exitonclick()