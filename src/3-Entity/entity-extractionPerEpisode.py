import os
import stanza
from bs4 import BeautifulSoup
import csv

# Define Seasons
fromSeason = 1
toSeason = 10

# Complete text will be stored in "completeCorpus"
completeCorpus = ''

# Download required stanza packages 
stanza.download('en')

# Setup stanza pipeline
nlp = stanza.Pipeline('en')

# create Entities folder if it does not exist
if not os.path.exists('Entities/episodes'):
    os.makedirs('Entities/episodes')

for S in range(fromSeason,toSeason+1):
    if(S < 8):
        maxEpisodes = 22
    else:
        maxEpisodes = 20
    
    for E in range(1, maxEpisodes+1):
        if(E <10):
            filename = str(S)+"-"+"0"+str(E)+".html"
        else:
            filename = str(S)+"-"+str(E)+".html"

        print("Parsing:" + filename)

        # Read season 1 episode 1 test file
        f = open('HTML/' + filename, 'r',  errors='ignore')
        episode = f.read()

        # Parse to remove all html tags
        episodeWithoutTags = ''
        soup = BeautifulSoup(episode, 'html.parser')
        text = soup.find_all(text=True)
        for t in text:
            episodeWithoutTags += '{} '.format(t)
        
        # Run pipeline on episode
        doc = nlp(episodeWithoutTags)

        if(E <10):
            savename = str(S)+"-"+"0"+str(E)
        else:
            savename = str(S)+"-"+str(E)
        
        # output words and write to csv file
        with open('Entities/episodes/'+ savename+ '.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Entity", "Type"])
            for sentence in doc.sentences:
                for ent in sentence.ents:
                    print("entity:", ent.text, " type:", ent.type)
                    writer.writerow([ent.text, ent.type])
        
        # completeCorpus += episodeWithoutTags




