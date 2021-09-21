"""
1791. Find Center of Star Graph
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

Example 1:

Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1

Constraints:

3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
"""
#54%
class Solution:
    def findCenter(self, edges) -> int:
        return list(set(edges[1]).intersection(set(edges[0])))[0]
"""
#15%
#edges: List[List[int]]
import collections

class Solution:
    def findCenter(self, edges) -> int:
        c = collections.Counter()
        for i in edges[:2]:
            for j in i:
                c[j] += 1
        return c.most_common(1)[0][0]
        
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return list((set(edges[1]) & set(edges[0])))[0]
"""
"""
#9%
#edges: List[List[int]]
import collections

class Solution:
    def findCenter(self, edges) -> int:
        c = collections.Counter()
        for i in edges:
            for j in i:
                c[j] += 1
        return c.most_common(1)[0][0]
"""
"""
The center is the only node that has more than one edge.
The center is also connected to all other nodes.
Any two edges must have a common node, which is the center.
"""
"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x,y = edges[0][0], edges[0][1]
        if x==edges[1][0] or x == edges[1][1]:
            return x
        return y

return (set(edges[0]) & set(edges[1])).pop()
"""