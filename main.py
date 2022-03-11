# Etch-a-Sketch
# F : Move Forwards
# B : Move Backwards
# D : Move Clockwise
# Q : Move Counter-Clockwise
# L : Move Left
# R : Move Right
# C : Clear All


from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# Function to move forwards
def move_forwards():
    """ Move Forward """
    tim.forward(10)


# Function to move backwards
def move_backwards():
    """ Move Backwards"""
    tim.backward(10)


# Function to turn left
def move_left():
    """ Turn Left"""
    tim.left(10)


# Function to turn right
def move_right():
    """ Turn Right"""
    tim.right(10)


# Function to move clockwise
def move_clockwise():
    """ Move Clockwise"""
    tim.circle(-50, 10)


# Function to move clockwise
def move_counter_clockwise():
    """ Move Counter-Clockwise"""
    tim.circle(50, 10)


# Function to clear all the drawings
def clear_all():
    """ Clear All Drawings"""
    screen.reset()


screen.listen()
screen.onkey(fun=move_forwards, key="f")
screen.onkey(fun=move_backwards, key="b")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=move_counter_clockwise, key="q")
screen.onkey(fun=move_left, key="l")
screen.onkey(fun=move_right, key="r")
screen.onkey(fun=clear_all, key="c")
screen.exitonclick()

