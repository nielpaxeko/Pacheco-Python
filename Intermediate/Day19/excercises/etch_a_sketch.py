from turtle import Turtle, Screen

tim = Turtle()
tim.speed(0)
tim.pensize(5)
canvas = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.penup()
    
canvas.listen()
canvas.onkey(key = "w", fun = move_forward)
canvas.onkey(key = "a", fun = turn_left)
canvas.onkey(key = "s", fun = move_backward)
canvas.onkey(key = "d", fun = turn_right)
canvas.onkey(key = "c", fun = clear)

canvas.exitonclick()