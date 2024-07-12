# Notes day 24 - Files and File paths

# Read File
file1 = open("Intermediate/Day24/note1.txt") #built in function\
# by default, the setting is read/r
content1 = file1.read()
print(content1)
# takes up some of the resources/storage
file1.close()
# Close down means we are not longer using it
# Make sure to close as it could slow computer

# with keyword makes it so that we don't need to close it as it does it for use
with open("Intermediate/Day24/note1.txt") as file:
    content = file.read()
    print(content1)

# write => need to change the mode into w 
with open("Intermediate/Day24/note2.txt",'w') as file:
    file.write("I like tacos!")
    # rewriting a file completely
    # if the file doesnt exist -> create a new file

# append => need to change the mode into a 
with open("Intermediate/Day24/note1.txt",'a') as file:
    file.write("\nMy name is Edgar Pacheco!")