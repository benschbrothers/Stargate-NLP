# Libraries
import csv
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

srcPath = 'Data/6-Quotes/'

# SrcDirGit
SrcPathGit = 'Src/6-TFIDF/'
 
dictP = {}
with open(srcPath + 'ListNames.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter=',')
    line_count = 0
    for row in reader:
        # first line is the header
        if line_count == 0:
            line_count += 1
        # others are entities
        else:
            dictP[row[0]] = int(row[1])

# print(dictP)
# Create the wordcloud object

mask = np.array(Image.open(SrcPathGit+"mask.png"))

wordcloud = WordCloud(background_color="Black", width=800, height=500, colormap='Blues', mask=mask)
wordcloud.generate_from_frequencies(frequencies=dictP)
 
# Display the generated image:
plt.imshow(wordcloud)
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()