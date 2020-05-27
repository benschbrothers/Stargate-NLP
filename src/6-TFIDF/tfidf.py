import pandas as pd
import numpy as np
import csv
import re
import sys
import os
import nltk

from nltk.corpus import stopwords
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from PIL import Image

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Set default target person to oneill
targetPerson = "tealc"

# Get the target person
if(len(sys.argv) == 2):
    targetPerson = sys.argv[1]
else:
    print("no target person specified! taking tealc")

# WorkDir
Path = 'Data/7-TFIDF/'
# SrcDir
SrcPath = 'Data/6-Quotes/episodes/'

# SrcDirGit
SrcPathGit = 'Src/6-TFIDF/'

# MaskGit
MaskPathGit = 'Resources/masks/'

# create WorkDir folder if it does not exist
if not os.path.exists(Path):
    os.makedirs(Path)

# Define Seasons
fromSeason = 1
toSeason = 10

# regex for names
regex = re.compile('[^a-zA-Z0-9]')

# All Quotes in dne Series
dictAllQuotes= [] 

for S in range(fromSeason,toSeason+1):
    if(S < 8):
        maxEpisodes = 22
    else:
        maxEpisodes = 20
    
    # All Quotes of the Season
    dictSeasonQuotes = [] 
    for E in range(1, maxEpisodes+1):
        if(E <10):
            filename = str(S)+"-"+"0"+str(E)
        else:
            filename = str(S)+"-"+str(E)

        # All Quotes of the Episode
        dictEpisodeQuotes = [] 

        with open(SrcPath + filename + ".csv") as csv_file:
            # read current CSV file
            csv_reader = csv.reader(csv_file, delimiter=',')
            # start with first line 
            line_count = 0
            for row in csv_reader:
                # first line is the header
                if line_count == 0:
                    # print(f'Column names are {", ".join(row)}')
                    line_count += 1
                # others are entities
                else:
                    # everything to lower space
                    name = row[0].lower()
                    # remove characters that are not needed
                    name = regex.sub('', name)

                    if (name  == targetPerson):
                        quote = row[1].lower()
                        dictEpisodeQuotes.append(quote)


        dictSeasonQuotes.extend(dictEpisodeQuotes)

    dictAllQuotes.extend(dictSeasonQuotes)

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)
 
    
def extract_topn_from_vector(feature_names, sorted_items, topn):
    
    #use only topn items from vector
    sorted_items = sorted_items[:topn]
 
    score_vals = []
    feature_vals = []
    
    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        
        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])
 
    #create a dictionary of feature,score
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

def keyWords(corpus, topN):
    
    # my_stop_words = set( stopwords.words('english') ).union( set(text.ENGLISH_STOP_WORDS) )

    # my_stop_words = my_stop_words.union(["dont", "im", "didnt", "your", "want", "thats", "just", "know", "youre", "going"])
    my_stop_words2 = []
    with open(SrcPathGit+'stopwords.txt', encoding='utf-8') as file:
        for line in file: 
            line = line.replace("'", '')
            line = line.replace('\n', '')
            my_stop_words2.append(line) #storing everything in memory!

    # print(my_stop_words2)
    my_stop_words = frozenset(my_stop_words2)
    cv=CountVectorizer(max_df=0.9,stop_words=my_stop_words)
    #cv=CountVectorizer(max_df=0.85)
    word_count_vector=cv.fit_transform(corpus)

    tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
    tfidf_transformer.fit(word_count_vector)

    # you only needs to do this once, this is a mapping of index to 
    feature_names=cv.get_feature_names()
    
    #generate tf-idf for the given document
    tf_idf_vector=tfidf_transformer.transform(cv.transform([listToString(corpus)]))
    
    #sort the tf-idf vectors by descending order of scores
    sorted_items=sort_coo(tf_idf_vector.tocoo())
    
    #extract only the top n; n here is 10
    keywords=extract_topn_from_vector(feature_names,sorted_items,100)

    return keywords


dictP= keyWords(dictAllQuotes, 100)
print(dictP)
# Create the wordcloud object
if targetPerson == 'tealc':
    mask = np.array(Image.open(MaskPathGit+"tealc.png"))
elif targetPerson == 'carter':
    mask = np.array(Image.open(MaskPathGit+"carter.png"))
elif targetPerson == 'fraiser':
    mask = np.array(Image.open(MaskPathGit+"fraiser.png"))
else:
    mask = np.array(Image.open(MaskPathGit+"mask.png"))
wordcloud = WordCloud(background_color="black", width=800, height=500, colormap='Blues', mask=mask)
wordcloud.generate_from_frequencies(frequencies=dictP)
 
# Display the generated image:
plt.imshow(wordcloud)
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()