class Student():
    def __init__(self, name, age, gender, gpa, number):
        self.name = name
        self.age = age
        self.gender = gender
        self.gpa = gpa
        self.number = number

        self.numCredits = 0
    
    def studentStatus(self):
        if self.gpa > 3:
            return "Good job!"
        elif self.gpa > 2:
            return "You are getting there"
        else:
            return "Uh oh..."

firstStudent = Student("Noah", 24, "Male", 3.9, 123456)

firstStudent.numCredits += 10
print(firstStudent.numCredits)

myStatus = firstStudent.studentStatus()

if myStatus == "Good job!":
    print("Yay!")