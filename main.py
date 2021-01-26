"""
A secret auction application
"""

from logo import logo
import os


# To prevent bidders from seeing bids different from theirs
def clear():
    os.system('clear')


# Keep the different bids in a dictionary
bids = {}


# Check the bid with the highest price
def highest_bid(bids_dict):
    max_bid = 0
    winner = ""
    for bid_name in bids_dict:
        bid_price = bids_dict[bid_name]
        if bid_price > max_bid:
            max_bid = bid_price
            winner = bid_name
    print(f'The winner is "{winner}" with a bid of €{max_bid}\n')
    print(' ❌ THE AUCTION IS OVER ❌ ')


bidding_over = False
while not bidding_over:
    # Default displays
    print(logo)
    print('IMPORTANT:\nThe bids will be hidden only the winner will be declared.\n')

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
        highest_bid(bids)
        bidding_over = True
    else:
        clear()
        print("Invalid Response, Bid again the auction is still on-going.\n")
