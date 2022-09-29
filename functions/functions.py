from grades import get_letter_grade

is303 = int(input("What is your IS 303 grade? (0-100) "))
letterGrade = get_letter_grade(is303)

is201 = int(input("What is your IS 201 grade? "))
is201Letter = get_letter_grade(is201)

print("IS303: ", letterGrade)
print("IS201:", is201Letter)

def sum(num1, num2):
    return num1 + num2

sum = lambda num1, num2 : num1 + num2

print(sum(1, 2))