# Template
class Book():
    publisher = "TOR" # Class Variable (Attribute)

    # Constructor - 3 parameters (and self)
    def __init__(self, title, author, rating):
        # Instance Variables (Attributes)
        self.title = title
        self.author = author
        self.rating = rating

        # Scoping
        # self.title is the attribute and scoped to the instance
        # title is the parameter and is scoped to the constructor

    # Method - Remember self!
    def getDescription(self):
        return self.title + " was written by " + self.author

    # Method - One parameter, but also remember self!
    def addReview(self, reviewScore):
        newRating = (self.rating + reviewScore) / 2
        self.rating = newRating

# Creating an Object from the Book Class (Template)
bestBook = Book("The Way of Kings", "Brandon Sanderson", 4.9)

# Calling a method
bookDescription = bestBook.getDescription()
print(bookDescription)

# Calling a method with a parameter
bestBook.addReview(5.0)
print(bestBook.rating)
