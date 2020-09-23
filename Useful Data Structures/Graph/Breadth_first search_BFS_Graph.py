import sys
sys.path.append('../')
#https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

from Queue import Queue
from Graph_Implimentation import *

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

g = buildGraph("words2.txt")

bfs(g,g.getVertex('fool'))
traverse(g.getVertex('sage'))