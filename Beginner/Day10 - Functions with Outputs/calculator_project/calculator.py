from logo import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    shouldContinue = True
    num1 = float(input("What's the first number? "))
    for op in operations:
        print(op)
    while shouldContinue:
        symbol = input("Pick an operation: ")
        nextNum = float(input("What's the next number? "))
        calculation = operations[symbol]
        answer = calculation(num1, nextNum)
        print(f"{num1} {symbol} {nextNum} = {answer}")
        if input(f"Type 'y' to continue operating with {answer} or 'n' to exit ") == "y":
            num1 = answer
        else:
            shouldContinue = False
            calculator()

calculator()