import csv
import re
import os

#### NOT WORKING

# work path
Path = 'Data/4-Entities/counts'

# src path
SrcPath = 'Data/6-Quotes'


fileOutput = "" 

nicknamesONEILL = ['oneill', 'jack', 'coloneloneill', 'colonel', 'jackoneill', 'youngjack']
nicknamesCARTER = ['carter', 'sam', 'captain', 'samantha', 'samanthacarter', 'cartersir', 'thera', 'carterthera'] 
nicknamesTEALC = ['teal', 'tealc', 'tealcs']
nicknamesDANIEL = ['daniel', 'jackson', 'danieljackson']

print(fileOutput)

with open(SrcPath + '/' + "ListNames.csv") as csv_file:
    # read current CSV file
    csv_reader = csv.reader(csv_file, delimiter=',')
    # start with first line 
    line_count = 0
    for row in csv_reader:
        # first line is the header
        if line_count == 0:
            line_count += 1
        # others are entities
        else:
            if row[1] >= 10:
                # take only Characters that talk more than 10 times
                print("todo")


# with open(csv_file, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(csv_columns)
#     for key, value in sorted_PlacesC.items():