"""
2379. Minimum Recolors to Get K Consecutive Black Blocks
Easy

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
"""

#100%
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cur = blocks[:k]
        cur_w = cur.count("W")
        minn = cur_w
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                cur_w += 1
            if cur[0] == 'W':
                cur_w -= 1
                minn = min(minn,cur_w)
                if minn == 0: return 0

            cur = cur[1:]+blocks[i]

        return minn

"""
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans=[]
        i=0
        while i<len(blocks)-k+1:
            temp=blocks[i:i+k]
            ans.append(temp.count('W'))
            i=i+1
        return min(ans)
"""

"""
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cur = blocks[:k]
        cur_b = cur.count("B")
        minn = cur_b
        for i in range(k, len(blocks)):
            print(cur)
            if cur[0] == 'B':
                cur_b -= 1
                minn = min(minn,cur_b)
            if blocks[i] == "B":
                cur_b += 1

            cur = cur[1:]+blocks[i]

        print(cur)
        return minn
"""
import random
def test_cases():
    n = random.randint(1,100)
    blocks = "".join(random.choices(['B','W'],k=n))
    k = random.randint(1,n)
    print('"'+blocks+'"')
    print(k)

for i in range(8):
    test_cases()

"""
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        combined = []
        white = blocks[0] == 'W'
        count = 0
        for i in blocks:
            if i == 'W':
                if white:
                    count += 1
                else:
                    combined.append(count)
                    count = 1
                    white = True
            else:
                if not white:
                    count -= 1
                else:
                    combined.append(count)
                    count = -1
                    white = False
        combined.append(count)
        
        print(combined)
"""