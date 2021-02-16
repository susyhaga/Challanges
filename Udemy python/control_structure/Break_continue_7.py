# Create a function that will roll a 6-number dice. 
# If it is odd, continue. If it is even and equal to the number drawn by the function given, print "Well done". 
# Then call the break. If you don't get the number drawn, call the else and print "You have failed"

from random import randint


def dice_game():
    return randint(1,6)
    
for i in range (1, 7):
    if i % 2 == 1:
        continue

    if dice_game() == i:
        print("Well done!", i)
        break
else:
    print("You have failed")