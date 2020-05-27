import os
import csv

# WorkDir
Path = 'Src/4-Quotes/'

# SrcDir
SrcPath = 'Data/6-Quotes/'

print('Parsing HTML to readable Quote CSVs')
# Parsing all Quotes from HTML to cleaned CSVs
os.system('python ' + Path + 'getQuotes.py')

print('Analyzing Protagonists...')
# Get every talking Person and count their quotes
os.system('python ' + Path + 'getQuoteNamesCount.py')

 
with open(SrcPath + "ListNames.csv") as csv_file:

    # read CSV file
    csv_reader = csv.reader(csv_file, delimiter=',')

    # start with first line 
    line_count = 0
    for row in csv_reader:

        # first line is the header
        if line_count == 0:
            line_count += 1

        # others are persons
        else:
            line_count += 1
            # just get the 40 first protagonists
            if(line_count <= 40):
                name = row[0].lower()
                print('Analyzing Top Quotes: ' + name)
                os.system('python ' + Path + 'getTopQuotes.py ' + name)

print('Quote Scripts done!')