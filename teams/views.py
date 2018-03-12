from django.shortcuts import render
from .models import Team
from random import randint

# Create your views here.

def home(request):
    return render(request, 'teams/home.html')

def midwestTeams():
    teams = []
    teams.append(Team(rank=1, name='Virginia', region='midwest'))
    teams.append(Team(rank=16, name='UMBC', region='midwest'))
    teams.append(Team(rank=8, name='Creighton', region='midwest'))
    teams.append(Team(rank=9, name='Kansas St.', region='midwest'))
    teams.append(Team(rank=5, name='Kentucky', region='midwest'))
    teams.append(Team(rank=12, name='Davidson', region='midwest'))
    teams.append(Team(rank=4, name='Arizona', region='midwest'))
    teams.append(Team(rank=13, name='Buffalo', region='midwest'))
    teams.append(Team(rank=6, name='Miami (fla.)', region='midwest'))
    teams.append(Team(rank=11, name='Loyola Chicago', region='midwest'))
    teams.append(Team(rank=3, name='Tennessee', region='midwest'))
    teams.append(Team(rank=14, name='Wright State', region='midwest'))
    teams.append(Team(rank=7, name='Nevada', region='midwest'))
    teams.append(Team(rank=10, name='Texas', region='midwest'))
    teams.append(Team(rank=2, name='Cincinnati', region='midwest'))
    teams.append(Team(rank=15, name='Georgia State', region='midwest'))
    return teams

def westTeams():
    teams = []
    teams.append(Team(rank=1, name='Villanova', region='west'))
    teams.append(Team(rank=16, name='LIUB/RAD', region='west'))
    teams.append(Team(rank=8, name='Virginia Tech', region='west'))
    teams.append(Team(rank=9, name='Alabama', region='west'))
    teams.append(Team(rank=5, name='West Virginia', region='west'))
    teams.append(Team(rank=12, name='Murray State', region='west'))
    teams.append(Team(rank=4, name='Wichita State', region='west'))
    teams.append(Team(rank=13, name='Marshall', region='west'))
    teams.append(Team(rank=6, name='Florida', region='west'))
    teams.append(Team(rank=11, name='SBU/UCLA', region='west'))
    teams.append(Team(rank=3, name='Texas Tech', region='west'))
    teams.append(Team(rank=14, name='SFA', region='west'))
    teams.append(Team(rank=7, name='Arkansas', region='west'))
    teams.append(Team(rank=10, name='Butler', region='west'))
    teams.append(Team(rank=2, name='Purdue', region='west'))
    teams.append(Team(rank=15, name='CSU Fullerton', region='west'))
    return teams

def eastTeams():
    teams = []
    teams.append(Team(rank=1, name='Xavier', region='east'))
    teams.append(Team(rank=16, name='NCC/TSU', region='east'))
    teams.append(Team(rank=8, name='Missouri', region='east'))
    teams.append(Team(rank=9, name='Florida State', region='east'))
    teams.append(Team(rank=5, name='Ohio St.', region='east'))
    teams.append(Team(rank=12, name='South Dakota St.', region='east'))
    teams.append(Team(rank=4, name='Gonzaga', region='east'))
    teams.append(Team(rank=13, name='UNCG', region='east'))
    teams.append(Team(rank=6, name='Houston', region='east'))
    teams.append(Team(rank=11, name='San Diego State', region='east'))
    teams.append(Team(rank=3, name='Michigan', region='east'))
    teams.append(Team(rank=14, name='Montana', region='east'))
    teams.append(Team(rank=7, name='Texas A&M', region='east'))
    teams.append(Team(rank=10, name='Providence', region='east'))
    teams.append(Team(rank=2, name='North Carolina', region='east'))
    teams.append(Team(rank=15, name='Lipscomb', region='east'))
    return teams

def southTeams():
    teams = []
    teams.append(Team(rank=1, name='Kansas', region='south'))
    teams.append(Team(rank=16, name='Penn', region='south'))
    teams.append(Team(rank=8, name='Seton Hall', region='south'))
    teams.append(Team(rank=9, name='NC State', region='south'))
    teams.append(Team(rank=5, name='Clemson', region='south'))
    teams.append(Team(rank=12, name='New Mexico St.', region='south'))
    teams.append(Team(rank=4, name='Auburn', region='south'))
    teams.append(Team(rank=13, name='Charleston', region='south'))
    teams.append(Team(rank=3, name='TCU', region='south'))
    teams.append(Team(rank=14, name='ASU/SYR', region='south'))
    teams.append(Team(rank=6, name='Michigan St.', region='south'))
    teams.append(Team(rank=11, name='Bucknell', region='south'))
    teams.append(Team(rank=7, name='Rhode Island', region='south'))
    teams.append(Team(rank=10, name='Oklahoma', region='south'))
    teams.append(Team(rank=2, name='Duke', region='south'))
    teams.append(Team(rank=15, name='Iona', region='south'))
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
