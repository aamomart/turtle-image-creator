import turtle as t

t.tracer(0,0)
t.hideturtle()

class Circle(object):

    def __init__(self, _x, _y, _r, _c):
        self.x = _x
        self.y = _y
        self.r = _r
        self.c = _c

    def __str__(self):
        return "Circle at: ({},{}) with radius: {}".format(self.x, self.y, self.r)

class Triangle(object):

    def __init__(self, _x, _y, _size, _c):
        self.x = _x
        self.y = _y
        self.size = _size
        self.c = _c

    def __str__(self):
        return "Triangle at: ({},{}) with size: {}".format(self.x, self.y, self.size)   

class Square(object):

    def __init__(self, _x, _y, _size, _c):
        self.x = _x
        self.y = _y
        self.size = _size
        self.c = _c

    def __str__(self):
        return "Square at: ({},{}) with size: {}".format(self.x, self.y, self.size)             

def draw_triangle(triangle):
    t.penup()
    t.goto(triangle.x, triangle.y)
    t.pendown()
    t.color(triangle.c)
    t.begin_fill()
    for a in range (3):
        t.forward(triangle.size)
        t.left(120)
    t.end_fill()

def draw_circle(circle):
    t.penup()
    t.goto(circle.x,circle.y)
    t.pendown()
    t.color(circle.c)
    t.begin_fill()
    t.circle(circle.r)
    t.end_fill()

def draw_square(square):
    t.penup()
    t.goto(square.x, square.y)
    t.pendown()
    t.color(square.c)
    t.begin_fill()
    for i in range(4): 
        t.forward(square.size)
        t.left(90)
    t.end_fill()

circles = [Circle(0,0,50,"blue"), Circle(60,50,20,"green"), Circle(-60,50,20,"red")]
triangles = [Triangle(0,-200,50,"blue"), Triangle(0,-190,20,"green"), Triangle(0,-210,20,"red")]
squares = [Square(-100,0,50,"blue"), Square(-110,0,20,"green"), Square(-90,0,20,"red")]

for circle in circles:
    draw_circle(circle)

for triangle in triangles:
    draw_triangle(triangle)

for square in squares:
    draw_square(square)

t.update()

t.exitonclick()