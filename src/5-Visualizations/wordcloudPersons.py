# Libraries
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

srcPath = 'Data/4-Entities/counts'
 
# Create a list of word
TextBlock = ""
with open(srcPath + '/' + 'Persons.csv') as csv_file:
    # read current CSV file
    csv_reader = csv.reader(csv_file, delimiter=',')
    # start with first line 
    line_count = 0
    for row in csv_reader:
        # first line is the header
        if line_count == 0:
            line_count += 1
        # others are entities
        else:
            count = int(row[1])
            for i in range(count):
                TextBlock += row[0] + " "

print(TextBlock)
# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(TextBlock)
 
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()