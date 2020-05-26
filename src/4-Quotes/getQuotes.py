import os
import stanza
from bs4 import BeautifulSoup
import csv

# WorkDir
Path = 'Data/6-Quotes/episodes/'
# SrcDir
SrcPath = 'Data/1-HTML/'

# create WorkDir folder if it does not exist
if not os.path.exists(Path):
    os.makedirs(Path)


# Define Seasons
fromSeason = 1
toSeason = 10

def cleanQuote(quote):
    quote = quote.replace('<p>', '')
    quote = quote.replace('</p>', '')
    quote = quote.replace('\n', '')
    quote = quote.replace("'", '')

    return quote

def cleanText(quote):
    quote = quote.replace('<i>', '')
    quote = quote.replace('</i>', '')
    quote = quote.replace('[', '')
    quote = quote.replace(']', '')
    quote = quote.replace('"', '')
    quote = quote.replace('(', '')
    quote = quote.replace(')', '')
    quote = quote.replace('\n', '')

    quote = quote.replace('?', '.')
    quote = quote.replace('!', '.')

    return quote

def cleanElement(quote):
    if(quote[0] == ' '):
        quote = quote[1:]
    
    if(quote[0] == ' '):
        quote = quote[1:]

    # we use ',' as CSV seperator so replace it with space
    quote = quote.replace(',', ' ')

    return quote

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
        f = open(SrcPath + filename, 'r',  errors='ignore')
        episode = f.read()

        # Parse to remove all html tags
        episodeWithoutTags = ''
        soup = BeautifulSoup(episode, 'html.parser')

        if(E <10):
            savename = str(S)+"-"+"0"+str(E)
        else:
            savename = str(S)+"-"+str(E)
        
        # write Cites to CSV
        with open(Path + savename+ '.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Quote"])

        # get all Blockquotes with soup.find_all()
        for quote in soup.find_all("blockquote"): 
            quoteElement = str(quote)

            # remove <blockquote></blockquote> code
            quoteElement = quoteElement[12:-13] 

            # parse Cite split by <br/>
            quoteElements = quoteElement.split('<br/>')
            cites = []
            name = ''

            # get Name and the specific quotes
            for i, element in enumerate(quoteElements):
                if(i == 0):
                    # first Element is always the name
                    name = cleanQuote(element)
                else:
                    element = cleanQuote(element)
                    element = cleanText(element)

                    # Get each Quote by Sentence (split by '.')
                    element = element.split('.')
                    
                    for subElement in element:
                        if(subElement != '.' and subElement != '' and subElement != ' '):
                            cites.append(cleanElement(subElement))

            # write Cites to CSV
            with open(Path + savename+ '.csv', 'a', newline='') as file:
                writer = csv.writer(file)

                for cite in cites:
                    writer.writerow([name, cite])
            
            # remove Quote from HTML
            quote.decompose()
        
        texts = soup.find_all(text=True)

        # write Texts to CSV
        with open(Path + savename+ '.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            for text in texts:
                if(text == '\n'):
                    pass
                    # ignore linebreaks
                else:
                    text = cleanText(text)
                    for cite in cites:
                        writer.writerow(["NoChar", text])

