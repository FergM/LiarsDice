import numpy as np

#Roll The Dice
Player_Dice   = np.random.randint(1,7,size=6) #Draws 1 to (7-1) inclusive
Computer_Dice = np.random.randint(1,7,size=6)
print("Your numbers are: ", Player_Dice)
