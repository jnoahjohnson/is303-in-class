# Description: Give ideas of activities based on the weather
# Author: Noah Johnson

# Please prompt the user for the current temperature outside and convert their input into an integer
from re import I


currTemp = int(input("What is the temperature outside? "))

# ask the user if it is raining and assign it to the variable isRaining
    # Make sure to tell the user to type either a y or n for yes or no.

isRaining = input("Is it raining (y/n)?")

# Do the same thing for isSnowing 
isSnowing = input("Is it snowing? ")

# Do the same thing for isWindy
isWindy = input("Is it windy? ")

# If it is 90 degrees or more, check to see if it is raining. 
#   If it is, suggest that the user put on rain boots and go jump in puddles. 
#   If it is not raining, tell the user to go swimming!
if currTemp >= 90:
    if isRaining.lower() == "y":
        print("Go put on rain boots and jump in puddles")
    else:
        print("Go swimming!")

# If it is between 60 and 89 degrees, check to see if it is windy. 
#   If it is, tell the user to fly a kite. 
#   If it is not, tell the user to go play spikeball (or another fun outdoor activity).
isWindy = isWindy.lower() == "y"

# if isWindy.lower() == "y":
#     isWindy = True
# else:
#     isWindy = False

if currTemp >= 60 and currTemp <= 89:
    if isWindy:
        print("Fly a kite!")
    else: 
        print("Go play spikeball")

# If it is less than 60, check to see if it is snowing. 
#   If it is, tell the user to go sledding. 
#   If it is not, tell the user to make hot chocolate and play board games (or another fun indoor activity).
if currTemp < 60 and isSnowing.lower() == "y":
    print("Go sledding!")
elif currTemp < 60:
    print("Make hot chocolate and play board games")