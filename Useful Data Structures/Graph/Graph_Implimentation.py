import sys

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize  # distance
        self.pred = None  # predecessor
        # The discovery time tracks the number of steps in the algorithm
        # before a vertex is first encountered.
        self.disc = 0  # discovery
        # The finish time is the number of steps in the algorithm
        # before a vertex is colored black.
        self.fin = 0  # finish times

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getId(self):
        return self.id

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

'''
g = Graph()
for i in range(6):
    g.addVertex(i)
'''
'''
    >>> g.vertList
    {0: <adjGraph.Vertex instance at 0x41e18>,
     1: <adjGraph.Vertex instance at 0x7f2b0>,
     2: <adjGraph.Vertex instance at 0x7f288>,
     3: <adjGraph.Vertex instance at 0x7f350>,
     4: <adjGraph.Vertex instance at 0x7f328>,
     5: <adjGraph.Vertex instance at 0x7f300>}
'''
'''
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
'''
'''
    ( 0 , 5 )
    ( 0 , 1 )
    ( 1 , 2 )
    ( 2 , 3 )
    ( 3 , 4 )
    ( 3 , 5 )
    ( 4 , 0 )
    ( 5 , 4 )
    ( 5 , 2 )
'''




