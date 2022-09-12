# Description: Weather in Python
# Author: Noah Johnson

# Ask for the current temperature
currTemp = int(input("What is the current temperature? "))

# Ask if it is raining
isRaining = input("Is it raining? (y/n) ")

# Convert isRaining to a boolean
if isRaining.lower() == "y":
    isRaining = True
else:
    isRaining = False

# Ask if it is snowing
isSnowing = input("Is it snowing? (y/n) ")

# Convert isSnowing to a boolean
if isSnowing.lower() == "y":
    isSnowing = True
else:
    isSnowing = False

# Ask if it is windy
isWindy = input("Is it windy? (y/n) ")

# Convert isWindy to a boolean
if isWindy.lower() == "y":
    isWindy = True
else:
    isWindy = False

if currTemp >= 80:
    if isRaining:
        # Tell the user to do an activity
        print("Put on boots and dance in the rain")
    else:
        print("Go swimming")
elif currTemp >= 60:
    if isSnowing:
        print("Go skiing")
    else:
        print("Go hiking")
else:
    if isWindy:
        print("Go kite flying")
    else:
        print("Go sledding")


       
