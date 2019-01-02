#SINGLEBIDGAME.py: A Single Bid game of Liar's Dice.
import numpy as np

#-------------------Internal Parameters
Dice = 5 #Number of Dice per Player

#-------------------Roll The Dice
Andrew_Dice   = np.random.randint(1,7,size= Dice) #Draws 1 to (7-1) inclusive
Computer_Dice = np.random.randint(1,7,size= Dice)

#Calculate Summary Statistics
    #Bincounts
    AndrewBincount = np.bincount(Andrew_Dice, minlength = 6+1) #For 6 sided Dice
    ComputerBincount = np.bincount(Computer_Dice, minlength = 6+1)

    ComputerModeVal = ComputerBincount[2:(6+1)].argmax()+2 #we don't want to
    #count 1's because it's a wildcard.

###Temp (we care about:)
##HandModeVal   = HandBincount.argmax() #Dice value which occurs most in computer's Hand
##HandModeQty   = HandBincount[HandModeVal] #Qty = Number of occurences
##HandBidQty = HandBincount[BidVal] #Occurences of the bid # in computer's hand

#-------------------Ask Andrew to Bid
print("\n\nSTART GAME-------------:")
print("Your numbers are: ", Andrew_Dice)
print("Please input your bid.")
BidQty = int(input("Quantity: "))
BidVal = int(input("Face Value: "))
Bidder = "Andrew"

#Basic Error Checking
if BidQty < 0:
    raise Exception("Bid Quantity can't be negative.")

if (BidVal < 1) or (BidVal > 6):
    raise Exception("Bid value must be an integer from 1 to 6.")

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
