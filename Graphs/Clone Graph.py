"""
133. Clone Graph
Medium

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.


Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""

def to_graph(adjList):
    if not adjList:
        return None
    nodes = [Node(i+1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    return nodes[0]

def to_adjList(node):
    if not node:
        return []
    visited = {}
    queue = [node]
    while queue:
        curr = queue.pop(0)
        if curr.val in visited:
            continue
        visited[curr.val] = [n.val for n in curr.neighbors]
        queue.extend(curr.neighbors)
    return [visited[i] for i in sorted(visited.keys())]

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        copied_nodes = {1: Node(node.val)}

        def helper(node, copy):
            for vertex in node.neighbors:
                if vertex.val not in copied_nodes.keys():
                    copied_nodes[vertex.val] = Node(vertex.val)
                    helper(vertex, copied_nodes[vertex.val])
                copy.neighbors.append(copied_nodes[vertex.val])
            return copy

        return helper(node, copied_nodes[1])

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.cloneGraph(to_graph(input1))
        print(to_adjList(ans))
        return to_adjList(ans)


    assert test([]) == []  # empty graph
    assert test([[]]) == [[]]  # single node no neighbors
    assert test([[2], [1]]) == [[2], [1]]  # two nodes
    assert test([[2, 4], [1, 3], [2, 4], [1, 3]]) == [[2, 4], [1, 3], [2, 4], [1, 3]]  # example 1
    assert test([[2, 3], [1, 3], [1, 2]]) == [[2, 3], [1, 3], [1, 2]]  # triangle
    assert test([[2], [1, 3], [2]]) == [[2], [1, 3], [2]]  # linear 3 nodes
    print("All tests passed!")

"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = deque([node])
        new = Node(node.val)
        copies = {node: new}

        while q:
            node = q.popleft()
            node_copy = copies[node]
            for neighbor in node.neighbors:
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                node_copy.neighbors.append(copies[neighbor])

        return new
"""