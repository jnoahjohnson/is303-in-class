# Get information about amusement park attractions
# Author: Noah Johnson

# Wait until the user is ready
userIsReady = input("Are you ready (y/n)? ")

while userIsReady.lower() != "y":
    print("Okay... :(")
    userIsReady = input("Are you ready now (y/n)? ")
else:
    print("You are ready")

# Ask user how many attractions
numAttractions = int(input("How many attractions are there? "))

for attractionsNum in range(1, numAttractions + 1):
    # Ask for name of attraction
    attractionName = input(f"What is the attraction {attractionsNum} name? ")

    # Ask for the type of attraction
    attractionType = input("What is the type? ")

    # Ask for num people on waitlist
    numPeople = int(input("How many people are on the waitlist? "))
    for personNum in range(numPeople):
        personName = input("What is the person's name? ")
    
    # Output - <name> - <type> - <num people> on waitlist
    print("{0} - {1} - {2} people on waitlist".format(attractionName, attractionType, numPeople))

