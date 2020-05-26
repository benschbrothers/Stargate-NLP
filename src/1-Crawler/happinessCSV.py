import csv

# loads the happiness data set from https://arxiv.org/abs/1101.5120 

# src path
Path = 'src/1-Crawler'

happinessDic = {}

line = 0
# loads the happiness data set from https://arxiv.org/abs/1101.5120 
with open(Path + "/" +  "pone.0026752.s001.txt", newline = '') as games:                                                                                          
    data = csv.reader(games, delimiter='\t')
    line = 0
    for word in data:
        # save average happiness in dictionary
        happinessDic[word[0]] = word[2]

# Write happiness to csv file
csv_file = Path + "/" + "Happiness.csv"
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for key, value in happinessDic.items():
        writer.writerow([key, value])
        