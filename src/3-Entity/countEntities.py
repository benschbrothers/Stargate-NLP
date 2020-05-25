import csv
import re
import os

# regex for names
regex = re.compile('[^a-zA-Z0-9]')

fromSeason = 1
toSeason = 10

dictPersonsComplete = {} 
dictOrgComplete = {} 
dictProductComplete = {}
dictPlacesComplete = {}


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

        dictPersons = {} 
        dictOrg = {} 
        dictProduct = {}
        dictPlaces = {}

        with open('Entities/episodes/' + filename + ".csv") as csv_file:
            # read current CSV file
            csv_reader = csv.reader(csv_file, delimiter=',')
            # start with first line 
            line_count = 0
            for row in csv_reader:
                # first line is the header
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                # others are entities
                else:
                    # everything to lower space
                    name = row[0].lower()
                    # remove characters that are not needed
                    name = regex.sub('', name)

                    # Person list
                    if row[1] == "PERSON":
                        if name in dictPersons:
                            dictPersons[name] = dictPersons[name] + 1
                        else:
                            dictPersons[name] = 1

                    # Organisation list
                    if row[1] == "ORG":
                        if name in dictOrg:
                            dictOrg[name] = dictOrg[name] + 1
                        else:
                            dictOrg[name] = 1

                    # Product list
                    if row[1] == "PRODUCT":
                        if name in dictProduct:
                            dictProduct[name] = dictProduct[name] + 1
                        else:
                            dictProduct[name] = 1

                    # Places list
                    if row[1] == "GPE":
                        if name in dictPlaces:
                            dictPlaces[name] = dictPlaces[name] + 1
                        else:
                            dictPlaces[name] = 1

                    # Person list complete
                    if row[1] == "PERSON":
                        if name in dictPersonsComplete:
                            dictPersonsComplete[name] = dictPersonsComplete[name] + 1
                        else:
                            dictPersonsComplete[name] = 1

                    # Organisation list complete
                    if row[1] == "ORG":
                        if name in dictOrgComplete:
                            dictOrgComplete[name] = dictOrgComplete[name] + 1
                        else:
                            dictOrgComplete[name] = 1

                    # Product list complete
                    if row[1] == "PRODUCT":
                        if name in dictProductComplete:
                            dictProductComplete[name] = dictProductComplete[name] + 1
                        else:
                            dictProductComplete[name] = 1

                    # Places list complete
                    if row[1] == "GPE":
                        if name in dictPlacesComplete:
                            dictPlacesComplete[name] = dictPlacesComplete[name] + 1
                        else:
                            dictPlacesComplete[name] = 1
                    line_count += 1
            print(f'Processed file {filename} with {line_count} lines.')

        # print(dictPersons)

        # create Entities folder if it does not exist
        if not os.path.exists('Entities/counts/episodes'):
            os.makedirs('Entities/counts/episodes')

        Path = 'Entities/counts/episodes/'

        # Convert to lists and sort
        lPer = sorted(dictPersons.items(), key=lambda x: x[1], reverse=True)
        lPro = sorted(dictProduct.items(), key=lambda x: x[1], reverse=True)
        lPla = sorted(dictPlaces.items(), key=lambda x: x[1], reverse=True)
        lOrg = sorted(dictOrg.items(), key=lambda x: x[1], reverse=True)

        # back to dictionary 
        sorted_Persons = dict(lPer)
        sorted_Products = dict(lPro)
        sorted_Places = dict(lPla)
        sorted_Orgs = dict(lOrg)

        # Write Persons to file
        csv_file = Path + filename + "-Persons.csv"
        csv_columns = ['Name','Count']

        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_columns)
            for key, value in sorted_Persons.items():
                writer.writerow([key, value])

        # Write Places to file
        csv_file = Path + filename + "-Places.csv"
        csv_columns = ['Name','Count']

        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_columns)
            for key, value in sorted_Places.items():
                writer.writerow([key, value])

        # Write Organisations to file
        csv_file = Path + filename + "-Orgs.csv"
        csv_columns = ['Name','Count']

        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_columns)
            for key, value in sorted_Orgs.items():
                writer.writerow([key, value])


        # Write Products to file
        csv_file = Path + filename + "-Products.csv"
        csv_columns = ['Name','Count']

        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_columns)
            for key, value in sorted_Products.items():
                writer.writerow([key, value])

 # create Entities folder if it does not exist
if not os.path.exists('Entities/counts/'):
    os.makedirs('Entities/counts/')

PathC = 'Entities/counts//'

# Convert to lists and sort
lPerC = sorted(dictPersonsComplete.items(), key=lambda x: x[1], reverse=True)
lProC = sorted(dictProductComplete.items(), key=lambda x: x[1], reverse=True)
lPlaC = sorted(dictPlacesComplete.items(), key=lambda x: x[1], reverse=True)
lOrgC = sorted(dictOrgComplete.items(), key=lambda x: x[1], reverse=True)

# back to dictionary 
sorted_PersonsC = dict(lPerC)
sorted_ProductsC = dict(lProC)
sorted_PlacesC = dict(lPlaC)
sorted_OrgsC = dict(lOrgC)

# Write Persons to file
csv_file = PathC + filename + "-Persons.csv"
csv_columns = ['Name','Count']

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in sorted_PersonsC.items():
        writer.writerow([key, value])

# Write Places to file
csv_file = PathC + filename + "-Places.csv"
csv_columns = ['Name','Count']

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in sorted_PlacesC.items():
        writer.writerow([key, value])

# Write Organisations to file
csv_file = PathC + filename + "-Orgs.csv"
csv_columns = ['Name','Count']

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in sorted_OrgsC.items():
        writer.writerow([key, value])


# Write Products to file
csv_file = PathC + filename + "-Products.csv"
csv_columns = ['Name','Count']

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for key, value in sorted_ProductsC.items():
        writer.writerow([key, value])