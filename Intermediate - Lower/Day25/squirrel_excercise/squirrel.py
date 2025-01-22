import pandas as np

data = np.read_csv("/Users/nielpaxeko/Desktop/Programming/Python/Pacheco-Python/Intermediate/Day25/squirrel_excercise/squirrel_data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels)
# print(cinnamon_squirrels)
# print(black_squirrels)

data_dict = {
    "Fur_Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, cinnamon_squirrels, black_squirrels]
}

df = np.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")