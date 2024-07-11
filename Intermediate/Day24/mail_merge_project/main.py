#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Intermediate/Day24/mail_merge_project/Input/Letters/starting_letter.txt", mode = "r") as letter_file:
    letter = letter_file.read()
    lines = letter_file.readlines()
    num_of_names = len(lines)

with open("Intermediate/Day24/mail_merge_project/Input/Names/invited_names.txt", mode = "r") as name_file:
    names = name_file.readlines()
    for name in names:
        with open(f"Intermediate/Day24/mail_merge_project/Output/ReadyToSend/letter_to_{name}.txt", mode = "w") as new_letter:
            letter_text = letter.replace("[name]", name) 
            new_letter.write(letter_text)