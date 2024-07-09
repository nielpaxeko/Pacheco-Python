# Day 5 project -> create a random password
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
letterAmount = int(input("How many letters would you like in your password? "))
symbolAmount = int(input("How many symbols would you like? "))
numberAmount = int(input("How many numbers would you like? "))

passWordLen = letterAmount + symbolAmount + numberAmount
word = []
for number in range(0, letterAmount):
    word.append(random.choice(letters))

for number in range(0, symbolAmount):
    word.append(random.choice(symbols))

for number in range(0, numberAmount):
    word.append(random.choice(numbers))

random.shuffle(word)

password = ""
for char in word:
    password += char

print(f"Here is your randomly generated password: {password}")
