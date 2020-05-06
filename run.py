import os
import stanza
from bs4 import BeautifulSoup
import csv

currentEpisode = "1-01"

# Read season 1 episode 1 test file
f = open('HTML/' + currentEpisode + '.html', 'r')
episode = f.read()

# Parse to remove all html tags
episodeWithoutTags = ''
soup = BeautifulSoup(episode, 'html.parser')
text = soup.find_all(text=True)
for t in text:
    episodeWithoutTags += '{} '.format(t)

# Output Episode content without html tags
# print(episodeWithoutTags)

# Download required stanza packages 
stanza.download('en', processors='tokenize,pos')

# Setup stanza pipeline
nlp = stanza.Pipeline('en', processors='tokenize,pos')

# Run pipeline on episode
doc = nlp(episodeWithoutTags)

# output words and write to csv file
for sentence in doc.sentences:
    for word in sentence.words:
        print("Text:", word.text, word.upos, word.xpos)


with open('POS/'+ currentEpisode +'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Text", "Upos", "Xpos"])
    for sentence in doc.sentences:
        for word in sentence.words:
            print("Word:", word.text, " upos:", word.upos, " xpos:", word.xpos)
            writer.writerow([word.text, word.upos, word.xpos])

