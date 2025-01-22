# Day 16 Notes - OOP

# Import turtle module -> add graphics to the screen and paint with turtle
from turtle import Turtle, Screen
import prettytable as pt

# Objects = real world Object
# Has attributes (variables, associated with the object) and methods (functions, what the object can do)

# A class is a blueprint of objects, but the object created from said class is what we will actually be using
# Pascal case = MyClass


# Create a new object from turtle
timmy = Turtle()
timmy.shape("turtle")  # change the shape
timmy.color("coral", "green")  # border, fill
timmy.forward(100)  # move forward


# print(timmy) -> an object
# accessing attribute -> object.attribute
my_screen = Screen()
# print(my_screen.canvheight) # height of the screen
# print(my_screen.canvwidth) #width of the screen

# accessing methods -> object.method()
my_screen.exitonclick()  # running until we click on the screen

# Packages are code by other developers that we can install and import to make our lives easier

table = pt.PrettyTable()
table.add_column(
    "Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], align="c", valign="t"
)
table.add_column("Type", ["Electric", "Water", "Fire"], align="l", valign="b")
print(table)
