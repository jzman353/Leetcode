"""
1503. Last Moment Before All Ants Fall Out of a Plank
Medium

We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with speed 1 unit per second. Some of the ants move to the left, the other move to the right.

When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions doesn't take any additional time.

When an ant reaches one end of the plank at a time t, it falls out of the plank imediately.

Given an integer n and two integer arrays left and right, the positions of the ants moving to the left and the right. Return the moment when the last ant(s) fall out of the plank.



Example 1:

Input: n = 4, left = [4,3], right = [0,1]
Output: 4
Explanation: In the image above:
-The ant at index 0 is named A and going to the right.
-The ant at index 1 is named B and going to the right.
-The ant at index 3 is named C and going to the left.
-The ant at index 4 is named D and going to the left.
Note that the last moment when an ant was on the plank is t = 4 second, after that it falls imediately out of the plank. (i.e. We can say that at t = 4.0000000001, there is no ants on the plank).

Example 2:

Input: n = 7, left = [], right = [0,1,2,3,4,5,6,7]
Output: 7
Explanation: All ants are going to the right, the ant at index 0 needs 7 seconds to fall.

Example 3:

Input: n = 7, left = [0,1,2,3,4,5,6,7], right = []
Output: 7
Explanation: All ants are going to the left, the ant at index 7 needs 7 seconds to fall.

Example 4:

Input: n = 9, left = [5], right = [4]
Output: 5
Explanation: At t = 1 second, both ants will be at the same intial position but with different direction.

Example 5:

Input: n = 6, left = [6], right = [0]
Output: 6



Constraints:

    1 <= n <= 10^4
    0 <= left.length <= n + 1
    0 <= left[i] <= n
    0 <= right.length <= n + 1
    0 <= right[i] <= n
    1 <= left.length + right.length <= n + 1
    All values of left and right are unique, and each value can appear only in one of the two arrays.

"""

#Modeling the entire problem:
class Solution:
    def getLastMoment(self, n: int, left, right) -> int:
        class ant:
            def __init__(self, pos, dir):
                self.pos = pos
                self.dir = dir
            def change_pos(self):
                self.pos += self.dir
        ant_list = []
        for pos in left:
            ant_list.append(ant(pos,-1))
        for pos in right:
            ant_list.append(ant(pos, 1))
        timer = 0
        while ant_list:
            remove = []
            pos_dict = {}
            for a in ant_list:
                a.change_pos()
                if a.pos > n or a.pos < 0:
                    remove.append(a)
                else:
                    if a.pos not in pos_dict:
                        pos_dict[a.pos] = [a]
                    else:
                        pos_dict[a.pos].append(a)
            ant_list = [e for e in ant_list if e not in [1,2,3]]
            timer += 1
            if not ant_list:
                return timer-1
            else:
                for key, value in pos_dict.items():
                    if len(value) > 1:
                        value[0].dir *= -1
                        value[1].dir *= -1

#Real solution: #99.65%
#Note that the collisions actually do not change anything. Even though the ants have turned around the next second everything
#will look as if the collision never happened. Therefore, you can just time how long it takes for the furthest ant from the ledge
#to get to the ledge
"""
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left:    return n-min(right)
        if not right:   return max(left)
        return max(n-min(right), max(left))
"""

if __name__ == '__main__':
    def test(input1, input2,input3):
        Test = Solution()
        print(Test.getLastMoment(input1, input2,input3))

    n,left,right = 4,[4,3],[0,1]
    test(n,left,right) #4
    n, left, right = 7, [], [0,1,2,3,4,5,6,7]
    test(n, left, right)#7
    n, left, right = 7, [0,1,2,3,4,5,6,7],  []
    test(n, left, right)#7
    n, left, right = 9, [5], [4]
    test(n, left, right)#5
    n, left, right = 6, [6], [0]
    test(n, left, right)#6