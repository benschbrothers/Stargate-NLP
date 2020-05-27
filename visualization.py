import os
import csv


# work path
Path = 'Data/'

# create workdir folder if it does not exist
if not os.path.exists(Path):
    os.makedirs(Path)                                                 

print('Visualizations script start!')

# Drawing ListNames WordCloud
print('Running ListName WordCloud')
os.system('python src/5-Visualizations/wordcloudPersonQuotes.py')

# Drawing TF-IDF WordCloud
print('Running TF-IDF WordClouds')
os.system('python src/6-TFIDF/tfidf.py tealc')
os.system('python src/6-TFIDF/tfidf.py carter')
os.system('python src/6-TFIDF/tfidf.py fraiser')

# Drawing Network Figure
print('Running Network')
os.system('python src/9-Network/network.py')

print('Visualizations script done!')