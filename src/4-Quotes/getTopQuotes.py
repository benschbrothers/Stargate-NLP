import os
import stanza
from bs4 import BeautifulSoup
import csv
import re
import sys

# Set default target person to oneill
targetPerson = "oneill"

# Get the target person
if(len(sys.argv) == 2):
    targetPerson = sys.argv[1]
else:
    print("no target person specified! taking oneill")

# WorkDir
Path = 'Data/6-Quotes/Top/'
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

dictTopQuotes= {} 

for S in range(fromSeason,toSeason+1):
    if(S < 8):
        maxEpisodes = 22
    else:
        maxEpisodes = 20
    
    # Best Quotes of the Season
    dictSeasonQuotes = {} 
    for E in range(1, maxEpisodes+1):
        if(E <10):
            filename = str(S)+"-"+"0"+str(E)
        else:
            filename = str(S)+"-"+str(E)

        # Best Quotes of the Episode
        dictEpisodeQuotes = {} 

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

                    if (name  == targetPerson):
                        quote = row[1].lower()
                        if quote in dictEpisodeQuotes:
                            dictEpisodeQuotes[quote] = dictEpisodeQuotes[quote] + 1
                        else:
                            dictEpisodeQuotes[quote] = 1

        # Convert to list and sort
        lEpisodeQuotes = sorted(dictEpisodeQuotes.items(), key=lambda x: x[1], reverse=True)
        lEpisodeQuotes = lEpisodeQuotes[:50]
        # back to dictionary 
        sorted_EpisodeQuotes = dict(lEpisodeQuotes)
        # print(sorted_Quotes)

        for quote, value in sorted_EpisodeQuotes.items():
            # print(quote + " " + str(value))
            if quote in dictSeasonQuotes:
                dictSeasonQuotes[quote] = dictSeasonQuotes[quote] + value
            else:
                dictSeasonQuotes[quote] = value

    lSeasonQuotes = sorted(dictSeasonQuotes.items(), key=lambda x: x[1], reverse=True)
    lSeasonQuotes = lSeasonQuotes[:50]
    sorted_SeasonQuotes = dict(lSeasonQuotes)
    # print(sorted_SeasonQuotes)

    for quote, value in sorted_SeasonQuotes.items():
            # print(quote + " " + str(value))
            if quote in dictTopQuotes:
                dictTopQuotes[quote] = dictTopQuotes[quote] + value
            else:
                dictTopQuotes[quote] = value

lTopQuotes = sorted(dictTopQuotes.items(), key=lambda x: x[1], reverse=True)
sorted_TopQuotes = dict(lTopQuotes)
# print(sorted_TopQuotes)

# Write Places to file
csv_file = Path + targetPerson + "-TopQuotes.csv"
csv_columns = ['Quote','Count']

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in sorted_TopQuotes.items():
        if(value >= 4):
            writer.writerow([key, value])