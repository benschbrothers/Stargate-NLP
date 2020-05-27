
import csv
import numpy as np
import matplotlib.pyplot as plt

srcPath = 'Data/8-MostMentioned'

dictM = {}
with open(srcPath + '/MostSocial.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter=',')
    counter = 0
    for row in reader:
        # first line is the header
        if counter == 0:
            counter += 1
        # others are entities
        else:
            counter += 1
            if(counter <= 20):
                dictM[row[0]] = int(row[1])


# ax = x.plot(kind='barh', figsize=(8, 10), color='#86bf91', zorder=2, width=0.85)
keys = list(dictM.keys())
values = list(dictM.values())

ax = plt
ax.barh(keys, values,  height=0.5)

# Switch off ticks
ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")


# Despine
ax.gca().spines['right'].set_position(('data',0))
ax.gca().spines['top'].set_position(('data',0))
ax.gca().spines['left'].set_position(('data',0))
ax.gca().spines['bottom'].set_position(('data',0))

# # Draw vertical axis lines
# vals = ax.get_xticks()
# for tick in vals:
#     ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

# Set x-axis label
ax.title("Most social")
ax.xlabel("characters mentioned", labelpad=20, weight='bold', size=12)

# # Set y-axis label
ax.ylabel("Character", labelpad=20, weight='bold', size=12)

# Format y-axis label
# ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))


ax.show()