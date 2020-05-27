import csv
import re
import os
import sys
import re

# work path
Path = 'Data/9-Happiness'

# src path
SrcPath = 'Data/6-Quotes'

# select seasons
fromSeason = 1
toSeason = 10

# create episodes folder if it does not exist
if not os.path.exists(Path):
    os.makedirs(Path)

personsHappiness = {}
happinessValues = {}

# regex for names
regex = re.compile('[^a-zA-Z0-9]')

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
            # only add characters that have said more than 10 quotes in the series
            if int(row[1]) >= 100:
                personsHappiness[row[0]] = 0


with open("src/1-Crawler/Happiness.csv") as csv_file:
    # read current CSV file
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
       happinessValues[row[0]] = row[1]

for person in personsHappiness:
    byName = person
    count = 0
    happinessTotal = 0
    # iterate through seasons
    for S in range(fromSeason,toSeason+1):
        if(S < 8):
            maxEpisodes = 22
        else:
            maxEpisodes = 20
        
        # iterate through episodes
        for E in range(1, maxEpisodes+1):
            if(E <10):
                filename = str(S)+"-"+"0"+str(E)
            else:
                filename = str(S)+"-"+str(E)

            with open(SrcPath + '/' + "episodes/" + filename + ".csv") as csv_file:
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
                        # everything to lower space
                        author = row[0].lower()
                        # remove characters that are not needed
                        author = regex.sub('', author)
                        if author == byName:
                            quote = row[1]
                        else:
                            quote = ""
                        words = quote.split(" ")
                        for word in words:
                            # everything to lower space
                            word = word.lower()
                            # remove characters that are not needed
                            word = regex.sub('', word)
                            if word in happinessValues:
                                count += 1
                                happinessTotal += float(happinessValues[word])
    
    # print to dic
    normalizedHappiness = happinessTotal / count
    personsHappiness[byName] = normalizedHappiness

# Convert to lists and sort
lPer = sorted(personsHappiness.items(), key=lambda x: x[1], reverse=True)

# back to dictionary 
sorted_Happiness = dict(lPer)

# Write Persons to file
csv_file = Path + "/" + "happiness.csv"
csv_columns = ['Name','Value']
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in sorted_Happiness.items():
        writer.writerow([key, value])

