# Comparisons in Python
# Noah Johnson

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