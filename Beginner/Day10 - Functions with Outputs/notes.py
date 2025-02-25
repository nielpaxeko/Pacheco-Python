# Day 10 Notes - FUNCTIONS WITH OUTPUTS

# A. FUNCTIONS WITH OUTPUTS
def format_name1(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"
print(format_name1("MATThew", "aDrianus"))


# B. MULTIPLE RETURN VALUES
def format_name2(first_name, last_name):
    if first_name == "" or last_name == "":
        return "Wrong input!"
    return f"{first_name.title()} {last_name.title()}"

# C. DOCSTRINGS -> documenting a function
def format_name3(first_name, last_name):
    """Take a first and last name and join them together in title case"""
    if first_name == "" or last_name == "":
        return "Wrong input!"
    return f"{first_name.title()} {last_name.title()}"

print(format_name3("MATThew", "aDrianus"))

# D. PRINT VS RETURN
# Remember that print only shows message in console while return can be used in a function to return a variable back to the system.


# E. Functions -> inputs/functionality/output

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

# First Class objects: can be passed around as arguments (int, string, float)
def calculate(func, n1, n2):
    return func(n1,n2)

# F. Nested Function
def outer():
    print("I'm outer")
    def inner():
        print("I'm inner")
    return inner

# Return functions from other functions
inner_function = outer()
inner_function()

# G. Python Decorator
def decorate(a_function):
    def wrap():
        a_function()
    return wrap

import time

def delay_decorator(function):
    def wrap():
        time.sleep(2)
        function()
    return wrap

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_greeting():
    print("Greetings")

def say_bye():
    print("Goodbye")

say_hello()
say_bye()