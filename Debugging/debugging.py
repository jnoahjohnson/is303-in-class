# Description: Calculate the user's age based on the year they were born
# Author: Noah Johnson
from datetime import datetime
import math

today = datetime.today()

userBirthYear = int(input("What year were you born? "))
userBirthMonth = int(input("What month were you born(1-12)? "))
userBirthDay = int(input("What day of the month were you born? "))

# dBirthday = datetime.strptime("12/01/2000", "%m/%d/%Y")
userDate = datetime.strptime(f"{userBirthMonth}/{userBirthDay}/{userBirthYear}", "%m/%d/%Y")

userAge = today - userDate

daysOld = userAge.days

print("You are", math.floor(daysOld / 365), "years old")