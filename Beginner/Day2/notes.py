# Day 2 Notes - Learning Outcomes

# 1 - Data Types 
# 2- Type Errors, Type casting, Type function
# 3- Mathematical Operator -> +, -, *, /, **, //
# 4- Mathematical Precedence
# 5- Rounding Numbers
# 6- F-Strings -> string formatting using f""

# 1. Data Types -> String, Integer, Float, Boolean

# a. String
# pulling out an element from the string = subscripting, the index starts from 0 to length-1
print("Hello"[3])

# b. Integer
# large integers can be separated with _
print(420_010)

# c. Float = floating point number
print(3.41231231)

# d. Boolean = True or False
print(True)

# 2. Type Error, Type Checking, Type Conversion

# Type Error -> when we give the wrong type to the function
print(type("aPPLE")) 

# TYPE CASTING -> CONVERT INTO ANOTHER VALUE
num_str = str(100)
# The type() function returns the data type of its parameters
type(num_str)
print(type(num_str))
print("My Wishful Score is "+ num_str)

# 3. Mathematical Operators
# '-' Substraction
# '*' Multiplication
# '**' Exponent
# '/' Division -> float result
# '//' Division -> number result
# '%' Modulus
# Priorities -> (), **, * / , + -

# Number Manipulation and F Strings
print(round(10/3,2)) # round function -> how many decimal places
# shorthand => symbol + '='

# f-string
score = 86
print(f'Your score is {score}')