# Description: Output in python
# Name: Noah Johnson
teamMotto = "Win"
print(teamMotto * 3)

sPronoun = "I"
sVerb = "want"
sNoun = "candy"
print(sPronoun, sVerb, sNoun, sep = "-", end = "!" )

print("{0}, {1}, {2}".format("John", "Doe", 20))
print("{last}, {first} is {age} years old".format(first="John", last="Doe", age=20))

sFirst = "John"
sLast = "Doe"
iAge = 20
print("{last}, {first} is {age} years old".format(first=sFirst, last=sLast, age=iAge))

sFirst = "John"
sLast = "Doe"
iAge = 20
print(f'{sLast}, {sFirst} is {iAge} years old')