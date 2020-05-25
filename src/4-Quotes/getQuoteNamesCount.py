import os
import stanza
from bs4 import BeautifulSoup
import csv
import re
import sys

# WorkDir
Path = 'Data/6-Quotes/'
# SrcDir
SrcPath = 'Data/6-Quotes/episodes/'

# create WorkDir folder if it does not exist
if not os.path.exists(Path):
    os.makedirs(Path)

# Define Seasons
fromSeason = 1
toSeason = 10

# regex for names
regex = re.compile('[^a-zA-Z0-9]')

dictNames= {} 

for S in range(fromSeason,toSeason+1):
    if(S < 8):
        maxEpisodes = 22
    else:
        maxEpisodes = 20
    
    # Best Quotes of the Season
    dictSeasonNames = {} 
    for E in range(1, maxEpisodes+1):
        if(E <10):
            filename = str(S)+"-"+"0"+str(E)
        else:
            filename = str(S)+"-"+str(E)

        # Best Quotes of the Episode
        dictEpisodeNames = {} 

        with open(SrcPath + filename + ".csv") as csv_file:
            # read current CSV file
            csv_reader = csv.reader(csv_file, delimiter=',')
            # start with first line 
            line_count = 0
            for row in csv_reader:
                # first line is the header
                if line_count == 0:
                    # print(f'Column names are {", ".join(row)}')
                    line_count += 1
                # others are entities
                else:
                    # everything to lower space
                    name = row[0].lower()
                    # remove characters that are not needed
                    name = regex.sub('', name)

                    if name in dictEpisodeNames:
                        dictEpisodeNames[name] = dictEpisodeNames[name] + 1
                    else:
                        dictEpisodeNames[name] = 1

        # Convert to list and sort
        lEpisodeNames = sorted(dictEpisodeNames.items(), key=lambda x: x[1], reverse=True)
        # back to dictionary 
        sorted_EpisodeNames = dict(lEpisodeNames)
        # print(sorted_Quotes)

        for name, value in sorted_EpisodeNames.items():
            # print(quote + " " + str(value))
            if name in dictSeasonNames:
                dictSeasonNames[name] = dictSeasonNames[name] + value
            else:
                dictSeasonNames[name] = value

    lSeasonNames = sorted(dictSeasonNames.items(), key=lambda x: x[1], reverse=True)
    sorted_SeasonNames = dict(lSeasonNames)
    # print(sorted_SeasonQuotes)

    for name, value in sorted_SeasonNames.items():
            # print(quote + " " + str(value))
            if name in dictNames:
                dictNames[name] = dictNames[name] + value
            else:
                dictNames[name] = value

lNames = sorted(dictNames.items(), key=lambda x: x[1], reverse=True)
sorted_Names = dict(lNames)
# print(sorted_TopQuotes)

# Write Places to file
csv_file = Path + "ListNames.csv"
csv_columns = ['Quote','Count']

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in sorted_Names.items():
        if(key != 'nochar'):
            writer.writerow([key, value])