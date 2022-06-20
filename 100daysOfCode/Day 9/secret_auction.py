from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.")

auction = {}

bidder = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
auction[bidder] = bid
while True:
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == 'no':
        break

    clear()
    bidder = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[bidder] = bid

max_bid = 0
max_bidder = None

for k, v in auction.items():
    if v > max_bid:
        max_bid = v
        max_bidder = k

print(f'The winner is {max_bidder} with a bid of ${max_bid}.')



