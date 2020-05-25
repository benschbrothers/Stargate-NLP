import os
import stanza
from bs4 import BeautifulSoup
import csv
import re

# WorkDir
Path = 'Data/6-Quotes/'
# SrcDir
SrcPath = 'Data/6-Quotes/episodes/'

# create WorkDir folder if it does not exist
if not os.path.exists(Path):
    os.makedirs(Path)

# Define Seasons
fromSeason = 1
toSeason = 1

dictTopQuotesComplete= {} 

# regex for names
regex = re.compile('[^a-zA-Z0-9]')

targetPerson = "daniel"
dictTopQuotes = {} 
for S in range(fromSeason,toSeason+1):
    if(S < 8):
        maxEpisodes = 22
    else:
        maxEpisodes = 20
    
    for E in range(1, maxEpisodes+1):
        if(E <10):
            filename = str(S)+"-"+"0"+str(E)
        else:
            filename = str(S)+"-"+str(E)

        dictQuotes = {} 

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
                        if quote in dictQuotes:
                            dictQuotes[quote] = dictQuotes[quote] + 1
                        else:
                            dictQuotes[quote] = 1

        # Convert to list and sort
        lQuotes = sorted(dictQuotes.items(), key=lambda x: x[1], reverse=True)
        lQuotes = lQuotes[:20]
        # back to dictionary 
        sorted_Quotes = dict(lQuotes)
        # print(sorted_Quotes)

        for quote, value in sorted_Quotes.items():
            # print(quote + " " + str(value))
            if quote in dictTopQuotes:
                dictTopQuotes[quote] = dictTopQuotes[quote] + value
            else:
                dictTopQuotes[quote] = value

    lTopQuotes = sorted(dictTopQuotes.items(), key=lambda x: x[1], reverse=True)
    sorted_TopQuotes = dict(lTopQuotes)
    print(sorted_TopQuotes)