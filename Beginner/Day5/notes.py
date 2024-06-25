# Day 5 Notes - Learning Outcomes

# 1 - FOR LOOPS -> SIMPLE FOR LOOPS, RANGE FUNCTION, INFINITE LOOP USING LISTS
# 2 - RANDOM -> SHUFFLE
# 3 - LISTS -> CREATE A LIST USING *

# 1. For Loops
fruits = ["Apple", "Peach", "Banana"]
for fruit in fruits:
    print(fruit + " Pie")
# INDENTATION IS IMPORTANT!!

# Range Functions
for num in range(1, 10, 3):
    # range(x,y,z)
    # x = start from x
    # y = until before y
    # z = size of steps
    print(num)

# Gaussian formula
total = 0
for num in range(1, 101):
    total += num
