"""
1640. Check Array Formation Through Concatenation
Easy

You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.



Example 1:

Input: arr = [85], pieces = [[85]]
Output: true

Example 2:

Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]

Example 3:

Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].

Example 4:

Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]

Example 5:

Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false



Constraints:

    1 <= pieces.length <= arr.length <= 100
    sum(pieces[i].length) == arr.length
    1 <= pieces[i].length <= arr.length
    1 <= arr[i], pieces[i][j] <= 100
    The integers in arr are distinct.
    The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
"""

#55%
import copy
class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        arr_copy = copy.deepcopy(arr)
        for i in pieces:
            if i[0] not in arr:
                continue
            else:
                if len(i) > 1:
                    ind = arr.index(i[0])
                    count = 1
                    full = True
                    for j in range(1, len(i)):
                        if ind + count >= len(arr) or arr[ind + count] != i[j]:
                            full = False
                            break
                        else:
                            count += 1

                    if full:
                        for j in range(len(i)):
                            arr_copy.remove(i[j])
                        #arr_copy = [e for e in arr_copy if e not in i]
                else:
                    arr_copy.remove(i[0])
            if len(arr_copy) == 0:
                return True
        return False

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.canFormArray(input1,input2)
        print(ans)
        return ans

    assert test([85], [[85]]) == True
    assert test([15,88], [[88],[15]]) == True
    assert test([49, 18, 16], [[16, 18, 49]]) == False
    assert test([91, 4, 64, 78], [[78], [4, 64], [91]]) == True
    assert test([1, 3, 5, 7], [[2, 4, 6, 8]]) == False
    assert test([1,2,3], [[2],[1,3]]) == False

