# Description: Get information about Women's Soccer record
# Author: Kinsee Nyland

# Repeat the Women's Soccer program logic.

# However, create a class called soccerTeam representing
# a soccer team with the attributes representing:

# Team Name
# Wins
# Losses
# Goals Scored
# Goals Allowed
 
# Your program should implement the soccerTeam class, 
# create an object, and load values into the attributes for the object.

# The class should have a constructor, the attributes 
# mentioned above, and a method called seasonStatus which returns 
# the season message based upon the winning percentage as described 
# in the previously completed Women's Soccer program:

# IF the team has won at least 75% of their games then print out 
# “NCAA Women's Soccer Tournament”. If the team has won at least 50% 
# but less than 75% (you don't need to worry about an upper limit since 
# the first IF statement handles this) then print out “You had a good season”. 
# Otherwise print out “Your team needs to practice!”.

# Make sure the value returned from the method is then displayed
# (the method should NOT display but instead return the message).

# The goal of this assignment is to combine what you did in the original
#  Women's Soccer assignment with loops and input, and now use the 
# SoccerTeam class that you have now created.

# The logical flow will remain the same

# Ask the user for your soccer team name
# Ask for how many games they should play
# Loop through those games, calculating the scores of each 
# team (make sure there are no ties)
# Check to see if you won or lost
# The difference will be that your soccer team should now be an
#  instance of the SoccerTeam class and you will use that object to keep track of:

# Wins
# Losses
# Goals Scored
# Goals Allowed

# At the end of the program you will output the following data:

# Team Name

# Wins - Losses

# Goals Scored - Goals Allowed

# Team Status

# For example:

# BYU

# 3 - 1

# 8 - 2

# NCAA Women's Soccer Tournament

import random

class SoccerTeam():
    def __init__(self, teamName):
        self.teamName = teamName
        self.Wins = 0
        self.Loses = 0
        self.goalsScored = 0
        self.goalsAllowed = 0

    def seasonStatus(self):
        if self.Wins / (self.Wins + self.Loses) >= .75:
            return "NCAA Women's Soccer Tournament!"
        elif self.Wins / (self.Wins + self.Loses) >= .5:
            return "You had a good season!"
        else:
            return "Your team needs to practice!"

teamName = input("Team name?")
userTeam = SoccerTeam(teamName)

numGames = int(input("Enter amount of games: "))

for gameNumber in range(0, numGames):
    opponent = input("What is the opponent's name? ")
    myScore = random.randrange(0, 15)
    opponentScore = random.randrange(0, 15)
    while (myScore == opponentScore):
        myScore = random.randrange(0, 15)
        opponentScore = random.randrange(0, 15)
    if myScore > opponentScore:
        userTeam.Wins += 1
    else:
        userTeam.Loses += 1
    
    userTeam.goalsScored += myScore
    userTeam.goalsAllowed += opponentScore

print(userTeam.teamName)
print(str(userTeam.Wins) + " - " + str(userTeam.Loses))
print(str(userTeam.goalsScored) + " - " + str(userTeam.goalsAllowed))
print(userTeam.seasonStatus())