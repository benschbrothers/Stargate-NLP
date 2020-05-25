import os
import numpy as np
import requests

from bs4 import BeautifulSoup

# Work dir
Path = 'Data/1-HTML'

#Crawl main Transcripts site
url = 'http://www.stargate-sg1-solutions.com/wiki/Transcripts'
html = requests.get(url)
content = html.text
start = content.split('<h3><span class="mw-headline" id="Episode_Transcripts">Episode Transcripts</span></h3>')
end = start[1].split('<h3><span class="mw-headline" id="Movie_Transcripts">Movie Transcripts</span></h3>')
rawContent = end[0]

soup = BeautifulSoup(rawContent, "html.parser")

seasonURLs = []

for seasons in soup.find_all('a', href=True):
    seasonURLs.append("http://www.stargate-sg1-solutions.com" + seasons['href'])

# create HTML folder if it does not exist
if not os.path.exists(Path):
    os.makedirs(Path)

#Crawl the Season Sites
for season in seasonURLs:
    print("Crawling season: ", season)
    url = season
    html = requests.get(url)
    content = html.text
    start = content.split('<h2><span class="mw-headline" id="Note">Note</span></h2>')
    end = start[1].split('<h2><span class="mw-headline" id="Related_Articles">Related Articles</span></h2>')
    rawContentSeasons = end[0]

    soupSeasons = BeautifulSoup(rawContentSeasons, "html.parser")

    episodeURLs = []

    for episodes in soupSeasons.find_all('a', href=True):
        episodeURLs.append("http://www.stargate-sg1-solutions.com" + episodes['href'])

    episodeURLs = list(dict.fromkeys(episodeURLs))

    #Crawl each episode
    for episode in episodeURLs:
        url = episode
        if("_Transcript" in url): 
            html = requests.get(url)
            content = html.text

            start = content.split('<h2><span class="mw-headline" id="Transcript">Transcript</span></h2>')
            end = start[1].split('<h2><span class="mw-headline" id="Related_Articles">Related Articles</span></h2>')
            rawContent = end[0]

            start = url.split('/wiki/')
            end = start[1].split('_%')
            episodeInfo = end[0].split('.')
            episodeSeason = episodeInfo[0]
            episodeNumber = episodeInfo[1]

            print("Crawling episode: ", episodeNumber)
            fileName = Path + "/"+ episodeSeason + "-" + episodeNumber + ".html"

            f = open(fileName, "w+")
            f.write(rawContent)
            f.close()