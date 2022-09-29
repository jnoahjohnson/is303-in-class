# Description: Comparison Operators in Python
# Author: Noah Johnson

# Equal to
num1 = 5
num2 = 10
print(num1 == num2)

# Not equal to
num1 = 5
num2 = 10
print(num1 != num2)

# Greater than
num1 = 5
num2 = 10
print(num1 > num2)

# Less than
num1 = 5
num2 = 10
print(num1 < num2)

# Greater than or equal to
num1 = 5
num2 = 10
print(num1 >= num2)

# Less than or equal to
num1 = 5
num2 = 10
print(num1 <= num2)

# Boolean Logic

# And
num1 = 5
num2 = 10
print(num1 == 5 and num2 == 10)

# Or
num1 = 5
num2 = 10
print(num1 == 5 or num2 == 5)

# Not
num1 = 5
num2 = 10
print(not num1 == 5)

# If Statements
myGrade = 80
if myGrade >= 90:
    print("A")

# If/Else Statements
myGrade = 80
if myGrade >= 90:
    print("A")
else:
    print("F")

# If/Elif/Else Statements
myGrade = 80
if myGrade >= 90:
    print("A")
elif myGrade >= 80:
    print("B")
else:
    print("F")

# Logical Operators
myGrade = 80
if myGrade >= 90 and myGrade <= 100:
    print("A")
elif myGrade >= 80 and myGrade < 90:
    print("B")
else:
    print("F")

# AND

myGrade = 80
hasExtraCredit = True
if hasExtraCredit and myGrade >= 80:
    print("A")

# OR

isRaining = False
isSnowing = False
if isRaining or isSnowing:
    print("Stay home")
else:
    print("Go to the beach")

# NOT
temperature = 75
isRaining = True

if temperature >= 70 and not isRaining:
    print("Go to the beach")
else:
    print("Stay home")

# Nested If Statements
temperature = 75
isRaining = True

if temperature >= 70:
    if isRaining:
        print("Stay home")
    else:
        print("Go to the beach")
else:
    print("Stay home")

myGrade = 80.5
if myGrade > 90:
    print("Congrats, you have an A")
elif myGrade >= 80:
    print("You have a B in the class")
else:
    print("You don't have an A")


myGrade = 90
hasExtraCredit = True

if hasExtraCredit or myGrade >= 90:
    print("You are a fantastic student")
else: 
    print("You are still fantastic")