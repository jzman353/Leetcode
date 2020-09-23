from depth_first_search_DFS_Graph import *

'''
# Test knightTour
g = Graph()
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')
A.addNeighbor(B)
A.addNeighbor(D)
B.addNeighbor(C)
B.addNeighbor(D)
D.addNeighbor(E)
E.addNeighbor(B)
E.addNeighbor(F)
F.addNeighbor(C)
g.addVertex(A)
g.addVertex(B)
g.addVertex(C)
g.addVertex(D)
g.addVertex(E)
g.addVertex(F)
#g.addEdge('A','B')
#g.addEdge('A','D')
#g.addEdge('B','C')
#g.addEdge('B','D')
#g.addEdge('D','E')
#g.addEdge('E','B')
#g.addEdge('E','F')


for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))


path = []
knightTour(0,path,A,5)
'''
'''
# Test General
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')
A.addNeighbor(B)
A.addNeighbor(D)
B.addNeighbor(C)
B.addNeighbor(D)
D.addNeighbor(E)
E.addNeighbor(B)
E.addNeighbor(F)
F.addNeighbor(C)
g = DFSGraph()
g.addVertex(A)
g.addVertex(B)
g.addVertex(C)
g.addVertex(D)
g.addVertex(E)
g.addVertex(F)
g.dfs()

options = [A,B,C,D,E,F]
for i in options:
    print(i.getId())
    print(i.getDiscovery())
    print(i.getFinish())
'''
'''
# Test dijkstra
u = Vertex('u')
v = Vertex('v')
x = Vertex('x')
w = Vertex('w')
y = Vertex('y')
z = Vertex('z')
u.addNeighbor(v,2)
u.addNeighbor(x,1)
u.addNeighbor(w,5)
v.addNeighbor(w,3)
v.addNeighbor(x,2)
x.addNeighbor(w,3)
x.addNeighbor(y,1)
y.addNeighbor(w,1)
y.addNeighbor(z,1)
z.addNeighbor(w,5)
g = Graph()
g.addVertex(u)
g.addVertex(v)
g.addVertex(x)
g.addVertex(w)
g.addVertex(y)
g.addVertex(z)

dijkstra(g,u)

options = [u,v,x,w,y,z]
for i in options:
    print(i.getId())
    print(i.getDistance())
'''
'''
# Test Prim’s Spanning Tree Algorithm
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')
G = Vertex('G')
A.addNeighbor(B,2)
B.addNeighbor(A,2)
A.addNeighbor(C,3)
C.addNeighbor(A,3)
B.addNeighbor(C,1)
C.addNeighbor(B,1)
B.addNeighbor(D,1)
D.addNeighbor(B,1)
B.addNeighbor(E,4)
E.addNeighbor(B,4)
D.addNeighbor(E,1)
E.addNeighbor(D,1)
C.addNeighbor(F,5)
F.addNeighbor(C,5)
E.addNeighbor(F,1)
F.addNeighbor(E,1)
F.addNeighbor(G,1)
G.addNeighbor(F,1)
g = Graph()
g.addVertex(A)
g.addVertex(B)
g.addVertex(C)
g.addVertex(D)
g.addVertex(E)
g.addVertex(F)
g.addVertex(G)
prim(g,A)

options = [A,B,C,D,E,F,G]
for i in options:
    print(i.getId())
    print("Previous node: "+str(i.getPred()))
    dist = i.getDistance()
    print("Distance from previous node: "+str(dist))
    node_dist = dist
    if i.getPred():
        k = i
        while k.getPred():
            node_dist += k.getPred().getDistance()
            k = k.getPred()
    print("Total distance from starting node: "+str(node_dist))
'''