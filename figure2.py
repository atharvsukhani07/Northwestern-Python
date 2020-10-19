import turtle

tina = turtle.Turtle()

def draw_triangle():
    tina.color("blue")
    tina.pendown()
    for i in range(3):
        tina.forward(50)
        tina.right(120)

def draw_square():
    tina.color("red")
    tina.pendown()
    for i in range(4):
        tina.forward(50)
        tina.right(90)

def draw_pentagon():
    tina.color("black")
    tina.pendown()
    for i in range(5):
        tina.forward(50)
        tina.right(72)


def draw_hexagon():
    tina.color("orange")
    tina.pendown()
    for i in range(5):
        tina.forward(50)
        tina.right(60)


def main():
    tina.clear()
    tina.penup()
    tina.back(200)

    draw_triangle()
    tina.penup()
    tina.forward(100)

    draw_square()
    tina.penup()
    tina.forward(100)

    draw_pentagon()
    tina.penup()
    tina.forward(100)

    draw_hexagon()
    tina.forward(50)

if __name__ == '__main__':
    main()
    
