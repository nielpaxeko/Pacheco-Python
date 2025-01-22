import colorgram
from turtle import Turtle, Screen
import random as r

# NOTE: MUST RUN ON VIRTUAL ENVIRONMENT WITH COLORGRAM PIP INSTALLED


# rgb_colors = []
# colors = colorgram.extract('hirst.webp', 41)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    

screen = Screen()
tim = Turtle()
tim.shape("turtle")
tim.speed(0)
screen.colormode(255)
tim.penup()
color_list = [(232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]

# Starting position for tim
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


def paint_line():
    for i in range(10):
        tim.color()
        tim.dot(20, r.choice(color_list))
        tim.forward(50)
        
def move_up():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    
def hirst():
    for i in range(10):
        paint_line()
        move_up()
    tim.hideturtle()
        
hirst()

        


