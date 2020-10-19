import turtle
# makes turtle that draws

tina = turtle.Turtle()

def draw_square(size):
    tina.color("red")
    tina.pendown()
    for i in range(4):
	    tina.forward(size)
	    tina.right(90)


def main():
    tina.clear()
    tina.penup()
    tina.forward(200)

    for i in range(4):
        size = (i+1)*10
        draw_square(size)
        tina.penup()
        tina.forward(size)

    tina.penup()
    tina.forward(100)

    for i in range(6):
        draw_square(40)
        tina.right(60)


if __name__ == '__main__':
    main()
