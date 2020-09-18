#10%

"""
Count Unhappy Friends (Medium)

You are given a list of preferences for n friends, where n is always even.

For each person i, preferences[i] contains a list of friends sorted in the order of preference. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1.

All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.

However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is paired with y and there exists a friend u who is paired with v but:

    x prefers u over y, and
    u prefers x over v.

Return the number of unhappy friends.



Example 1:

Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
Output: 2
Explanation:
Friend 1 is unhappy because:
- 1 is paired with 0 but prefers 3 over 0, and
- 3 prefers 1 over 2.
Friend 3 is unhappy because:
- 3 is paired with 2 but prefers 1 over 2, and
- 1 prefers 3 over 0.
Friends 0 and 2 are happy.

Example 2:

Input: n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
Output: 0
Explanation: Both friends 0 and 1 are happy.

Example 3:

Input: n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
Output: 4



Constraints:

    2 <= n <= 500
    n is even.
    preferences.length == n
    preferences[i].length == n - 1
    0 <= preferences[i][j] <= n - 1
    preferences[i] does not contain i.
    All values in preferences[i] are unique.
    pairs.length == n/2
    pairs[i].length == 2
    xi != yi
    0 <= xi, yi <= n - 1
    Each person is contained in exactly one pair.

"""

class Solution:
    def __init__(self):
        pass
    def unhappyFriends(self, n: int, preferences, pairs) -> int:
        dict1 = {}
        unhappy_friends = []
        for pair in pairs:
            if pair[1] == preferences[pair[0]][0] and pair[0] == preferences[pair[1]][0]:
                continue
            else:
                dict1[pair[0]] = preferences[pair[0]][:preferences[pair[0]].index(pair[1])]
                dict1[pair[1]] = preferences[pair[1]][:preferences[pair[1]].index(pair[0])]
        #friend, list of friends closer than their chosen pair person
        for key, value in dict1.items():
            #If they can be happier
            if value:
                #For each person they would be happier with (person)
                for person in value:
                    if key in dict1[person]:
                        if key not in unhappy_friends:
                            unhappy_friends.append(key)
                        if person not in unhappy_friends:
                            unhappy_friends.append(person)
        return len(unhappy_friends)

        #print(dict1)
        #print(unhappy_friends)


def test(n, preferences, pairs):
    Test = Solution()
    print(Test.unhappyFriends(n, preferences, pairs))

n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]
test(n, preferences, pairs) #2

n = 2
preferences = [[1], [0]]
pairs = [[1, 0]]
test(n, preferences, pairs) #0

n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]
test(n, preferences, pairs) #4

"""
def unhappyFriends(self, n: int, pres: List[List[int]], pairs: List[List[int]]) -> int:
        f = collections.defaultdict(int)
        ans = 0
        for u, v in pairs:
            f[u] = v
            f[v] = u
        
        def count(x):
            y = f[x]
            for u in pres[x]:
                if u == y:
                    break
                for pre in pres[u]:
                    if pre == f[u]:
                        break
                    if pre == x:
                        return 1
            return 0
        
        return sum(count(i) for i in range(n))
"""