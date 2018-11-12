import random
import os
import sys

class player:
    def __init__(self, name, shooting, passing, defending, goalkeeping, fitness):
        self.name = name

        self.stats = {
            "shooting": shooting,
            "passing": passing,
            "defending": defending,
            "goalkeeping": goalkeeping,
            "fitness": fitness
        }

    def get_stats(self):
        return sum(self.stats.values())

def arrange_teams(p):
    team1=[]
    team2=[]
    team1Count=0
    team2Count=0
    for i in range(0,len(p)):
        rand=random.randint(0,len(p)-1)
        tmpstring=p[rand].split(':')
        if team2Count > team1Count:
            team1.append(tmpstring[0])
            team1Count=team1Count+int(tmpstring[1])
            p.pop(rand)
        else:
            team2.append(tmpstring[0])
            team2Count=team2Count+int(tmpstring[1])
            p.pop(rand)
    return team1, team2, team1Count, team2Count

players = []
with open('players.csv', 'r') as f:
    playerfile=f.readlines()
    for i in range(0,len(playerfile)):
        fStats=playerfile[i].rstrip().split(',')
        if (len(fStats)!=6):
            print('Incorrectly formatted csv')
            sys.exit()
        players.append(player(fStats[0],int(fStats[1]),int(fStats[2]),int(fStats[3]),int(fStats[4]),int(fStats[5])))
    

array = [player.name + ":" + str(player.get_stats()) for player in players]

team1Skill=0
team2Skill=31
team1=[]
team2=[]

while (team2Skill-team1Skill)>abs(30):
    [team1, team2, team1Skill, team2Skill]=arrange_teams(array)


print team1
print team2
print team1Skill
print team2Skill
