from logo import logo
import os

# This day's project tested my knowledge of python dictionaries to create a highest bidding system.
print(logo)
bidders = {}


# Add bidder's info to dictionary
def addBidderInfo(bidderName, bidderAmount):
    bidders[bidderName] = int(bidderAmount)


# Find highest bidder
def findHighestBidder():
    highestBid = 0
    highestBidder = ""
    for key in bidders:
        if bidders[key] > highestBid:
            highestBidder = key
    print(f"{highestBidder} has won the bid with a bid amount of {bidderAmount}!")


# Repeatedly ask bidders for their name and bid amount until no bidders remain
otherBidderExists = True
while otherBidderExists:
    bidderName = input("What's your name?: ")
    bidderAmount = input("What's your bid?: ")
    addBidderInfo(bidderName, bidderAmount)
    continueBid = input("Are there any other bidders? Type 'yes' or 'no': ")
    if continueBid == "no":
        otherBidderExists = False
    else:
        os.system('clear')

findHighestBidder()
