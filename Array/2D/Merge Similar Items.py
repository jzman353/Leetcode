"""
2363. Merge Similar Items
Easy

You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:

items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
The value of each item in items is unique.
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

Note: ret should be returned in ascending order by value.

Example 1:

Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
Output: [[1,6],[3,9],[4,5]]
Explanation:
The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
The item with value = 4 occurs in items1 with weight = 5, total weight = 5.
Therefore, we return [[1,6],[3,9],[4,5]].
Example 2:

Input: items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
Output: [[1,4],[2,4],[3,4]]
Explanation:
The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 3, total weight = 1 + 3 = 4.
The item with value = 2 occurs in items1 with weight = 3 and in items2 with weight = 1, total weight = 3 + 1 = 4.
The item with value = 3 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
Therefore, we return [[1,4],[2,4],[3,4]].
Example 3:

Input: items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]
Output: [[1,7],[2,4],[7,1]]
Explanation:
The item with value = 1 occurs in items1 with weight = 3 and in items2 with weight = 4, total weight = 3 + 4 = 7.
The item with value = 2 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
The item with value = 7 occurs in items2 with weight = 1, total weight = 1.
Therefore, we return [[1,7],[2,4],[7,1]].

Constraints:

1 <= items1.length, items2.length <= 1000
items1[i].length == items2[i].length == 2
1 <= valuei, weighti <= 1000
Each valuei in items1 is unique.
Each valuei in items2 is unique.
"""

#100%
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        t1 = dict(items1)
        t2 = dict(items2)

        for i in t2:
            if i in t1.keys():
                t1[i] += t2[i]
            else:
                t1[i] = t2[i]

        ans = []
        for i in t1:
            ans.append([i, t1[i]])

        return sorted(ans)

"""
9%
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        flatten_list = list(chain.from_iterable(items1))
        values = flatten_list[::2]
        for i in items2:
            try:
                inx = values.index(i[0])
                items1[inx][1] += i[1]
            except:
                items1.append(i)

        items1.sort()
        return items1
"""

import random
def test_cases():
    length1 = random.randint(1,1000)
    length2 = random.randint(1, 1000)
    possibilities = [i for i in range(1,1000)]
    samplev1 = random.sample(possibilities, length1)
    samplev2 = random.sample(possibilities, length2)
    samplec1 = random.choices(possibilities,k=length1)
    samplec2 = random.choices(possibilities, k=length1)

    list1 = [list(a) for a in zip(samplev1,samplec1)]
    list2 = [list(a) for a in zip(samplev2, samplec2)]
    print(list1)
    print(list2)


for i in range(8):
    test_cases()