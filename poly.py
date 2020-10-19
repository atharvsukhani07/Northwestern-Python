import turtle
wn = turtle.Screen()
ezra = turtle.Turtle()

def poly(side, angle):
    ezra.setheading(0)
    while(True):
        ezra.forward(side)
        ezra.right(angle)
        if ezra.heading() == 0:
            break;


poly(40, 72)
ezra.clear()
poly(80, 144)
ezra.clear()
poly(50, 90)
ezra.clear()
