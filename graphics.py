import turtle as t

grid = (
    ("001","111","001","111","001","111","001","111"),
    ("111","001","111","001","111","001","111","001"),
    ("001","111","001","111","001","111","001","111"),
    ("111","001","111","001","111","001","111","001"),
    ("001","111","001","111","001","111","001","111"),
    ("111","001","111","001","111","001","111","001"),
    ("001","111","001","111","001","111","001","111"),
    ("111","001","111","001","111","001","111","001")
)

colourDictionary = {
    "000": "white",
    "001": "green",
    "010": "yellow",
    "011": "blue",
    "100": "red",
    "101": "light grey",
    "110": "dark grey",
    "111": "black"
}

size = 20

t.tracer(0,0)
t.hideturtle()

t.penup()
t.goto(-4 * size, 3 * size)
t.pendown()

for y in range(8):
    for x in range(8):
        t.color(colourDictionary[grid[y][x]])
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