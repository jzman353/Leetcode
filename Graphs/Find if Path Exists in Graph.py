"""
1971. Find if Path Exists in Graph
Easy

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex start to vertex end.

Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= start, end <= n - 1
There are no duplicate edges.
There are no self edges.
"""

#68%
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        self.seen = set()
        d = defaultdict(set)
        for i in edges:
            d[i[0]].add(i[1])
            d[i[1]].add(i[0])

        def recursive(vertex):
            self.seen.add(vertex)
            if end in d[vertex] or end in self.seen:
                self.seen.add(end)
                return
            for i in d[vertex]:
                if i not in self.seen:
                    recursive(i)

        recursive(start)
        return end in self.seen


"""
This solution is verysimilar to mine. They don't stop the recursion early if end is in seen but they have a useful check at the start
sample 1432 ms submission
class Solution:
    def dfs(self, s, vis, adj):
        vis.add(s)
        for n in adj[s]:
            if n not in vis:
                self.dfs(n, vis, adj)
                
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end or [start, end] in edges:
            return True
    
        adj = defaultdict(list)
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)
            
        vis = set()
        self.dfs(start, vis, adj)
        return end in vis
"""