# DATA TYPE EXERCISE - this excercise is meant to add the first and second digit of a two digit number
two_digit_number = input("Enter a two digit number: ")
if len(two_digit_number)!=2:
    print("Invalid input")
print(int(two_digit_number[0]) + int(two_digit_number[1]))