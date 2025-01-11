# EXERCISE 1: averageHeights -> implements for loops, standard I/O, arithmetic operator, rounding, and typecasting
# Do not use commas when inputting heights
student_heights = input("Enter the heights of the students: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
numOfStudents = 0
for student in student_heights:
    total_height += student
    numOfStudents += 1
averageHeight = total_height / numOfStudents
print(f"total height = {total_height}")
print(f"number of students = {numOfStudents}")
print(f"average height = {round(averageHeight)}")
