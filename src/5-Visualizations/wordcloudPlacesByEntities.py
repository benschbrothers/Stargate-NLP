# Libraries
import csv
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

srcPath = 'Data/4-Entities/counts'
maskPath = "Resources/map"

dictP = {}
with open(srcPath + '/Places_Clean.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter=',')
    line_count = 0
    for row in reader:
        # first line is the header
        if line_count == 0:
            line_count += 1
        # others are entities
        else:
            dictP[row[0]] = int(row[1])

# Create the wordcloud object
mask = np.array(Image.open(maskPath+"/" + "ChevronEarth.png"))
wordcloud = WordCloud(background_color="black", width=800, height=500, colormap='Blues', mask=mask)
wordcloud.generate_from_frequencies(frequencies=dictP)
 
# Display the generated image:
plt.imshow(wordcloud)
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()