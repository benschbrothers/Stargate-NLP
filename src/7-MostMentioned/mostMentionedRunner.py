import os
import csv

# WorkDir
Path = 'Src/7-MostMentioned'

# SrcDir
SrcPath = 'Data/6-Quotes'

print('Analyzing everything...')
# create MostMentioned csv 
# os.system('python ' + Path + "/" 'mostMentioned.py')

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
            # only add characters that have said more than 300 quotes in the series
            if line_count <= 51:
                print('Getting quotes for: ' + row[0])
                os.system('python ' + Path + "/" 'mostMentioned.py' + " " + row[0])
                line_count += 1