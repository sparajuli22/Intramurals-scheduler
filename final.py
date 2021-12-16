import random 
import string
import pandas as pd
import numpy as np
import xlsxwriter


# Importing data from csv file (U-REC real qualdratics input)
data = pd.read_csv(r"C:\Users\mlie23\Desktop\algo\Final_Project_Balsam\Team+Time+Preference_December+6,+2021_14.56 (1).csv")

# Q4_1 to Q4_7 represents Monday - Sunday
# Q7 = name of the sport 
# Q1 = Data of the teams
columns = ["Q7","Q1","Q4_1","Q4_2","Q4_3","Q4_4","Q4_5","Q4_6","Q4_7"]

data2 = pd.DataFrame(data= data, columns=columns)

data2 = data2.drop([0,1])

list_unique = data2.Q7.unique()
list_unique

game = [] # create list for storing specific games data
for i in list_unique:
    game.append(data2[data2["Q7"] == i])


for i in range(0,len(game)): # rename the days columns for the ease of iterating
    game[i] = game[i].rename(columns={
        "Q4_1":1,"Q4_2":2,"Q4_3":3,"Q4_4":4,"Q4_5":5,"Q4_6":6,"Q4_7":7}
        )

def timeList(team, day):
    list_teams = list(game[team]['Q1'])
    list_times = list(game[team][day])
    list_times = list(map(lambda i:[i], list_times)) # convert list to list of lists 
    dictofteams = {}

    for i in range(len(list_teams)):
        dictofteams[list_teams[i]] = str(list_times[i][0]).split(",")
    return dictofteams

    



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


def common(list1,list2):
    for value in list1:
        if value in list2 and value !='nan':
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


# Bipartite Matching algorithm
# Arguments:
#            1.Graph    : Consist of 2D lists that store the possible matches between all team
#                        size of list= n*n (where n is the number of teams)
#            2.Team     : index of the number of the team
#            3.matches  : default = -1, reprents index of the team. (If they have match, then -1 will 
#                        change to the number of the team they are playing against)
#                        EX: [-1,3,-1,1] => Team no.1 will be playing with team no.3
#            4.isPlaying: Checking if one team has played another team or not
#                        Then it will check if a team can play another team or not 
def findPossibleMatch(graph, team, matches, isPlaying):
    for i in range(len(graph)):
        if (graph[team][i] == 1) and (isPlaying[i] == False) and (team != i):
            isPlaying[i] = True
            if matches[i] == -1 or matches[i] == team or findPossibleMatch(graph, matches[i], matches, isPlaying):
                matches[team] = i
                matches[i] = team
                return True 
    return False

def common_time (a,b):
    #This is sorted
    gametime = [c for c in a if c in b]
    return (gametime)

#Writing to excel!
count = 1
for a in range (0,5):
    for days in range (1,8):
        newTimeList = timeList(a,days)
        teams1 = list(getList(newTimeList))
        def filter(graph):
            noOfTeams = len(graph)
            matches = [-1] * noOfTeams
            for team in range(len(graph)):
                isPlaying = [False] * noOfTeams
                isPlaying[team] = True
                findPossibleMatch(graph, team, matches, isPlaying)
            # get the index of the keys in dict
            list_index = list(newTimeList)
            pairing = []
            for i in matches:
                pairing.append('No match') if i == -1 else pairing.append(list_index[i])
            return pairing
        final_matches = (filter(check(newTimeList, teams1)))
        workbook = xlsxwriter.Workbook('Result'+str(count)+'.xlsx')
        worksheet = workbook.add_worksheet()
        count+=1
        row = 0
        column = 0
        if len(final_matches)%2==1:
            for i in range(((len(final_matches)+1)//2)):
                if final_matches[i]!="No match":
                    print(teams1[i], " vs ", teams1[i])
                    worksheet.write (row,column, teams1[i]+" vs "+ final_matches[i])
                    listoftime = common_time(newTimeList[teams1[i]], newTimeList[final_matches[i]])
                    for time in range (len(listoftime)):
                        worksheet.write (i,time+1, listoftime[time])
                    column+=1
                row+=1
        else:
            for i in range(((len(final_matches))//2)):
                if final_matches[i]!="No match":
                    print(teams1[i], " vs ", teams1[i])
                    worksheet.write (row,column, teams1[i]+" vs "+ final_matches[i])
                    listoftime = common_time(newTimeList[teams1[i]], newTimeList[final_matches[i]])
                    for time in range (len(listoftime)):
                        worksheet.write (i,time+1, listoftime[time])
                    column+=1
                row+=1
        workbook.close()










    # This is shuffled
    # gametime= set(a).intersection(b)
    # return (gametime)



# teams1_new = [x for x in teams1 if np.isnan(x) == False] # delete all the nan values 

# final_matches_new = [x for x in final_matches if np.isnan(x) == False] # delete all the nan values

# counter = 0
# while(set(teams1_new) & set(final_matches_new)):
#     print(teams1_new[i]," Vs. ",final_matches_new[i])
#     teams1_new.remove(final_matches_new[i])
#     final_matches_new.remove(teams1_new[i])
#     counter=counter+1

    

    
    
