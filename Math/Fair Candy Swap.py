"""
888. Fair Candy Swap
Easy

Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.

Example 1:

Input: aliceSizes = [1,1], bobSizes = [2,2]
Output: [1,2]
Example 2:

Input: aliceSizes = [1,2], bobSizes = [2,3]
Output: [1,2]
Example 3:

Input: aliceSizes = [2], bobSizes = [1,3]
Output: [2,3]

Constraints:

1 <= aliceSizes.length, bobSizes.length <= 104
1 <= aliceSizes[i], bobSizes[j] <= 105
Alice and Bob have a different total number of candies.
There will be at least one valid answer for the given input.
"""
#56%
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        avg = (sum_alice+sum_bob)//2
        d_alice = sum_alice-avg
        s_alice = set(aliceSizes)
        s_bob = set(bobSizes)
        #print(sum_alice,sum_bob,avg,sum_alice-avg,sum_bob-avg)
        for i in s_alice:
            if -(d_alice-i) in s_bob:
                return [i, -(d_alice-i)]

"""
sample 339 ms submission
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice, sum_bob = sum(aliceSizes), sum(bobSizes)
        set_bob = set(bobSizes)
        for i in aliceSizes:
            potential = i + (sum_bob  - sum_alice) / 2
            if potential in set_bob:
                return [i, potential]

Approach 1: Solve the Equation
Intuition

If Alice swaps candy x, she expects some specific quantity of candy y back.

Algorithm

Say Alice and Bob have total candy S_A, S_BS 
A
 ,S 
B
  respectively.

If Alice gives candy xx, and receives candy yy, then Bob receives candy xx and gives candy yy. Then, we must have

S_A - x + y = S_B - y + xS 
A
 −x+y=S 
B
 −y+x

for a fair candy swap. This implies

y = x + \frac{S_B - S_A}{2}y=x+ 
2
S 
B
 −S 
A
 
 

Our strategy is simple. For every candy xx that Alice has, if Bob has candy y = x + \frac{S_B - S_A}{2}y=x+ 
2
S 
B
 −S 
A
 
 , we return [x, y][x,y]. We use a Set structure to check whether Bob has the desired candy yy in constant time.

class Solution(object):
    def fairCandySwap(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]

Complexity Analysis

Time Complexity: O(A\text{.length} + B\text{.length})O(A.length+B.length).

Space Complexity: O(B\text{.length})O(B.length), the space used by setB. (We can improve this to \min(A\text{.length}, B\text{.length})min(A.length,B.length) by using an if statement.)
"""