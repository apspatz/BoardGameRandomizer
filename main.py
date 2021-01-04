import os
import csv
from random import seed
from random import random

csvpath = os.path.join('BoardgameData', 'BoardGameLibrary.csv')

count = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    Header = next(csvreader, None)

    Name = []
    Type = []
    Min_player = []
    Max_player = []
    Play_time = []

    for row in csvreader:
        count += 1
        Name.append(row[0])
        Type.append(row[1])
        Min_player.append(row[2])
        Max_player.append(row[3])
        Play_time.append(row[4])
    
    GameNum = int(random()*count-1) 

    

