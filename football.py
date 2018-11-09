import random
import os

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

players = [player("Greg", 15, 17, 12, 14, 12), player("Steve", 12, 12, 11, 11, 14), player("Mark", 11, 12, 12, 12, 12), player("Craig", 17, 12, 9, 11, 15), player("Bill", 17, 17, 18, 14, 18), player("John", 12, 13, 16, 12,16)]
array=[]

for i in range(0,len(players)):
    tmp=str(players[i].name) + ":" + str(players[i].get_stats())
    array.append(tmp)

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
