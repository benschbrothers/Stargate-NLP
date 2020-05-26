import csv
import re
import os
import sys

# work path
Path = 'Data/7-MostMentioned'

# src path
SrcPath = 'Data/6-Quotes'

# select by
by = False
byName = 'oneill'

# Get the target person
if(len(sys.argv) == 2):
    by = True
    byName = sys.argv[1]
else:
    print("no target person specified! Using all quotes")

# select seasons
fromSeason = 1
toSeason = 10

# create episodes folder if it does not exist
if not os.path.exists(Path):
    os.makedirs(Path)

# create episodes folder if it does not exist
if not os.path.exists(Path + "/episodes"):
    os.makedirs(Path + "/episodes")

# create by folder if it does not exist
if not os.path.exists(Path + "/by"):
    os.makedirs(Path + "/by")

personsDict = {}

nicknamesONEILL = ['jack', 'coloneloneill', 'colonel', 'jackoneill', 'youngjack']
nicknamesCARTER = ['sam', 'samantha', 'captain', 'samanthacarter', 'cartersir', 'thera', 'carterthera'] 
nicknamesTEALC = ['teal', 'tealcs']
nicknamesDANIEL = ['jackson', 'danieljackson']

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
            if int(row[1]) >= 10:
                personsDict[row[0]] = 0

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
                    # select if quotes only from one char
                    if by:                         
                        # everything to lower space
                        author = row[0].lower()
                        # remove characters that are not needed
                        author = regex.sub('', author)
                        if author == byName:
                            quote = row[1]
                        else:
                            quote = ""
                    else:
                        quote = row[1]
                    
                    words = quote.split(" ")
                    for word in words:
                        # everything to lower space
                        word = word.lower()
                        # remove characters that are not needed
                        word = regex.sub('', word)
                        if word in nicknamesONEILL:
                            personsDict['oneill'] += 1
                        elif word in nicknamesCARTER: 
                            personsDict['carter'] += 1
                        elif word in nicknamesTEALC:
                            personsDict['tealc'] += 1
                        elif word in nicknamesDANIEL:
                            personsDict['daniel'] += 1
                        elif word in personsDict:
                            personsDict[word] += 1

# Convert to lists and sort
lPer = sorted(personsDict.items(), key=lambda x: x[1], reverse=True)

# back to dictionary 
sorted_Mentioned = dict(lPer)

if by:
    # Write Persons to file
    csv_file = Path + "/" + "by/" + byName + ".csv"
    csv_columns = ['Name','Count']

    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_columns)
        for key, value in sorted_Mentioned.items():
            writer.writerow([key, value])
else:
    # Write Persons to file
    csv_file = Path + "/" + "MostMentioned.csv"
    csv_columns = ['Name','Count']

    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_columns)
        for key, value in sorted_Mentioned.items():
            writer.writerow([key, value])
