import os
import csv

# work path
Path = 'Data/'

# create workdir folder if it does not exist
if not os.path.exists(Path):
    os.makedirs(Path)


# Getting all HTML Files per Episode
print('Running HTML Crawler')
os.system('python src/1-Crawler/crawler.py')
os.system('python src/1-Crawler/extractRawText.py')
os.system('python src/1-Crawler/happinessCSV.py')

# Running Quotes Scripts
print('Running Quote Scripts')
os.system('python src/4-Quotes/mainQuotes.py')

# Running Entity-Tagging Scripts
print('Running Entity Tagger Scripts')
os.system('python src/3-Entity/entity-extractionPerEpisode.py')
os.system('python src/3-Entity/countEntities.py')
os.system('python src/3-Entity/countCleanUpNicknames.py')

# Running POS-Tagging Scripts
print('Running POS Tagger Scripts')
os.system('python src/2-Pos/pos-taggingPerEpisode.py')

# Running Most mentioned Scripts
print('Running Most mentioned Tagger Scripts')
os.system('python src/7-MostMentioned/mostMentionedRunner.py')

# Running Happiness Script
print('Running Hapiness Tagger Scripts')
os.system('python src/8-Happiness/happiness.py')

print('Main script done!')