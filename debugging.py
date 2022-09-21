import datetime

## Example of a syntax error
# datetime.date().today()
today = datetime.date.today()

currentYear = today.year

# Example of a runtime error
# not having an int
userBirthYear = int(input("What year were you born? "))

userAge = currentYear - userBirthYear

birthYear = datetime.date(userBirthYear, 1, 1)

dateDiff = today - birthYear

# Exmaple of a logic error - Not the correct year born
print("You are", dateDiff.days / 365, "years old!")


myGrade = 10
hasDeduction = True

if hasDeduction:
    myGrade -= 10

finalScore = 100 / myGrade