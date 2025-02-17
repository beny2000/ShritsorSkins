'''
Created on Dec 23, 2017

@author: ben
'''
import itertools
import math

class Players():
    
    

    def __init__(self,names):
        self.names = names
        self.fairness_rating = 100
        self.team2_skill = 0
        self.team1_skill = 0

    def __fairness(self,teams):
        team1 = teams[len(teams)//2:]
        team2 = teams[:len(teams)//2]
        self.team2_skill = 0
        self.team1_skill = 0

        for i in range(len(team1)):
          self.team1_skill += self.names[team1[i]]
    
        for i in range(len(team2)):
          self.team2_skill += self.names[team2[i]]
    
        self.fairness_rating = abs(self.team1_skill - self.team2_skill)
        return self.fairness_rating

    def __combo_maker(self):
        lst_names = list(self.names)
        combs = []
        all_games = []
        most_fair = 100
    
        for i in range(1):
            els = [list(x) for x in itertools.combinations(self.names, int(len(self.names)/2))]
            combs.append(els)
    
        for i in range(int(len(combs[0])/2)):
          game = combs[0][i] + combs[0][(len(combs[0])-1)-i]
          all_games.append(game)
    
        for one_game in all_games:
    
          self.fairness_rating = self.__fairness(one_game)
    
          if self.fairness_rating < most_fair :
            most_fair = self.fairness_rating
            most_fair_game = one_game
    
        return most_fair_game
    
    def team_maker(self):
        game = []
        #max_game_combs = (int(math.factorial(len(self.names)) / math.factorial(int(len(self.names)/2))**2))/2
        if 'Name' in self.names.keys():
    
            del self.names['Name']  
            most_fair_game = self.__combo_maker()
    
            team1 = most_fair_game[len(most_fair_game)//2:]
            team2 = most_fair_game[:len(most_fair_game)//2]

            #print(team1,'vs', team2)
          # return (team1,'vs', team2)
    
        else:
    
          #self.names.remove({'Name':'Skill'})
          most_fair_game = self.__combo_maker()
    
          team1 = most_fair_game[len(most_fair_game)//2:]
          team2 = most_fair_game[:len(most_fair_game)//2]
            
        game.append(team1)
        game.append(team2)  
        return game 
          #print(team1,'vs', team2)
          # return (team1,'vs', team2)


#Make an Input box for player input
#obj = Players({'Name':0,'Name':0,'Name':0,'Name':0, 'Name':'Skill'})
#print(obj.team_maker())