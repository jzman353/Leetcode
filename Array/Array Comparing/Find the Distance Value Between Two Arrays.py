"""
1385. Find the Distance Value Between Two Arrays
Easy

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation:
For arr1[0]=4 we have:
|4-10|=6 > d=2
|4-9|=5 > d=2
|4-1|=3 > d=2
|4-8|=4 > d=2
For arr1[1]=5 we have:
|5-10|=5 > d=2
|5-9|=4 > d=2
|5-1|=4 > d=2
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1

Constraints:

1 <= arr1.length, arr2.length <= 500
-10^3 <= arr1[i], arr2[j] <= 10^3
0 <= d <= 100
"""
#48%
import bisect
class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        arr2.sort()
        answer = 0
        for i in range(len(arr1)):
            x = bisect.bisect_left(arr2, arr1[i])-1
            y = bisect.bisect_left(arr2, arr1[i])
            if y == len(arr2):
                if abs(arr2[-1]-arr1[i]) > d:
                    answer += 1
            elif abs(arr2[x]-arr1[i]) > d and abs(arr2[y]-arr1[i]) > d:
                answer += 1
        return answer

if __name__ == '__main__':
    def test(input1, input2, input3):
        Test = Solution()
        ans = Test.findTheDistanceValue(input1, input2, input3)
        print(ans)
        return ans


    assert test([4,5,8], [10,9,1,8], 2) == 2
    assert test([1,4,2,3], [-4,-3,6,10,20,30], 3) == 2
    assert test([2,1,100,3], [-5,-2,10,-3,7], 6) == 1
    assert test([-803,715,-224,909,121,-296,872,807,715,407,94,-8,572,90,-520,-867,485,-918,-827,-728,-653,-659,865,102,-564,-452,554,-320,229,36,722,-478,-247,-307,-304,-767,-404,-519,776,933,236,596,954,464],[817,1,-723,187,128,577,-787,-344,-920,-168,-851,-222,773,614,-699,696,-744,-302,-766,259,203,601,896,-226,-844,168,126,-542,159,-833,950,-454,-253,824,-395,155,94,894,-766,-63,836,-433,-780,611,-907,695,-395,-975,256,373,-971,-813,-154,-765,691,812,617,-919,-616,-510,608,201,-138,-669,-764,-77,-658,394,-506,-675,523,730,-790,-109,865,975,-226,651,987,111,862,675,-398,126,-482,457,-24,-356,-795,-575,335,-350,-919,-945,-979,611],37) == 0
    assert test([2,6],[-10,9,2,-1],2) == 1

"""
Looks almost the same as mine but one less bisect calculation (mine is redundant in this way)
sample 56 ms submission
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        distance = 0
        for num1 in arr1:
            index = bisect_left(arr2, num1)
            if index == 0:
                if abs(arr2[0] - num1) > d:
                    distance += 1
            elif index == len(arr2):
                if abs(arr2[-1] - num1) > d:
                    distance += 1
            else:
                if abs(arr2[index] - num1) > d and abs(arr2[index - 1] - num1) > d:
                    distance += 1
        return distance

My revised code:
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        answer = 0
        for i in range(len(arr1)):
            x = bisect.bisect_left(arr2, arr1[i])-1
            if x+1 == len(arr2):
                if abs(arr2[-1]-arr1[i]) > d:
                    answer += 1
            elif abs(arr2[x]-arr1[i]) > d and abs(arr2[x+1]-arr1[i]) > d:
                answer += 1
        return answer
"""