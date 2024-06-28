import math
# This excercise is simply about practicing the use of functions with parameters
def paint_calc(height, width, cover):
    numOfCans = math.ceil((height * width) / cover)
    print(f"You'll need {numOfCans} cans of paint.")


test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
