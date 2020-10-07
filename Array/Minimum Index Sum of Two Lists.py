"""
48%
599. Minimum Index Sum of Two Lists
Easy

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.



Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Example 3:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 4:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 5:

Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]



Constraints:

    1 <= list1.length, list2.length <= 1000
    1 <= list1[i].length, list2[i].length <= 30
    list1[i] and list2[i] consist of spaces ' ' and English letters.
    All the stings of list1 are unique.
    All the stings of list2 are unique.

Accepted
97,856
Submissions
192,128
"""

class Solution:
    def findRestaurant(self, list1, list2):
        length = max(len(list1),len(list2))
        d = {}
        for i in range(length):
            if i<len(list1) and list1[i] in d.keys():
                d[list1[i]] = (True, d[list1[i]][1]+i)
            elif i<len(list1) and list1[i] not in d.keys():
                d[list1[i]] = (False, i)
            if i<len(list2) and list2[i] in d.keys():
                d[list2[i]] = (True, d[list2[i]][1]+i)
            elif i<len(list2) and list2[i] not in d.keys():
                d[list2[i]] = (False, i)

        import math
        minn = math.inf
        for key, value in d.items():
            if value[0]:
                minn = min(value[1],minn)
        ans = []
        for key, value in d.items():
            if value[0]:
                if value[1] == minn:
                    ans.append(key)
        return ans

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.findRestaurant(input1,input2)
        print(ans)

    input1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    input2 = ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]
    test(input1, input2) #["KFC","Burger King","Tapioca Express","Shogun"]

    #import timit
    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))