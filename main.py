import os
import csv
from random import seed
from random import random

csvpath = os.path.join('BoardgameData', 'BoardGameLibrary.csv')

def Game_Picker(Players, PartyGame):
    count = 0

    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        Header = next(csvreader, None)

        NameList = []
        TypeList = []
        Min_playerList = []
        Max_playerList = []
        Play_timeList = []

        for row in csvreader:
            count += 1
            NameList.append(row[0])
            TypeList.append(row[1])
            Min_playerList.append(row[2])
            Max_playerList.append(row[3])
            Play_timeList.append(row[4])

        GameNum = int(random()*count-1) 

        GameName = NameList[GameNum]
        GameType = TypeList[GameNum]
        GameMinP = int(Min_playerList[GameNum])
        GameMaxP = int(Max_playerList[GameNum])
        GameTime = Play_timeList[GameNum]
        Game = [GameName, GameType, GameMinP, GameMaxP, GameTime]
        print(Game)

        
        return(Game)

Players = int(input('How many players? > '))
PartyGame = False
if(input("Party Game? 'y' or 'n' > ")=='y'):
    PartyGame = True
print('Party:', PartyGame)

Game = Game_Picker(Players, PartyGame)

if('party' in Game and PartyGame == False):
    Game = Game_Picker(Players, PartyGame)
    print('1')
elif('party' not in Game and PartyGame == True):
    Game_Picker(Players, PartyGame)
    print('2')
elif(GameMinP > Players or GameMaxP < Players):
    Game_Picker(Players, PartyGame)
    print('3')

print(Game_Picker(Players, PartyGame)[0])





    

