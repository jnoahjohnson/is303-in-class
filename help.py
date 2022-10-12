#Naomy Sanchez
# Who will Win the womens soccor tournament
# SoccerTeam Class
# team scores range / random number#random number 1-10
from itertools import count
from operator import truediv
from pickle import TRUE
import random
myTeamScore = random.randrange(1,11)
OpponentScore = random.randrange(1,11)
# inputs, insert main team and games inthe season
myTeam = input ("Enter your team you hope to win and keep track of: ")
iHowManyGames = int(input("How many games per season?: "))
GoalsAllowed = OpponentScore
wins = 0
gameLost = 0
mypoints = 0
GoalsAllowed = 0
class soccerTeam ():
    # tem constrocter
    def __init__(self,TeamName, wins, gameLost, myTeamScore, GoalsAllowed):
        self.TeamName = TeamName
        self.wins = wins
        self.gameLost = gameLost
        self.GoalsScored = myTeamScore
        self.GoalsAllowed = GoalsAllowed
# second = meathod
    def seasonStatus(self):
    # wins preformance over 75%
        if (self.wins /(self.wins + self.gameLost)) >= (75/100) :
            return(" NCAA Woman's Soccer Tournament" )
     # wins preformance over 50%
        elif (self.wins/(self.wins + self.gameLost)) >= (50/100) :
            return (" You Had a Good Season ")
     # poor game preformance / under 50% wins
        else :
            return(" Your team needs to practice ")
#object - unique team based on the template
# reference
# wins,lost and tie logic
tie = (OpponentScore == myTeamScore)
#loop- who won per game based on inputs
for iHowManyGames in range(0,iHowManyGames):
    Opponent = input("Name Next Opponent: ")
    myTeamScore = random.randrange(1,11)
    OpponentScore = random.randrange(1,11)
            # tie logic - random number 1-10
    while  OpponentScore == myTeamScore :
            myTeamScore = random.randrange (1,11)
            OpponentScore = random.randrange (1,11)
#wins
    if myTeamScore > OpponentScore :
        print("Yes, " + myTeam + " won! let's celebrate! ")
        print(str(myTeamScore))
        wins = wins + 1
        mypoints = myTeamScore
    else :
            print("oh no maybe " + myTeam + " will win next time. ")
            print( Opponent + " scored " + str(OpponentScore))
            gameLost = gameLost + 1
            GoalsAllowed = OpponentScore
# print results from my team
print ( " "+ myTeam )
print ( str(mypoints)+ " - "+ str(GoalsAllowed))
# input myteam score wins and lostgames
print(str(wins) +" - "+ str(gameLost))
# print preformance
myTeam = soccerTeam( myTeam, wins, gameLost, myTeamScore, GoalsAllowed)
print(myTeam.seasonStatus())