# 
# Noah Johnson

isReady = False

while not isReady:
    userIsReady = input("Are you ready? (y/n): ")

    if userIsReady == "y":
        isReady = True
    else:
        print("Okay, let's wait a bit...")
else:
    print("Let's go!")


numAttractions = int(input("How many attractions are there? "))

for i in range(numAttractions):
    print(i)