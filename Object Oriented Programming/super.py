class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduction(self):
        print(self.name)

class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa

class Teacher(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

myStudent = Student("Noah", 24, "IS303")

myStudent.introduction()