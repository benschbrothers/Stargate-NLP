import os
import stanza
from bs4 import BeautifulSoup
import csv

# Define Seasons
fromSeason = 1
toSeason = 10

# Complete text will be stored in "completeCorpus"
completeCorpus = ''

# create POS folder if it does not exist
if not os.path.exists('RAW/'):
    os.makedirs('RAW/')

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

        if(E <10):
            savename = str(S)+"-"+"0"+str(E)
        else:
            savename = str(S)+"-"+str(E)
        
        # Output Episode content without html tags
        print(episodeWithoutTags,  file=open('RAW/'+savename+'.txt', 'w'))
        

