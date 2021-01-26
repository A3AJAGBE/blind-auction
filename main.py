"""
A secret auction application
"""

from logo import logo

# Default displays
print(logo)
print('Each bids will be hidden')


# Keep the different bids in a dictionary
bids = {}

# User prompts
name = input("What is your name?\n").title()
price = int(input("How much are you bidding?\n€"))

# Add the input to the dictionary
bids[name] = price
