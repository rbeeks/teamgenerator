import random
import os
import sys
import csv
from random import shuffle

class Player:
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

class Team:
    def __init__(self):
        self.players = []
    
    def __repr__(self):
        return '\n'.join(["Team Name (" + str(self.get_skill()) + ")"] + ["- " + player.name for player in self.players] + [""])

    def get_skill(self):
        return sum([p.get_stats() for p in self.players])

def arrange_teams(players):
    team1=Team()
    team2=Team()
    shuffle(players)

    for player in players:
        if team2.get_skill() > team1.get_skill():
            team1.players.append(player)
        else:
            team2.players.append(player)

    return team1, team2

   
def read_players(filename = 'players.csv'):
    with open(filename, 'r') as f:
        csv_file = csv.reader(f)
        try:           
            return [Player(line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5])) for line in csv_file if not line[0].startswith("#")]
        except:
            print("Incorrectly formatted csv")
            sys.exit()


players = read_players()

while True:
    [team1, team2] = arrange_teams(players)
    if (abs(team1.get_skill() - team2.get_skill()) < 30): break

print team1
print team2