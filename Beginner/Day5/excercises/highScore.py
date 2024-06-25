# EXERCISE 2: highScore -> implements for loops, standard I/O, arithmetic operator, conditionals, and typecasting

# Input a list of student scores
student_scores = input("Enter the students' scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highScore = 0
for score in student_scores:
  if score > highScore:
    highScore = score
print(f"The highest score in the class is: {highScore}")