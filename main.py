from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move():
    tim.forward(10)


screen.listen()
screen.onkey(fun=move, key="space")
screen.exitonclick()
