class Student():
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        
    
    def getTopGrade(self):
        if self.gpa > 3:
            return "A"
        else:
            return "B"

    def studentStatus(self):
        if (self.getTopGrade() == "A"):
            return "You are awesome"
        else:
            return "You are still awesome"

myStudent = Student("Zack", 2)
print(myStudent.getTopGrade())
myStudent.gpa = 4
print(myStudent.studentStatus())