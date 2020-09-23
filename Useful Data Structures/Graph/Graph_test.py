from Graph_Implimentation import *

#print(buildGraph("words.txt").getVertices())
for v in buildGraph("words2.txt"):
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))