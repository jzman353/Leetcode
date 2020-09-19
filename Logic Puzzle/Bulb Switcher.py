'''
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.

Runtime: 40 ms Beats 11%
Memory Usage: 13.9 MB
'''

class Solution:
    def bulbSwitch(self, n: int) -> int:
        #[1,1,1,1,1,1,1,1,1,1]
        #[1,0,1,0,1,0,1,0,1,0]
        #[1,0,0,0,1,1,1,0,0,0]
        #[1,0,0,1,1,1,1,1,0,0]
        #[1,0,0,1,0,1,1,1,0,1]
        #[1,0,0,1,0,0,1,1,0,1]
        #[1,0,0,1,0,0,0,1,0,1]
        #[1,0,0,1,0,0,0,0,0,1]
        #[1,0,0,1,0,0,0,0,1,1]
        #[1,0,0,1,0,0,0,0,1,0]
        if n==0:
            return 0
        i = 1
        while ((i+1)**2)<=n:
            i+=1
        return i
        '''
        if n==0:
            return 0
        total_on = 1
        
        if n>=4:
            for i in range(4,n+1):
                if (i**(1/2)).is_integer():
                    total_on += 1
        return total_on
        '''
'''
Runtime: 16ms
class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 1
        
        while res * res <= n:
            res += 1
        
        return res - 1
'''




        