"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.



Constraints:

    1 <= asteroids <= 104
    -1000 <= asteroids[i] <= 1000
    asteroids[i] != 0
"""
#10%
import collections
class Solution:
    def asteroidCollision(self, asteroids):
        ansleft = []
        ansright = collections.deque()
        while asteroids:
            while asteroids and asteroids[0] < 0:
                ansleft.append(asteroids[0])
                del asteroids[0]
            while asteroids and asteroids[-1] > 0:
                ansright.appendleft(asteroids[-1])
                del asteroids[-1]
            if not asteroids:
                break
            i = 0
            while asteroids and i<len(asteroids)-1:
                if asteroids[i+1] < 0 and asteroids[i] > 0:
                    if abs(asteroids[i+1])>abs(asteroids[i]):
                        del asteroids[i]
                    elif abs(asteroids[i+1])<abs(asteroids[i]):
                        del asteroids[i+1]
                    elif abs(asteroids[i+1])==abs(asteroids[i]):
                        del asteroids[i]
                        del asteroids[i]
                elif asteroids[i] < 0:
                    break
                else:
                    i += 1
        ans = ansleft+list(ansright)
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.asteroidCollision(input1)
        print(ans)
        return ans

    assert test([5,10,-5]) == [5,10]
    assert test([8,-8]) == []
    assert test([10,2,-5]) == [10]
    assert test([-2,-1,1,2]) == [-2,-1,1,2]
    assert test([1, -2, 2, -2]) == [-2]
    assert test([1, -2, 2, 1]) == [-2,2,1]
    assert test([10, -2, 2, 1]) == [10, 2, 1]
    assert test([1,-1,-1,-2]) == [-1,-2]

"""
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stackleft=deque()
        stackright=deque()
        
        for asteroid in asteroids:
            if asteroid>0: 
                stackright.append(asteroid)
            else:
                while stackright and stackright[-1]<=abs(asteroid):
                    temp=stackright[-1]
                    stackright.pop()
                    if temp==abs(asteroid):break
            
        for asteroid in reversed(asteroids):
            if asteroid <0:
                stackleft.appendleft(asteroid)
            else:
                while stackleft and abs(stackleft[0])<=asteroid:
                    temp=stackleft[0]
                    stackleft.popleft()
                    if abs(temp)==asteroid:break
        return stackleft+stackright
"""