from art import logo
from replit import clear
#HINT: You can call clear() to clear the output in the console.
print(logo)

continue_bid = True  #flag to check continuation
master_DB = {}  #declare an empty dictionary 
max_value = 0  #saves the max value of all time
max_bidder = ""  #variable to save name of maximum bidder

#declare function to add input values to dictionary
def add_bid(name, bid):
  master_DB[user_name] = bid_input

while continue_bid:
  #taking input from user
  user_name = input("\nPlease enter your name: ")
  bid_input = int(input("\nPlease enter your bid: ₹"))
  add_bid(user_name, bid_input)  #call function 

  #take input whether user want to continue bidding
  continue_response = input("\nAny other tycoon wants to bid? Y or N: ")

  #checking for valid input
  if continue_response == "Y" or continue_response == "N":
      if continue_response == "N":
        continue_bid = False  #stop bidding and start analysing inputs
        for key, value in master_DB.items():  #read multiple values 

          #compare values and store max value to variable
          if max_value == 0 or value > max_value:
            max_value = value
            max_bidder = key

        #final O/P
        if max_value != 0:
          print(f"\nThe winner is {max_bidder} with a bid of ₹{max_value} 🎊")
      else:
        #continue bidding 
        clear()
  else:
    print("\nInvalid input!")
    break
