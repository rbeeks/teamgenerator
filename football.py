#!/usr/bin/python3
import sys
import csv
from random import shuffle
import names

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
        self.name = names.generate_team_name()
    
    def __repr__(self):
        return '\n'.join([self.name + " (" + str(self.get_skill()) + ")"] + ["- " + player.name for player in self.players] + [""])

    def get_skill(self):
        return sum([p.get_stats() for p in self.players])

def arrange_teams(players):
    team1 = Team()
    team2 = Team()
    while team1.name == team2.name:
        team2 = Team()
        
    

    # Try to get the teams as even as possible
    for max_skill_gap in range(1,1000,5):
        for i in range(2000):
            # Assign teams
            shuffle(players)
            for player in players:
                if team2.get_skill() > team1.get_skill():
                    team1.players.append(player)
                else:
                    team2.players.append(player)
            # If they're within tolerance, return
            if (abs(team1.get_skill() - team2.get_skill()) < max_skill_gap):
                return team1, team2
            else:
                # Clear teams and try again
                del team1.players[:]
                del team2.players[:]   
    sys.exit()

   
def read_players(filename = 'players.csv'):
    with open(filename, 'r') as f:
        csv_file = csv.reader(f)
        try:           
            return [Player(line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5])) for line in csv_file if not line[0].startswith("#")]
        except:
            print("Incorrectly formatted csv")
            sys.exit()


players = read_players()

[team1, team2] = arrange_teams(players)

print("HOME TEAM")
print(team1)
print("AWAY TEAM (BIBS)")
print(team2)
