logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}

continue_bidding = True

def compare_bids(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"the winner is {winner} with a bid of {highest_bid}")

while continue_bidding:
    name = input("What is your Name?: ")
    price = int(input("What is your bid?: RS"))
    bids[name] = price
    should_continue = input("Are there any other bidders? 'yes' or 'no'. \n").lower()

    if should_continue == 'no':
        continue_bidding = False
        compare_bids(bids)
    elif should_continue == 'yes':
        print(" \n " * 30)



#using the max function
#example 
# fruits = {
#     "apple": 2,
#     "banana" : 4
#     "mango": 7
# }

# max(fruits, key=fruits.get) #this will give out the key with the max value which in this case is mango