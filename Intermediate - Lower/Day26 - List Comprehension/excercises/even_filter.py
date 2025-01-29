list_of_strings = input("Enter the numbers: ").split(',')

# TODO: Use list comprehension to convert the strings to integers 👇:
list_of_integers = [int(string) for string in list_of_strings]

# TODO: Use list comprehension to filter out the odd numbers and then square them
# and store the even numbers in a list called "result"
result = [num*num for num in list_of_integers if num % 2 == 0]

print(result)