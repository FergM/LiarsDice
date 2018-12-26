print("Please input your bid.")
PlayerBidQty = int(input("Quantity: "))
PlayerBidVal = int(input("Face Value: "))

#-------------------------Basic Error Checking
if PlayerBidQty < 1:
    raise Exception("Bid Quantity can't be negative.")

if (PlayerBidVal < 1) or (PlayerBidVal > 6):
    raise Exception("Bid value must be an integer from 1 to 6.")

#-------------------------
