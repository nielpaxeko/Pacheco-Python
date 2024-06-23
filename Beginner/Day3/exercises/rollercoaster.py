# EXAMPLE OF NESTED IF-ELSE and IF-ELSE in succession:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height>=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    price = 0
    if age<12:
        price = 5
        print("The Child Cost is $5")
    elif age<=18:
        price = 7
        print("The Teenager Cost is $7")
    elif not (age>=45 and age<=55):
        price = 12
        print("The Adult Cost is $12")
    else:
        price = 0
        print("For those between 45-55 years old, tickets are free!")
    buyPhoto = input("Do you want photos?[Yes|No] ")
    if buyPhoto =='Yes':
        price += 3
        print("The Extra cost for photos is $3!")
    print(f"You must pay ${price}!")
else:
    print("Sorry, you are not allowed to ride this rolllercoaster")
    