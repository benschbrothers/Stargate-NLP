import csv
import re
import os

# work path
Path = 'Data/4-Entities/counts'

# create workdir folder if it does not exist
if not os.path.exists(Path):
    os.makedirs(Path)

newDictPersons = {} 
newDictOrgs = {} 
newDictPlaces = {} 
newDictProducts = {} 

nicknamesONEILL = ['oneill', 'jack', 'coloneloneill', 'colonel', 'jackoneill', 'youngjack']
nicknamesCARTER = ['carter', 'sam', 'samantha', 'samanthacarter', 'cartersir', 'thera', 'carterthera'] 
nicknamesTEALC = ['teal', 'tealc', 'tealcs']
nicknamesDANIEL = ['daniel', 'jackson', 'danieljackson']

PERSONS = ['vala', 'kawalsky', 'bratac', 'fraiser', 'apophis', 'linea', 'hammond', 'maybourne', 'mitchell', 'baal', 'skaara', 'sokar', 'anubis']
ORGS = ['sg1', 'goauld']

newDictPersons['oneill'] = 0
newDictPersons['carter'] = 0
newDictPersons['tealc'] = 0
newDictPersons['daniel'] = 0

# Clean up Persons, look for nicknames of major characters
with open(Path + '/' + 'Persons.csv') as csv_file:
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
            if row[0] in nicknamesONEILL:
                newDictPersons['oneill'] += int(row[1])
            elif row[0] in nicknamesCARTER:
                newDictPersons['carter'] += int(row[1])
            elif row[0] in nicknamesTEALC:
                newDictPersons['tealc'] += int(row[1])
            elif row[0] in nicknamesDANIEL:
                newDictPersons['daniel'] += int(row[1])
            else:
                if int(row[1]) > 2:
                    newDictPersons[row[0]] = int(row[1])

# load Organisations and clean all person counts to person dict
with open(Path + '/' + 'Orgs.csv') as csv_file:
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
            if row[0] in nicknamesONEILL:
                newDictPersons['oneill'] += int(row[1])
            elif row[0] in nicknamesCARTER:
                newDictPersons['carter'] += int(row[1])
            elif row[0] in nicknamesTEALC:
                newDictPersons['tealc'] += int(row[1])
            elif row[0] in nicknamesDANIEL:
                newDictPersons['daniel'] += int(row[1])
            elif row[0] in PERSONS:
                newDictPersons[row[0]] += int(row[1])
            else:
                if int(row[1]) > 1:
                    newDictOrgs[row[0]] = int(row[1])

# load Organisations and clean all person counts to person dict
with open(Path + '/' + 'Places.csv') as csv_file:
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
            if row[0] in nicknamesONEILL:
                newDictPersons['oneill'] += int(row[1])
            elif row[0] in nicknamesCARTER:
                newDictPersons['carter'] += int(row[1])
            elif row[0] in nicknamesTEALC:
                newDictPersons['tealc'] += int(row[1])
            elif row[0] in nicknamesDANIEL:
                newDictPersons['daniel'] += int(row[1])
            elif row[0] in PERSONS:
                newDictPersons[row[0]] += int(row[1])
            elif row[0] in ORGS:
                newDictOrgs[row[0]] += int(row[1])
            else:
                if int(row[1]) > 1:
                    newDictPlaces[row[0]] = int(row[1])

# load Organisations and clean all person counts to person dict
with open(Path + '/' + 'Products.csv') as csv_file:
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
            if row[0] in nicknamesONEILL:
                newDictPersons['oneill'] += int(row[1])
            elif row[0] in nicknamesCARTER:
                newDictPersons['carter'] += int(row[1])
            elif row[0] in nicknamesTEALC:
                newDictPersons['tealc'] += int(row[1])
            elif row[0] in nicknamesDANIEL:
                newDictPersons['daniel'] += int(row[1])
            elif row[0] in PERSONS:
                newDictPersons[row[0]] += int(row[1])
            elif row[0] in ORGS:
                newDictOrgs[row[0]] += int(row[1])
            else:
                if int(row[1]) > 1:
                    newDictProducts[row[0]] = int(row[1])

csv_columns = ['Name','Count']

# Convert to lists and sort
lPer = sorted(newDictPersons.items(), key=lambda x: x[1], reverse=True)
lPro = sorted(newDictProducts.items(), key=lambda x: x[1], reverse=True)
lPla = sorted(newDictPlaces.items(), key=lambda x: x[1], reverse=True)
lOrg = sorted(newDictOrgs.items(), key=lambda x: x[1], reverse=True)

# back to dictionary 
newDictPersons = dict(lPer)
newDictProducts = dict(lPro)
newDictPlaces = dict(lPla)
newDictOrgs = dict(lOrg)

with open(Path + "/" + "Persons_Clean.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in newDictPersons.items():
        writer.writerow([key, value])

with open(Path + "/" + "Orgs_Clean.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in newDictOrgs.items():
        writer.writerow([key, value])

with open(Path + "/" + "Places_Clean.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in newDictPlaces.items():
        writer.writerow([key, value])

with open(Path + "/" + "Products_Clean.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in newDictProducts.items():
        writer.writerow([key, value])