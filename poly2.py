import turtle
wn = turtle.Screen()
ezra = turtle.Turtle()

def lcm(a, b):
    multiple = 0
    while True:
        multiple += a
        if multiple % b == 0:
            return int(multiple / a);


def poly(side, angle):
    ezra.setheading(0)
    for i in range(lcm(angle,360)):
        ezra.forward(side)
        ezra.left(angle)
           

poly(80, 144)
ezra.clear()
poly(1, 1)
ezra.clear()
poly(40, 135)
ezra.clear()
poly(80, 108)
ezra.clear()
