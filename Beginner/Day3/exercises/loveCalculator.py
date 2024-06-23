# This exercises "calculates" the love score of two names

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

loveName = name1.lower() + name2.lower()
trueCalc = loveName.count("t") + loveName.count("r") + loveName.count("u") + loveName.count("e")
loveCalc = loveName.count("l") + loveName.count("o") + loveName.count("v") + loveName.count("e")

score = trueCalc*10 + loveCalc

if score <10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")