# TODO: INDEX ERROR EXCERCISE - Catch the exception and make sure the code runs without crashing
fruits = ["banana", "ananas", "apple"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
make_pie(4)