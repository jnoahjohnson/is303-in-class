class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Director(Person):
    def __init__(self, name, age, numOscars):
        super().__init__(name, age)
        self.numOscars = numOscars

    def introduction(self):
        print("My name is " + self.name + " and I have " + str(self.numOscars) + " oscars")

class Actor(Person):
    def __init__(self, name, age, starStatus):
        super().__init__(name, age)
        self.starStatus = starStatus


class Movie():
    def __init__(self, title, director, ageRating):
        # Title, Director, Age Rating, User Score, Is In Theaters
        self.title = title
        self.director = director
        self.ageRating = ageRating
        self.userScore = 0
        self.isInTheaters = False

        self.actors = []
    
    def getDescription(self):
        # "<title> was directed by <director> and has a rating of <userScore>"
        return self.title + " was directed by " +  self.director.name + " and has a rating of " + str(self.userScore)
    
    def addToTheater(self):
        self.isInTheaters = True

    def printActors(self):
        for actor in self.actors:
            print(actor.name)


movie = Movie("Avatar", Director("James Cameron", 65, 3), "PG-13")
print(movie.title)

movie.actors.append(Actor("Zoe Saldana", 45, "VERY MUCH A STAR"))
movie.actors.append(Actor("Sam Worthington", 45, "NOT VERY MUCH A STAR"))

movie.printActors()