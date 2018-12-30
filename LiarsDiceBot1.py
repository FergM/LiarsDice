import numpy as np

print("\n\nSTART GAME-------------:")

#-------------------Internal Values
Dice = 5 #Number of Dice per Human

#-------------------Roll The Dice
Human_Dice   = np.random.randint(1,7,size= Dice) #Draws 1 to (7-1) inclusive
Computer_Dice = np.random.randint(1,7,size= Dice)
print("Your numbers are: ", Human_Dice)

#-------------------Ask Human to Bid
print("Please input your bid.")
BidQty = int(input("Quantity: "))
BidVal = int(input("Face Value: "))
Bidder = "Human"

#Basic Error Checking
if BidQty < 0:
    raise Exception("Bid Quantity can't be negative.")

if (BidVal < 1) or (BidVal > 6):
    raise Exception("Bid value must be an integer from 1 to 6.")

#-------------------Evaluate Computer's hand
#Find Value with most Occurences in Computer's Hand
HandBincount = np.bincount(Computer_Dice, minlength = 6+1)
HandOnes  = HandBincount[1] #Count ccurences of #1 in Computer's Hand
print("DEBUGPRINT HandBincount>", HandBincount)
HandBincount[1] = 0         #Clear #1 rolls from bincount.
                            #Because #1 is a wildcard in this game
print("DEBUGPRINT HandBincount>", HandBincount)
HandModeVal   = HandBincount.argmax() #Dice value which occurs most in computer's Hand
HandModeQty   = HandBincount[HandModeVal] #Qty = Number of occurences
HandBidQty = HandBincount[BidVal] #Occurences of the bid # in computer's hand

#DEBUGPRINT HAND
print("\n DEBUG PRINT 1-------------:")
print("Computer Dice:", Computer_Dice)
if Bidder == "Human":
    print("Human has bid ", BidQty  , " ", BidVal, "'s.")
else:
    raise Exception("Expected Bidder = 'Human' at this point.")
print("Computer holds ", HandBincount[BidVal], " ", BidVal, "'s.")
print("Computer holds ", HandOnes, "  1's.")
print("Computer holds ", HandBidQty + HandOnes, " (1's & ", BidVal, "'s.)")
print("END DEBUG PRINT-------------:")

#-------------------Evaluate Computer's Options
#Calculate Cost Functions for Each CounterBid Option

OutOfHandE = Human_Dice.size * 1/3 #Out of Hand Quantity Expectation

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

#DEBUGPRINT OPTIONS
print("\n DEBUG PRINT 2-------------:")
print("Out of hand Expectation = ", OutOfHandE)
print(" Reject_Cost = ", Reject_Cost)
print(" RaiseVal_Cost = ", RaiseVal_Cost)
print(" RaiseQty_Cost = ", RaiseQty_Cost)
print("END DEBUG PRINT-------------:\n")
input("Press ENTER to Continue. Ctrl-C to Abort.")

#-------------------Select CounterBid
BidOptions = {'Reject': Reject_Cost, 'RaiseVal': RaiseVal_Cost, 'RaiseQty': RaiseQty_Cost}
action = min(BidOptions, key=BidOptions.get) #Action = option with lowest cost
print("Computer chooses to", action)

if action != "Reject":
    Bidder = "Computer"
    print("DEBUGPRINT Bidder = ", Bidder)
    #INSERT HERE: value of bid if RaiseVal or RaiseQty
elif action == "Reject":
    Bidder = "Human"
    print("DEBUGPRINT Bidder = ", Bidder)

#------------------Determine if Bidder Wins or Loses

#If ~HandBincount[BidVal] + HumanBincount[BidVal] >= BidQty
#   Bidder wins
#else
#   Bidder Loses

#---------------------------------------------------
#Bot2v
#Then:
#Make a Loop on Human Bid / Computer Bid (on paper first)
#   Once computer makes it's bid Add: Raise bid? (Y/N)
#   Exit the loop if someone Rejects a Bid.
#       While HumanRejects == False and ComputerRejects == False
#       e.g. a == 2 and b == 3
#Once someone rejects a bid:
#   Evaluate if it wins by counting
#   Print out "BidderName" Wins OR "BidderName" Loses.
