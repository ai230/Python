import turtle

def draw_square():
    # Create window
    window = turtle.Screen()
    window.bgcolor("red")

    #Create object
    fig = turtle.Turtle()
    fig.shape("circle")
    fig.color("white")
    fig.speed(5)
    fig.forward(200)
    fig.right(90)
    fig.forward(200)
    fig.right(90)
    fig.forward(200)
    fig.right(90)
    fig.forward(200)

    fig2 = turtle.Turtle()
    fig2.shape("arrow")
    fig2.circle(100)


    #Close the window by click
    window.exitonclick()


draw_square()
