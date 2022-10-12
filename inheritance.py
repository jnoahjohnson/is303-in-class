class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old")

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    
    def introduction(self):
        super().introduction()
        print("I am majoring in " + self.major)
        
    def switchMajor(self, newMajor):
        print("I am switching my major from " + self.major + " to " + newMajor)
        self.major = newMajor

newStudent = Student("Noah", 24, "Information Systems")
newStudent.introduction()
# Output: 
#   Hello, my name is Noah and I am 24 years old
#   I am majoring in Information Systems


class Book():
    def __init__(self, title, author, pages):
        # Public Attributes
        self.title = title
        self.author = author
        self.pages = pages

newBook = Book("The Hobbit", "J.R.R. Tolkien", 295)
print(newBook.title)
# Output: The Hobbit
