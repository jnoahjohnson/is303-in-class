# Description: Concatenating strings in Python
# Author: Noah Johnson

# Concatenation is the process of combining strings
# Concatenation is done using the + operator
# The + operator is called the concatenation operator
# The + operator takes two strings and returns a new string
# The + operator syntax is:
# string1 + string2

sFirstName = "George"
sLastName = "McFly"
sFullName = sLastName + "," + sFirstName
print(sFullName)

sFirstName = "George"
sLastName = "McFly"
iYearBorn = 1938
sFullName = sLastName + ", " + sFirstName
print(sFullName + " was born in " + iYearBorn)

sFirstName = "George"
sLastName = "McFly"
iYearBorn = 1938
sFullName = sLastName + ", " + sFirstName
print(sFullName,"was born in", iYearBorn)

firstName = input("What is your first name? ")
lastName = input ("What is your last name? ")
# fullName = "Noah Johnson"
fullName = firstName + " " + lastName

print(fullName, firstName, lastName)