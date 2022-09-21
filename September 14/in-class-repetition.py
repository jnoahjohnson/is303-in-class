# In class repetition
# Noah Johnson

# myNum = 1

# while myNum <= 10:
#     myNum += 1

#     if myNum % 2 == 0:
#         pass
#     else:
#         break

    # print(myNum) 
    
# userInput = input("Would you like to continue (y/n)? ")

# while userInput != "y":
#     print("Okay, we will wait for you...")
#     userInput = input("Would you like to continue (y/n)? ")

#     if userInput.lower() == "quit":
#         break

# range(<startNumber>, <endNumber>)
# range(<endNumber>)
# range(<startNumber>, <endNumber>, <increment>)

# for myNum in range(10, 0, -1):
#     print(myNum)

numTeams = int(input("How many teams do you want to input? "))

for teamNum in range(1, numTeams + 1):
    print(f"Team {teamNum}")