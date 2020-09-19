'''
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000

Return an array where the values are symmetric. (+x , -x).
If n is odd, append value 0 in your returned array.

Runtime: 24 ms Beats 97%
Memory Usage: 12.6 MB
'''

class Solution:
    def sumZero(self, n: int) -> List[int]:
        even=0
        result=[]
        if n%2==1:  
            count=0
            for i in range(n):
                if even==0:
                    result.append(-1*count)
                    even=1
                else:
                    count=count+1
                    result.append(count)
                    even=0
        else:
            count=1
            for i in range(int(n/2)):
                result.append(count)
                result.append(-1*count)
                count=count+1
        return result
        
'''
Runtime: 12 ms
class Solution:
    def sumZero(self, n: int) -> List[int]:
        new_list = []
        for i in range(n-1):
            new_list.append(i)
        last_num = sum(new_list)*-1
        new_list.append(last_num)
        return new_list
'''


