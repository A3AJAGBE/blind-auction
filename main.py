"""
A secret auction application
"""

from logo import logo
import os

# Default displays
print(logo)
print('Each bids will be hidden')


# To prevent bidders from seeing bids different from theirs
def clear():
    os.system('clear')


# Keep the different bids in a dictionary
bids = {}

# User prompts
name = input("What is your name?\n").title()
price = int(input("How much are you bidding?\n€"))

# Add the input to the dictionary
bids[name] = price

# Prompt for another user
another_bid = input("Is there a new bid? Type 'Yes' or 'No'. \n").title()

# Verify the input
if another_bid == 'Yes':
    clear()
elif another_bid == 'No':
    print('NO more')
else:
    print("Invalid Input")
