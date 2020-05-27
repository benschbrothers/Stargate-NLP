import matplotlib.pyplot as plt
import networkx as nx

import os
import csv

# WorkDir
Path = 'Src/7-MostMentioned'

# SrcDir
SrcPath = 'Data/6-Quotes'

# SrcDirMentioned
SrcPath2 = 'Data/8-MostMentioned/by/'

# define a function to calculate the Network
def getNetwork():
    
    # Weights are Stored in a List
    # (Name1, Name2), value = mentionedAmount
    edgeWeights={}

    # Nodes are Top 50 Names
    nodes={}
    nameList=[]

    with open(SrcPath + '/' + "ListNames.csv") as csv_file:
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
                # only add top 50 characters
                if line_count <= 51:
                    name = row[0]
                    nameList.append(name)
                    if name == "oneill" or name == "carter" or name == "daniel" or name == "tealc":
                        nodes[name] = {"Team" : "SG1", "Color": "#33ff33", "counts": row[1]} # SG 1 is green
                    elif name == "baal" or name == "apophis":
                        nodes[name] = {"Team" : "Systemlords", "Color": "#ff3333", "counts": row[1]} # Systemlords red
                    else:
                        nodes[name] = {"Team" : "others", "Color": "#a9a9a9", "counts": row[1]} # unclassified

                    with open(SrcPath2 + name + ".csv") as csv_file:
                        # read current CSV file
                        csv_reader2 = csv.reader(csv_file, delimiter=',')
                        # start with first line 
                        line_count2 = 0
                        for row2 in csv_reader2:
                            # first line is the header
                            if line_count2 == 0:
                                line_count2 += 1
                            # others are entities
                            else:
                                if row2[0] in nameList:
                                    edgeWeights[(name, row2[0])]=row2[1]  
                                    #edgeWeights[(row2[0], name)]=row2[1]  
                line_count += 1 

    return edgeWeights, nodes

edgeWightDic, nodes = getNetwork()
#print(edgeWightDic)

# build a directed graph 
G=nx.DiGraph()
G.add_nodes_from(list(nodes.items()))
G.add_edges_from([(k[0],k[1],{"weight" : v}) for (k,v) in edgeWightDic.items()])

# Color list
colorList = [nodes[name]["Color"] for name in nodes]

# Node Size list
# sizeList = [0.0005 *nodes[name]["counts"] for name in nodes]

positions = nx.circular_layout(G)
# Label list
labeling={}


# Plot a network graph
plt.figure(figsize=(15,10))
plt.axis("off")
nx.draw_networkx(G, positions, cmap=plt.get_cmap('jet'), node_size=800, with_labels=True, node_color = colorList, edge_color='#0033CC')
plt.title("Character network in Stargate", fontweight='bold')
plt.savefig('Characters_network.png')
plt.show()