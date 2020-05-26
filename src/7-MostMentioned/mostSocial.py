import csv
import re
import os
import sys

# work path
Path = 'Data/8-MostMentioned'

# src path
SrcPath = 'Data/8-MostMentioned/by'

# names path
namesPath = 'Data/6-Quotes'

dictSocial = {}

with open(namesPath + '/' + "ListNames.csv") as csv_file:
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
            if int(row[1]) >= 300:
                name =  row[0]
                print('couting mentions for: ' + name)
                count = 0
                with open(SrcPath + '/' +  name + ".csv") as csv_file:
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
                            count += int(row[1])

                dictSocial[name] = count


removedZeros = {}
for person, count in dictSocial.items():
    if count != 0:
        removedZeros[person] = count

# Convert to lists and sort
lSoc = sorted(removedZeros.items(), key=lambda x: x[1], reverse=True)

# back to dictionary 
sorted_Social = dict(lSoc)

# print(sorted_Social)
csv_columns = ['Name','Count']

# Write happiness to csv file
csv_file = Path + "/" + "MostSocial.csv"
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
        writer.writerow(csv_columns)
    for key, value in sorted_Social.items():
        writer.writerow([key, value])
