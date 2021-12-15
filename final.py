import random 
import string
import pandas as pd
import numpy as np

data = pd.read_csv("/Users/mmourya23/Downloads/Team+Time+Preference+-+Fall+Indoor_December+6,+2021_14.59.csv")

columns = ["Q7","Q1","Q4_1","Q4_2","Q4_3","Q4_4","Q4_5","Q4_6","Q4_7"]

data2 = pd.DataFrame(data= data, columns=columns)
data2 = data2.drop([0,1])

list_unique = data2.Q7.unique()
list_unique

game = [] # create list for storing specific games data
for i in list_unique:
    game.append(data2[data2["Q7"] == i])

for i in range(0,len(game)): # rename the days columns for the ease of iterating
    game[i] = game[i].rename(columns={"Q4_1":1,"Q4_2":2,
    "Q4_3":3,
    "Q4_4":4,"Q4_5":5,"Q4_6":6,"Q4_7":7})

def timeList(team, day):
    list_teams = list(game[team]['Q1'])
    list_times = list(game[team][day])
    list_times = list(map(lambda i:[i], list_times)) # convert list to list of lists 

    dictofteams = {}
    # print(list_teams)
    # print(list_times)

    for i in range(len(list_teams)):
        dictofteams[list_teams[i]] = str(list_times[i][0]).split(",")
    return dictofteams

    
# list_teams = list(game[0]['Q1'])
# list_times = list(game[0]['Q4_4'])
# list_times = list(map(lambda i:[i], list_times)) # convert list to list of lists 
# check game 4 - Free Mason got fucked up

# for i in range(len(list_teams)):

#     print(list_teams[i],list_times[i])



class teams:
   def __init__(self,timeslot = None, name=None):
        if timeslot is None:
            timeslot = []
        self.timeslot = timeslot

        if name is None:
            name = ''.join(random.choices(string.ascii_uppercase+string.digits, k=5))
        self.name = name
    
class graph:
   def __init__(self,graph):
      self.graph = graph
# Get the keys of the dictionary
   def getVertices(self):
      return list(self.gdict.keys())

def getList(dict):
    return dict.keys()

print("Enter Game:")
gameNumber = int(input())
print("Enter Day:")
dayNumber = int(input())

newTimeList = timeList(gameNumber,dayNumber)
#print (newTimeList)

teams1 = list(getList(newTimeList))
#print(teams1,"\n""\n")

def common(list1,list2):
    for value in list1:
        if value in list2:
            return value,True
    return False


def check (newTimeList, teams1):
    noOfTeams = len(newTimeList)
    graph = [[0 for i in range(noOfTeams)] for j in range(noOfTeams)]
    for i in range(0, len(graph)):
        for j in range(0, len(graph[0])):
            if i > j and common(newTimeList[teams1[i]], newTimeList[teams1[j]]):
                graph[i][j] = graph[j][i] = 1
    return graph 

def findPossibleMatch(graph, team, matches, isPlaying):
    for i in range(len(graph)):
        # print(matches)
        if (graph[team][i] == 1) and (isPlaying[i] == False) and (team != i):
            isPlaying[i] = True
            if matches[i] == -1 or matches[i] == team or findPossibleMatch(graph, matches[i], matches, isPlaying):
                matches[team] = i
                matches[i] = team
                return True
    return False

def filter(graph):
    noOfTeams = len(graph)
    matches = [-1] * noOfTeams

    for team in range(len(graph)):
        isPlaying = [False] * noOfTeams
        isPlaying[team] = True
        findPossibleMatch(graph, team, matches, isPlaying)
     
    list_index = list(newTimeList) # get the index of the keys in dict
    pairing = []
    for i in matches:
        pairing.append('No match') if i == -1 else pairing.append(list_index[i])
    
    return pairing

final_matches = (filter(check(newTimeList, teams1)))

for i in range(len(final_matches)):
    print(teams1[i], " Vs. ", final_matches[i])

# teams1_new = [x for x in teams1 if np.isnan(x) == False] # delete all the nan values 

# final_matches_new = [x for x in final_matches if np.isnan(x) == False] # delete all the nan values

# counter = 0
# while(set(teams1_new) & set(final_matches_new)):
#     print(teams1_new[i]," Vs. ",final_matches_new[i])
#     teams1_new.remove(final_matches_new[i])
#     final_matches_new.remove(teams1_new[i])
#     counter=counter+1

    

    
    
