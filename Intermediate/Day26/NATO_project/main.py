import pandas as np

#TODO 1. Create a dictionary in this format:
data = np.read_csv("NATO_project/nato_phonetic_alphabet.csv")
# print(data)
nato_dict = {row.letter:row.code for (idx, row) in data.iterrows()}

print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
coded_word = [nato_dict[letter] for letter in word]
print(coded_word)