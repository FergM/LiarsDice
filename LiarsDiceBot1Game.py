import numpy as np

print("\n\nSTART GAME-------------:")

#-------------------Internal Values
Dice = 5 #Number of Dice per Player

#-------------------Roll The Dice
Andrew_Dice   = np.random.randint(1,7,size= Dice) #Draws 1 to (7-1) inclusive
Computer_Dice = np.random.randint(1,7,size= Dice)
print("Your numbers are: ", Andrew_Dice)

#-------------------Ask Andrew to Bid
print("Please input your bid.")
BidQty = int(input("Quantity: "))
BidVal = int(input("Face Value: "))
Bidder = "Andrew"

#Basic Error Checking
if BidQty < 0:
    raise Exception("Bid Quantity can't be negative.")

if (BidVal < 1) or (BidVal > 6):
    raise Exception("Bid value must be an integer from 1 to 6.")
#-------------------Evaluate Each Player's hand
AndrewBincount = np.bincount(Andrew_Dice, minlength = 6+1) #For 6 sided Dice
ComputerBincount = np.bincount(Computer_Dice, minlength = 6+1)

#-------------------Evaluate Computer's hand
#Find Value with most Occurences in Computer's Hand
HandBincount = np.bincount(Computer_Dice, minlength = 6+1)
HandOnes  = HandBincount[1] #Count ccurences of #1 in Computer's Hand

HandBincount[1] = 0         #Clear #1 rolls from bincount.
                            #Because #1 is a wildcard in this game
HandModeVal   = HandBincount.argmax() #Dice value which occurs most in computer's Hand
HandModeQty   = HandBincount[HandModeVal] #Qty = Number of occurences
HandBidQty = HandBincount[BidVal] #Occurences of the bid # in computer's hand

if Bidder == "Andrew":
    print("Andrew has bid ", BidQty, BidVal, "'s.")
else:
    raise Exception("Expected Bidder = 'Andrew' at this point.")

#-------------------Evaluate Computer's Options
#Calculate Cost Functions for Each CounterBid Option
OutOfHandE = Andrew_Dice.size * 1/3 #Out of Hand Quantity Expectation

#Reject Bid
Reject_Cost   = (OutOfHandE + HandOnes + HandBidQty ) - BidQty

#Bid up Value (Without increasing BidQty)
if HandModeVal > BidVal:
    RaiseVal_Cost = BidQty - (OutOfHandE + HandOnes + HandModeQty )
else: #Else we can't change BidValue to HandModeQty unless we raise BidQty
    RaiseVal_Cost = Reject_Cost + 100

#Bid another Quantity (keep the same BidVal)
RaiseQty = BidQty + 1
RaiseQty_Cost = RaiseQty - (OutOfHandE + HandOnes + HandModeQty)

#-------------------Select CounterBid
BidOptions = {'Reject': Reject_Cost, 'RaiseVal': RaiseVal_Cost, 'RaiseQty': RaiseQty_Cost}
action = min(BidOptions, key=BidOptions.get) #Action = option with lowest cost
print("\nComputer chooses to", action)

if action != "Reject":
    Bidder = "Computer"
    if action == "RaiseVal":
        BidVal = HandModeVal
    else: # action = "RaiseQty":
        BidVal = HandModeVal
        BidQty = BidQty + 1
else: #action == "Reject":
    Bidder = "Andrew"

#------------------Determine if Bidder Wins or Loses
AndrewBidQty = AndrewBincount[BidVal] + AndrewBincount[1]
ComputerBidQty = ComputerBincount[BidVal] + ComputerBincount[1]
print("Computer's numbers are: ", Computer_Dice)
print(f"\nFinal Bid by {Bidder} is {BidQty}, {BidVal}'s")

if BidQty <= (AndrewBidQty + ComputerBidQty):
    print(Bidder, "Wins!")
else:
    print(Bidder, "Loses")
