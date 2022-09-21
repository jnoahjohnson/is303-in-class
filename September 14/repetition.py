# # Repetition in Python
# # Noah Johnson

# # While loops
# # While loops are similar to for loops, but they are used when you don't know how many times you want to repeat something.
# # For example, if you want to keep asking the user for input until they give you the right answer, you can use a while loop.
# # The while loop will keep repeating until the condition is no longer true.

# # Let's say we want to keep asking the user for input until they give us the right answer.
# # We can do this with a while loop.

# # We'll start by setting a variable to False.
# numTimes = 1

# while numTimes <= 10:
#     print(f"This loop has run {numTimes} times.")
#     numTimes += 1

# numTimes = 1

# while numTimes <= 10:
#     if numTimes % 2 == 0:
#         print("{0} is even.".format(numTimes))
#     else:
#         print("{0} is odd.".format(numTimes))
    
#     numTimes += 1

# # We can also use a while loop to keep asking the user for input until they give us the right answer.
# userIsReady = input("Are you ready? (y/n): ")

# while userIsReady != "y":
#     print("Okay, let's wait a bit...")
#     userIsReady = input("Are you ready? (y/n): ")
# else:
#     print("Let's go!")

# # Breaks and continues

# userAnswer = input("Would you like to continue? (y/n) ")
# while userAnswer == "y":
#     print("Continuing...")

#     anotherAnswer = input("What is your favorite data type? ")

#     if anotherAnswer.upper() == "QUIT":
#         break
#     else:
#         print("Good answer")

#     userAnswer = input("Enter Y or N: ")
# else:
#     print("Exiting...")


# sAnswer = input("Do you want to enter a student name?").upper()
# while (sAnswer == "Y") :
#     sFullName = input("Enter the student name: ")
#     fGPA = float(input("Enter the " + sFullName + "'s GPA: "))
#     if (fGPA == 0) :
#         continue
#     print(sFullName, "has a GPA of", fGPA)
#     sAnswer = input("Do you want to enter a student name?").upper()
# print("Thank you")



# Fo Loops
# For loops are used when you know how many times you want to repeat something.
# For example, if you want to print out the numbers 1 through 10, you can use a for loop.

# for iCount in range(10):
#     print(iCount)

# for iCount in range(0, 10):
#     print(iCount)

# for iCount in range(0, 10, 2):
#     print(iCount)

# numTeams = int(input("How many teams are there? "))
# for i in range(numTeams):
#     teamName = input(f"Enter the name of team {i}: ")
#     print(f"Team {i} is called {teamName}.")
# else:
#     print("There are no more teams.")

# userName = input("Enter your name: ")
# for char in userName:
#     if char.upper() == "A":
#         pass
#     else:
#         print(char)

# # Nested loops
# # Nested loops are loops inside of loops.
# # For example, if you want to print out a multiplication table, you can use a nested loop.

# # Let's say we want to print out a multiplication table.
# # We can do this with a nested loop.

# # We'll start by using a for loop to print out the numbers 1 through 10.
# for i in range(1, 11):
#     # We'll use another for loop to print out the numbers 1 through 10.
#     for j in range(1, 11):
#         # We'll print out the product of i and j.
#         print("{0} x {1} = {2}".format(i, j, i * j))

for firstNum in range(1, 11):
    for secondNum in range(1, 11):
        print(f"{firstNum} x {secondNum} = {firstNum * secondNum}")


myNum = 1
while myNum <= 3:
    print(myNum)
    myNum += 1

for myNum in range(1, 4):
    print(myNum)