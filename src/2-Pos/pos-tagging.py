import os
import stanza
from bs4 import BeautifulSoup
import csv

# Workdir
Path = 'Data/5-POS'

# Src dir
srcPath = 'Data/1-HTML'

# Define Seasons test
fromSeason = 1
toSeason = 10

# Complete text will be stored in "completeCorpus"
completeCorpus = ''

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
        f = open(srcPath + '/' + filename, 'r',  errors='ignore')
        episode = f.read()

        # Parse to remove all html tags
        episodeWithoutTags = ''
        soup = BeautifulSoup(episode, 'html.parser')
        text = soup.find_all(text=True)
        for t in text:
            episodeWithoutTags += '{} '.format(t)
        
        completeCorpus += episodeWithoutTags

# Output Episode content without html tags
# print(episodeWithoutTags)

# Download required stanza packages 
stanza.download('en', processors='tokenize,pos')

# Setup stanza pipeline
nlp = stanza.Pipeline('en', processors='tokenize,pos')

# Run pipeline on episode
doc = nlp(completeCorpus)

# create POS folder if it does not exist
if not os.path.exists('POS'):
    os.makedirs('POS')

# output words and write to csv file
with open(Path + '/Pos-tags.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Text", "Upos", "Xpos"])
    for sentence in doc.sentences:
        for word in sentence.words:
            print("Word:", word.text, " upos:", word.upos, " xpos:", word.xpos)
            writer.writerow([word.text, word.upos, word.xpos])

