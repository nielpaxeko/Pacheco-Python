# This day's project is to create a calculator that calculate how much money to tip based on percentages.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much would you like to tip based on percentage? "))
people = int(input("How many people to split the bill? "))
tip = tip / 100 + 1
finalBill = (bill*tip)/people
print(f'Each person should pay: ${round(finalBill,2)}')
