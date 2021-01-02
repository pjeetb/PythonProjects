from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

#printing the logo importing from art module.
print(logo)
bids ={}    #declaring an empty dictionary to store the bid details.
bidding_finished = False #setting it false to run the while loop.

def highest_bidder(bidding_record):   #will check who is the highest bidder 
  highest_amount = 0
  winner =""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]  #storing the value from the key.
    if bid_amount > highest_amount:      #checking the value with highest var.
      highest_amount = bid_amount       #updating the current highest_amount. 
      winner = bidder                    #storing the key.
  print(f"{winner} has won the aution with a Bid of ${highest_amount}")

while not bidding_finished:              #loop will run until the cond is true.
  name= input("What is your name: ")    #accepting user inputs.
  bid = int(input("What is your price bid $")) #converting to int in acceptance.
  bids[name] = bid   #storing user/inputs to empty dictionary in key & value.
  
  choice=input("Are there are any bidders? Yes or No: ").lower() #asking input & converting to lower case.
  if choice == "no":
    bidding_finished = True      #if choice is no, while loop will exit.
    highest_bidder(bids)         #calling func to calculate the highest bidder.
  
  elif choice == "yes":          #clearing the screen & continuing while loop.
    clear()
