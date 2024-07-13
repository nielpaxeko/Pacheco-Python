# This code takes in a sentence and creates a dictionary of each words and its length using dict comprehension
sentence = input("Enter a sentence: ")
result = {word:len(word) for word in sentence.split()}
print(result)