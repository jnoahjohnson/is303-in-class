class Team():
    def __init__(self, name):
        self.name = name
        self.wins = 0

def startTeam():
    teamName = input("What is your team name? ")

    team = Team(teamName)

    for num in range(10):
        team.wins += num

    return team

teamOne = startTeam()
teamTwo = startTeam()

print(teamOne.name, teamOne.wins)
print(teamTwo.name)