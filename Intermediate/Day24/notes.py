# Notes day 24 - Files and File paths

# Read a file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write or append on a file
with open("Intermediate/Day24/my_file.txt", mode = "a") as file:
    file.write("New Text")