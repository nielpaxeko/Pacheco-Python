# Day 1 Notes - Learning Outcomes
# 1-Printing to Console -> using print function
# 2-String Manipulation -> "", '', + and \n
# 3-Receiving Inputs -> Input function
# 4-Python Variables

# 1. PRINTING TO CONSOLE
print("Hello, World!")
print("I'm extremely hungry")
print('He said,"I wish that i could be like the cool kids!') #double inside single

# 2. STRING MANIPULATION
# backslash n
print("Hello, it's me\nI was wondering if after all these years you'd like to meet") #use \n to create enter

# concatenate literal strings
print("Hello!"+" My name is Matthew")

# INDENTATION IS VERY IMPORTANT

# 3. INPUTS
input("What is your name?\n") # the inputted data is passed into the input
# the program paused until the user input something
# syntax = input(prompt) -> prompt = string

print("Hello "+ input("What is your name?\n"))
# input first-> then print hello + inputted string

# INPUT EXERCISE
print(len(input("What is your name? ")))
# len -> length of a string

# 4. VARIABLES
name = input("What's my name? ") # like taking notes into a notebook
# variables are useful so that we can refer back to the value

length = len(name)

# VARIABLE EXERCISE
a = input("a: ")
b = input('b: ')

c = a
a = b
b = c

print("a = "+a)
print("b = "+b)

# VARIABLES NAMING -> BASIC RULES AND BEST PRACTICES
# 1. MAKE SURE THE NAMES MAKE SENSE
# 2. YOU CAN'T ADD SPACES OR USE KEYWORDS
# 3. SEPARATE WORDS USING UNDERSCORE -> IN PYTHON -> BEST PRACTICE