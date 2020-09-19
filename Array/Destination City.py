'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
 

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.
Start in any city and use the path to move to the next city.
Eventually, you will reach a city with no path outgoing, this is the destination city.

Runtime: 56 ms Beats 68%
Memory Usage: 13.9 MB
'''

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ruled_out = []
        possible = []
        for i in paths:
            ruled_out.append(i[0])
            if i[1] not in ruled_out:
                possible.append(i[1])
        i=0
        while i < len(possible)-1:
            if possible[i] in ruled_out:
                possible.pop(i)
            else:
                i+=1
        #print(ruled_out)
        #print(possible)
        return possible[0]

'''
Runtime: 56 ms
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, end = set(), set()
        for i,j in paths:
            start.add(i), end.add(j)
        return (end-start).pop()

Runtime: 48 ms
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return ({path[1] for path in paths} - {path[0] for path in paths}).pop()

Runtime: 36 ms
from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        arr = defaultdict(lambda : 0)
        
        for path in paths:
            arr[path[0]] += 1
            arr[path[1]] -= 1
            
        for i in arr:
            if arr[i] == -1:
                return i
'''





