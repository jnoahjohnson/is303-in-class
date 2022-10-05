class Movie():
    def __init__(self, title, director, ageRating):
        # Title, Director, Age Rating, User Score, Is In Theaters
        self.title = title
        self.director = director
        self.ageRating = ageRating
        self.userScore = 0
        self.isInTheaters = False
    
    def getDescription(self):
        # "<title> was directed by <director> and has a rating of <userScore>"
        return self.title + " was directed by " +  self.director + " and has a rating of " + str(self.userScore)
    
    def addToTheater(self):
        self.isInTheaters = True

myMovie = Movie("Dune", "Denis Villenue", "PG-13")
print(myMovie.title)

print(myMovie.getDescription())

myMovie.addToTheater()
print(myMovie.isInTheaters)

# Loop and get user ratings

# How many users?
numUsers = int(input("How many users rated the movie? "))
totalRating = 0

for user in range(numUsers):
    userRating = float(input("What is your rating of the movie? "))
    totalRating += userRating

averageRating = totalRating / numUsers
myMovie.userScore = averageRating

print(myMovie.getDescription())