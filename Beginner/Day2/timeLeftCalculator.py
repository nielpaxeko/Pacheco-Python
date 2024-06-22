# LIFE IN WEEKS Calculator
# Count how many days, weeks, and months you have left to live until you reach the age of 90

age = int(input("What is your current age? "))
days = (90 - age) * 365
weeks = (90 - age) * 52
months = (90 - age) * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
