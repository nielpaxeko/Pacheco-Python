from logo import logo
# This day's project is a ceasar cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# This function decodes or encodes a given text by a given shift amount
# If direction is encode then add shift, else subtract shift
def caesar(text, shift, direction):
    message = ""
    if direction == "decode":
        shift *= -1
    for idx in range(0,len(text)):
        if (text[idx] in alphabet):
            message += alphabet[alphabet.index(text[idx]) + shift]
        else:
            message += text[idx]
    print(f"The {direction}d message is: '{message}'")
    
        

print(logo)
restart = True
# Keep asking user if they want to continue program
while restart: 
    # First ask user wether they want to decode or encode a message as well as the shift numnber,
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % 26
    caesar(text, shift, direction)
    startOver = input("Type 'yes' if you want to go again. Otherwise, type 'no' ")
    # If user does not want to continue, exit here
    if startOver == "no":
        restart = False
        print("Goodbye")


        


