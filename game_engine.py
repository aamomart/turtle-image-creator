import turtle as t
import math

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

class IsoscelesTriangle(object):

    def __init__(self, _x, _y, _base, _height, _c):
        self.x = _x
        self.y = _y
        self.base = _base
        self.height = _height
        self.c = _c

    def __str__(self):
        return "IsoscelesTriangle at: ({},{}) with base: {} and height {}".format(self.x, self.y, self.base, self.height)

    def get_congruent_size(self):
        return math.sqrt(math.pow(self.base/2,2) + math.pow(self.height,2))

    def get_base_angle(self):
        return math.degrees(math.atan(self.height/(self.base/2)))

    def get_top_angle(self):
        return (90 - self.get_base_angle()) * 2

class Square(object):

    def __init__(self, _x, _y, _size, _c):
        self.x = _x
        self.y = _y
        self.size = _size
        self.c = _c

    def __str__(self):
        return "Square at: ({},{}) with size: {}".format(self.x, self.y, self.size)      

def draw_equilateral(triangle):
    t.penup()
    t.goto(triangle.x, triangle.y)
    t.pendown()
    t.color(triangle.c)
    t.begin_fill()
    for a in range (3):
        t.forward(triangle.size)
        t.left(120)
    t.end_fill()

def draw_isosceles(isosceles_triangle):
    t.penup()
    t.goto(isosceles_triangle.x, isosceles_triangle.y)
    t.pendown()
    t.color(isosceles_triangle.c)
    t.begin_fill()
    t.forward(isosceles_triangle.base)
    t.left(180 - isosceles_triangle.get_base_angle())
    t.forward(isosceles_triangle.get_congruent_size())
    t.left(180 - isosceles_triangle.get_top_angle())
    t.forward(isosceles_triangle.get_congruent_size())
    t.left(180 - isosceles_triangle.get_base_angle())
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

def renderDrawing():
    t.update()
    t.exitonclick()