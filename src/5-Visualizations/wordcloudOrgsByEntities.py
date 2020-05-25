# Libraries
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

srcPath = 'Data/4-Entities/counts'

dictO = {}
with open(srcPath + '/Orgs_Clean.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter=',')
    line_count = 0
    for row in reader:
        # first line is the header
        if line_count == 0:
            line_count += 1
        # others are entities
        else:
            dictO[row[0]] = int(row[1])

# Create the wordcloud object
wordcloud = WordCloud(background_color="white", width=800, height=500, colormap='Blues')
wordcloud.generate_from_frequencies(frequencies=dictO)
 
# Display the generated image:
plt.imshow(wordcloud)
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()