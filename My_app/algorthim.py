'''
'''
import itertools
import math

class Players():
    '''
    
    Attributes:
        names: dictonry of names and their respectivy skills
        fairness_rating: fairness rating of each created team
        team2_skill: the combine skill of team2
        team1_skill: the combine skill of team1
    '''


    def __init__(self,names):
        '''initizes atrributes '''
        self.names = names
        self.fairness_rating = 100
        self.team2_skill = 0
        self.team1_skill = 0


    def __fairness(self,teams):
        '''calculates fairness of give list of teams'''
        
        # resets team skill to zero
        self.team2_skill = 0
        self.team1_skill = 0
        
        #splits list into two teams
        team1 = teams[len(teams)//2:]
        team2 = teams[:len(teams)//2]
        
        #calcutes total skill of both teams
        for i in range(len(team1)):
            self.team1_skill += self.names[team1[i]]
    
        for i in range(len(team2)):
            self.team2_skill += self.names[team2[i]]
    
        #return abs val of diffrence between the two team
        self.fairness_rating = abs(self.team1_skill - self.team2_skill)
        return self.fairness_rating


    def __combo_maker(self):
        '''creates the possible teams returns the combonation of teams that are the most fair.
            The lower the fairness rating the more fair the teams are beacasue the diffrence between
            their combintied skill is closes to zero, where the the fairnes rating is the same'''
        
        combs = []
        all_games = []
        most_fair = 100
    
        #uses itertools to go thru all possible combonations of names    
        for i in range(1):
            els = [list(x) for x in itertools.combinations(self.names, int(len(self.names)/2))]
            combs.append(els)
    
        #creates a game with combonation of teams, into one list, then all the game into another list
        for i in range(int(len(combs[0])/2)):
            game = combs[0][i] + combs[0][(len(combs[0])-1)-i]
            all_games.append(game)
        
        #iterates thru each item of game in the list of all the games to find fairest game
        for one_game in all_games:
    
            self.fairness_rating = self.__fairness(one_game)
    
            if self.fairness_rating < most_fair :#stores game with lowest fairness rating 
                most_fair = self.fairness_rating
                most_fair_game = one_game
    
        return most_fair_game
    
    def team_maker(self):
        '''returns 2D list of most fair game where the each team is a sublist '''
        
        game = []
        most_fair_game = self.__combo_maker()# calls the combo maker method to get most fair 
    
        #splits into two teams
        team1 = most_fair_game[len(most_fair_game)//2:]
        team2 = most_fair_game[:len(most_fair_game)//2]
          
        #adds both teams to game list so that they are sublists
        game.append(team1)
        game.append(team2) 
         
        return game