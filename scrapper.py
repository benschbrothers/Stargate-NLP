import os
import numpy as np
import requests


url = 'http://www.stargate-sg1-solutions.com/wiki/1.01_%22Children_Of_The_Gods_Part_1%22_Transcript'
html = requests.get(url)
content = html.text
f = open("Season1-1.txt", "a")

start = content.split('<h2><span class="mw-headline" id="Transcript">Transcript</span></h2>')

end = start[1].split('<h2><span class="mw-headline" id="Related_Articles">Related Articles</span></h2>')
rawContent = end[0]

print(rawContent)

f.write(rawContent)
f.close()
