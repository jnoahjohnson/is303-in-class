# There are a lot of errors in here. Help me fix the program

def get_grade_value(grade):
    if grade == "A":
        return 4.0
    elif grade == "A-":
        return 3.7
    elif grade == "B+":
        return 3.4
    elif grade == "B":
        return 3.0
    elif grade == "B-":
        return 2.7
    elif grade == "C+":
        return 2.4
    elif grade == "C":
        return 2.0
    elif grade == "C-":
        return 1.7
    elif grade == "D+":
        return 1.4
    elif grade == "D":
        return 1.0
    elif grade == "D-":
        return 0.7
    elif grade == "E":
        return 0.0

overallGPA = float(input("What is your overall GPA? "))
last30GPA = float(input("What is your last 30 credits GPA? "))
accountingGrade = int(input("What is your Accounting 200 grade? "))
is201Grade = int(input("What is your IS 201 grade? "))
is303Grade = int(input("What is your IS 303 grade? "))
acc200Grade = int(input("What is your Accounting 200 grade? "))
essayScore = int(input("What is your essay score? "))

get_grade_value(is201Grade)
get_grade_value(is303Grade)
get_grade_value(acc200Grade)

newGPA = (acc200Grade * .05) + (is201Grade * .3) + (is303Grade * .3) + (overallGPA * .12) + (last30GPA * .18) + (essayScore * .05)
# Using the following logic, also display the message on a new line:
# GPA of 3.8 and above displays "Chances are very good"
# GPA of 3.5 and above displays "Chances are good"
# GPA of 3.2 and above displays "Chances are so-so"
# Otherwise display "You might want to retake IS 201 and/or IS 303"

if newGPA > 3.8:
    print("Chances are very good")
elif newGPA > 3.5:
    print("Chances are good")
elif newGPA > 3.2:
    print("Chances are so-so")
else:
    print("You might want to retake IS 201 and/or IS 303")
    

for dayOfWeek in range(7):
    print(dayOfWeek)