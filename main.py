import os
import csv
from random import seed
from random import random

csvpath = os.path.join('BoardgameData', 'BoardGameLibrary.csv')

count = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    Header = next(csvreader, None)

    for row in csvreader:
        count += 1
        print(count)
    

    Name = 'a'
    Type = 'a'
    Min_player = 0
    Max_player = 0
    Play_time = 0

