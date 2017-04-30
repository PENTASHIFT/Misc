"""
A script to roll a series of nine numbers like on *chan. Written in Python 3. 
Complete with fairly unhelpful commenting.

Date Created: March 4th, 2017
Edit: March 20th, 2017

"""

from random import randint

# How many rolls would you like?
print("Please enter how many rolls you'd like.")

while True:
   roll_num = input('> ')
   try:
      roll_num = int(roll_num)
      break
   except ValueError:
      print("Please enter a whole number.")
      continue

# Checking the last digits of rolls for repeating numbers. 
def checkRoll(roll):
    if(roll[-2] != roll[-1]):
        pass
    else:
        if(roll[-3] != roll[-1]):
            roll += ' Dubs'
        else:
             roll += ' Trips+'
    return roll

# Gets a set of nine random numbers for the roll.
def pseudoRoll():
    outpt = "\t- "
    for itr in range(9):
        rand = randint(0, 9)
        outpt += str(rand)
    return outpt

# Finally a for loop to put everything together.
for _ in range(roll_num):
    print(checkRoll(pseudoRoll()))
