# BMI CALCULATOR excercise from day 2
# Formula = weight/(height^2)
weight = float(input("Input your Weight (kg): "))
height = float(input("Input your Height (m): "))
print("Your BMI index is "+ str(int(weight/(height**2))))