# Type Hints in Python
# Type hints allow you to specify the expected data types for variables, function arguments, and return types. 
# While Python is a dynamically typed language (meaning variables can change types during execution), 
# type hints make it easier to understand what types a function or variable expects, 
# leading to fewer bugs and easier code maintenance.


# This makes it so that both paramas must be an int and the return will also be an int
def add(a: int, b: int) -> int:
    return a + b