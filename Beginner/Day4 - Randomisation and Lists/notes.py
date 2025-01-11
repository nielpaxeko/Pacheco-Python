# Day 4 Notes - Learning Outcomes

# 1 - RANDOM MODULE -> GENERATE RANDOM NUMBERS AND RANDOM FLOATS
# 2 - LISTS-> BASIC LIST FUNCTIONS(CREATE, UPDATE, ACCESS), NESTED LISTS


# 1. Random Module -> pseudo-random 
import random
# documentation in askpython.com

# randint(a,b) -> a<=x<=b
random_integer = random.randint(1,100)
print(random_integer)

# random floating point
# a. random()-> 0.0 - 1.0 (not until 1)
random_float1 = random.random()
print(random_float1)

# b. get random floating point number between 0 and 5
random_float2 = random.random()*5
print(random_float2)

# c. get random floating point number between 1 and 5
random_float3 = 1 + random.random()*4
print(random_float3)

# 2. Lists 
# Lists -> data structure

fruits = ["orange",'apple']
print(fruits)
print(type(fruits))

print(fruits[0])# index 0
print(fruits[-1])# index from the length-1
print(len(fruits))
fruits.append("mango")
fruits.insert(1,"grapefruit")

# index error -> retrieving the wrong index -> out of bounds

# nested lists 
# there are fruits and vegetables
dirty_dozen = ["Strawberries","Spinach", "Kale", "Nectarines", 
"Apples", "Grapes","Peaches", "Cherries", "Pears", "Tomatoes",
"Potatoes", "Celery"]
print(dirty_dozen)

fruits =["Strawberries","Nectarines","Apples", "Grapes","Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale","Tomatoes", "Potatoes", "Celery"]

# contains 2 lists
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)