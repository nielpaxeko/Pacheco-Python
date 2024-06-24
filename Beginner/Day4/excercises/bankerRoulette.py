import random

friends = ["Michael", "Laufey", "Edgar", "Angela", "Luis", "Eric", "Kim", "Carlos"]
rand = random.randint(0, len(friends) - 1)
person = friends[rand].strip()

print(f"{person} is going to buy the meal today!")

