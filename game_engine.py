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

def draw_circle(circle):
    t.penup()
    t.goto(circle.x,circle.y)
    t.pendown()
    t.color(circle.c)
    t.begin_fill()
    t.circle(circle.r)
    t.end_fill()

circles = [Circle(0,0,50,"blue"), Circle(60,50,20,"green"), Circle(-60,50,20,"red")]

for circle in circles:
    draw_circle(circle)

t.update()

t.exitonclick()