#Shirts or Skins primary FUnction Implementation
#Developers : Ben and Yasha
#Date Created 12/1/2017

class Player():
  def __init__(self,names):
    self.names = names
    
  def team_maker(self):
    
    def fairness(teams):
      team1 = teams[len(teams)//2:]
      team2 = teams[:len(teams)//2]
      team2_skill = 0
      team1_skill = 0    
      for i in range(len(team1)):
        team1_skill += self.names[team1[i]]
      team1_skill /= len(team1)
      for i in range(len(team2)):
        team2_skill += self.names[team2[i]]
      team2_skill /= len(team2)
      
      fairness_rating = abs(team1_skill-team2_skill)
      return fairness_rating
      
    ctr = len(self.names)
    ctr2 = 0 
    f=100
    #f_team =[]
    names= []
    for i in self.names:
      names.append(i)
      
      ctr2 = -1
    while ctr2 != len(names):
      ctr = ctr2+1
      teams = []
      loop_ctr = 0
      while loop_ctr != len(names):
        if ctr >= len(names):
          ctr=0
        teams.append(names[ctr])
        ctr+=1
        loop_ctr +=1
        if len(teams)==len(names):
          print(teams)
          fair = fairness(teams)
          
          if fair < f:
            f = fair
            f_team = teams
            
      ctr2+=1
      
    teams = []
    for i in range(len(names)):
      if i % 2 != 0:
        teams.append(names[i])
        
    for i in range(len(names)):
      if i % 2 == 0:
        teams.append(names[i])  
    print(teams)
    fair = fairness(teams)
    if fair < f:
      f = fair
      f_team = teams
      
    print('')
    print(f_team)
    print(f)
    
    team1 = f_team[len(f_team)//2:]
    team2 = f_team[:len(f_team)//2]
    print(""" Shrits  | Skins
              %s      |  %s      """ %(team1, team2)
    
      
obj = Player({'Ben':4,'Yasha':3, 'Josh':2, 'Max':1})
obj.team_maker()
'''
ben, yasha vs josh,max
ben, max vs yasha,josh
ben josh vs yasha,max

ben,yasha,josh,max
yasha,josh,max,ben
josh,max,ben,yasha
max,ben,yasha,josh
'''




