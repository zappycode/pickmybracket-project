from django.shortcuts import render
from .models import Team
from random import randint

# Create your views here.

def home(request):
    return render(request, 'teams/home.html')

def midwestTeams():
    teams = []
    teams.append(Team(rank=1, name='MidWest', region='midwest'))
    teams.append(Team(rank=16, name='MidWest', region='midwest'))
    teams.append(Team(rank=8, name='MidWest', region='midwest'))
    teams.append(Team(rank=9, name='MidWest', region='midwest'))
    teams.append(Team(rank=5, name='MidWest', region='midwest'))
    teams.append(Team(rank=12, name='MidWest', region='midwest'))
    teams.append(Team(rank=4, name='MidWest', region='midwest'))
    teams.append(Team(rank=13, name='MidWest', region='midwest'))
    teams.append(Team(rank=3, name='MidWest', region='midwest'))
    teams.append(Team(rank=14, name='MidWest', region='midwest'))
    teams.append(Team(rank=6, name='MidWest', region='midwest'))
    teams.append(Team(rank=11, name='MidWest', region='midwest'))
    teams.append(Team(rank=7, name='MidWest', region='midwest'))
    teams.append(Team(rank=10, name='MidWest', region='midwest'))
    teams.append(Team(rank=2, name='MidWest', region='midwest'))
    teams.append(Team(rank=15, name='MidWest', region='midwest'))
    return teams

def westTeams():
    teams = []
    teams.append(Team(rank=1, name='West', region='west'))
    teams.append(Team(rank=16, name='West', region='west'))
    teams.append(Team(rank=8, name='West', region='west'))
    teams.append(Team(rank=9, name='West', region='west'))
    teams.append(Team(rank=5, name='West', region='west'))
    teams.append(Team(rank=12, name='West', region='west'))
    teams.append(Team(rank=4, name='West', region='west'))
    teams.append(Team(rank=13, name='West', region='west'))
    teams.append(Team(rank=3, name='West', region='west'))
    teams.append(Team(rank=14, name='West', region='west'))
    teams.append(Team(rank=6, name='West', region='west'))
    teams.append(Team(rank=11, name='West', region='west'))
    teams.append(Team(rank=7, name='West', region='west'))
    teams.append(Team(rank=10, name='West', region='west'))
    teams.append(Team(rank=2, name='West', region='west'))
    teams.append(Team(rank=15, name='West', region='west'))
    return teams

def eastTeams():
    teams = []
    teams.append(Team(rank=1, name='East', region='east'))
    teams.append(Team(rank=16, name='East', region='east'))
    teams.append(Team(rank=8, name='East', region='east'))
    teams.append(Team(rank=9, name='East', region='east'))
    teams.append(Team(rank=5, name='East', region='east'))
    teams.append(Team(rank=12, name='East', region='east'))
    teams.append(Team(rank=4, name='East', region='east'))
    teams.append(Team(rank=13, name='East', region='east'))
    teams.append(Team(rank=3, name='East', region='east'))
    teams.append(Team(rank=14, name='East', region='east'))
    teams.append(Team(rank=6, name='East', region='east'))
    teams.append(Team(rank=11, name='East', region='east'))
    teams.append(Team(rank=7, name='East', region='east'))
    teams.append(Team(rank=10, name='East', region='east'))
    teams.append(Team(rank=2, name='East', region='east'))
    teams.append(Team(rank=15, name='East', region='east'))
    return teams

def southTeams():
    teams = []
    teams.append(Team(rank=1, name='Kansas', region='south'))
    teams.append(Team(rank=16, name='Austin Peay', region='south'))
    teams.append(Team(rank=8, name='Colorado', region='south'))
    teams.append(Team(rank=9, name='UConn', region='south'))
    teams.append(Team(rank=5, name='Maryland', region='south'))
    teams.append(Team(rank=12, name='South Dakota State', region='south'))
    teams.append(Team(rank=4, name='California', region='south'))
    teams.append(Team(rank=13, name='Hawaii', region='south'))
    teams.append(Team(rank=3, name='Miami (FL)', region='south'))
    teams.append(Team(rank=14, name='Buffalo', region='south'))
    teams.append(Team(rank=6, name='Arizona', region='south'))
    teams.append(Team(rank=11, name='Witchita State', region='south'))
    teams.append(Team(rank=7, name='Iowa', region='south'))
    teams.append(Team(rank=10, name='Temple', region='south'))
    teams.append(Team(rank=2, name='Villanova', region='south'))
    teams.append(Team(rank=15, name='UNC Asheville', region='south'))
    return teams

def runGames(teams):
    winners = []
    for x in range(0, int(len(teams) / 2)):
        team1 = (teams[x*2].rank * -4) + randint(0,50)
        team2 = (teams[x*2 + 1].rank * -4) + randint(0,50)
        if team1 > team2:
            winners.append(teams[x*2])
        else:
            winners.append(teams[x*2 + 1])

    return winners


def results(request):
    # Get all teams from the south
    south = runRegion(southTeams(), 360, 427, -1)
    west = runRegion(westTeams(), 360, 164, -1)
    east = runRegion(eastTeams(), -415, 427, 1)
    midwest = runRegion(midwestTeams(), -415, 164, 1)

    leftWinner = runGames([east[0][0],midwest[0][0]])
    rightWinner = runGames([south[0][0],west[0][0]])
    champ = runGames([leftWinner[0],rightWinner[0]])

    teamsHTML = south[1] + west[1] + east[1] + midwest[1] + printTeamsInArray(leftWinner, -63, 352, 0, 6) + printTeamsInArray(rightWinner, 8, 482, 0, 6) + printTeamsInArray(rightWinner, -25, 416, 0, 7)
    return render(request, 'teams/results.html', {'teams':teamsHTML})

def runRegion(teams, startX, startY, leftOrRight):
    teamsHTML = printTeamsInArray(teams, startX, startY, 16.2, 1)
    round2teams = runGames(teams)
    teamsHTML += printTeamsInArray(round2teams, startX+(73*leftOrRight), startY+9, 32.8, 2)
    round3teams = runGames(round2teams)
    teamsHTML += printTeamsInArray(round3teams, startX+(142*leftOrRight), startY+25, 65.3, 3)
    round4teams = runGames(round3teams)
    teamsHTML += printTeamsInArray(round4teams, startX+(212*leftOrRight), startY+58, 131, 4)
    regionWinner = runGames(round4teams)
    teamsHTML += printTeamsInArray(regionWinner, startX+(282*leftOrRight), startY+124, 0, 5)
    return [regionWinner,teamsHTML]


def printTeamsInArray(teams, startX, startY, spacing, round):
    theHTML = ''
    for team in teams:
        theHTML += '<div class="teamThang round' + str(round) + '" style="display:none; position:absolute; left: 50%; margin-left: ' + str(startX) + 'px; top:' + str(startY) + 'px; z-index: 1;">' + str(team.rank) + ' ' + team.name + '</div>'
        startY += spacing
    return theHTML
