import turtle

def draw_square():
    circle_angle = 10

    window = turtle.Screen()
    window.bgcolor("red")
    fig = turtle.Turtle()
    fig.shape("circle")
    fig.color("white")
    fig.speed(10)

    while(circle_angle < 360):
        for i in range(0, 4):
            fig.forward(200)
            fig.right(90)

        fig.right(10)
        circle_angle +=  10
        
    window.exitonclick()


draw_square()
