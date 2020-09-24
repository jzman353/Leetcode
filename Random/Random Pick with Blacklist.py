"""
Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

    1 <= N <= 1000000000
    0 <= B.length < min(100000, N)
    [0, N) does NOT include N. See interval notation.

Example 1:

Input:
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]

Example 2:

Input:
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]

Example 3:

Input:
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]

Example 4:

Input:
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""

#The issue with this code is that it has to repeatedly guess until it doesn't hit a blacklisted item
#To make the code more efficient, we need to create a list of whitelisted intervals
#To do this, sort the blacklist and make a list that finds all the spaces in blacklist
#Then, randomly choose a whitelisted range (it should be weighted by the number of numbers in the interval)
#Then, randomly choose a number within that whitelisted range
"""
class Solution:

    def __init__(self, N: int, blacklist):
        self.N = N
        self.blacklist = blacklist
        self.smallblacklist = False
        if len(blacklist) < N/2:
            self.smallblacklist = True
            defined = [1 for i in blacklist]
            self.dict1 = dict(zip(blacklist,defined))

    def pick(self) -> int:
        import random
        if self.smallblacklist:
            while(1):
                x = random.randint(0,self.N-1)
                if x not in self.dict1.keys():
                    return x
        else:
            sorted_bl = list(sorted(self.blacklist))
            possibilities = []
            if sorted_bl[0] != 0:
                j = 0
                while j < sorted_bl[0]:
                    possibilities.append(j)
                    j += 1
            if sorted_bl[-1] != self.N-1:
                j = self.N-1
                while j > sorted_bl[-1]:
                    possibilities.append(j)
                    j -= 1
            for i in range(len(sorted_bl)-1):
                if sorted_bl[i] + 1 != sorted_bl[i+1]:
                    j = sorted_bl[i] + 1
                    while j < sorted_bl[i+1]:
                        possibilities.append(j)
                        j += 1
            return random.choice(possibilities)
"""

class Solution:

    def __init__(self, N: int, blacklist):
        self.N = N
        self.blacklist = blacklist

    def pick(self) -> int:
        import random
        if len(self.blacklist) < N / 5:
            while (1):
                x = random.randint(0, self.N - 1)
                if x not in self.blacklist:
                    return x
        if not self.blacklist:
            return random.randint(0,self.N-1)
        sorted_bl = list(sorted(self.blacklist))
        possibilities = []
        weights = []
        if sorted_bl[0] != 0:
            possibilities.append([0,sorted_bl[0]-1])
            weights.append(sorted_bl[0]-1+1)
        if sorted_bl[-1] != self.N-1:
            possibilities.append([sorted_bl[-1]+1,self.N-1])
            weights.append(self.N-(sorted_bl[-1]+1))
        for i in range(len(sorted_bl)-1):
            if sorted_bl[i] + 1 != sorted_bl[i+1]:
                possibilities.append([sorted_bl[i] + 1, sorted_bl[i+1]-1])
                weights.append(sorted_bl[i+1]-1-(sorted_bl[i] + 1)+1)
        range1 = random.choices(possibilities,weights)[0]
        return random.randint(range1[0],range1[1])



# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution(input1, input2)
        print(Test.pick())
        print(Test.pick())
        print(Test.pick())
        print(Test.pick())
        print(Test.pick())

    #No Blacklist
    N = 1
    B = []
    test(N, B)
    N = 2
    B = []
    test(N, B)
    #1 item in blacklist
    N = 3
    B = [1]
    test(N, B)
    N = 4
    B = [2]
    test(N, B)
    # Complex test
    N = 10
    B = [2,4,5,6,8]
    test(N, B)
    N = 10
    B = [0,1,2, 4, 5, 6, 9]
    test(N, B)
    N = 10
    B = [0, 1, 2, 4]
    test(N, B)

import timeit
print(timeit.timeit("test(10000000,range(0,10000000,2))", setup="from __main__ import test", number=2))
# This is an example of a large n with a blacklist that is not super populated
#1st attempt took 11 seconds on average
#2nd attemp took 19.5 seconds on average

"""
We have to generate numbers in [0,N) excluding integers in set B. That means that are M = N-len(B) valid numbers. So, generate random index in [0,M); if that index is not excluded, return it. Otherwise, map it to a non-excluded value in [M,N).

class Solution:

    def __init__(self, N: int, B: List[int]):
        B = frozenset(B)
        self.M = M = N-len(B)
        self.D = D = dict()
        for b in B:
            if b < M:
                while M in B:
                    M += 1
                D[b] = M
                M += 1

    def pick(self) -> int:
        i = randrange(self.M)
        return self.D.get(i,i)

"""

"""
This is the first time I am getting a 100% time performance on LC so it may be a bit of luck.

Generally, there are 3 things to consider: size of the population to pick up from (N), size of the blacklist (B) and the number of queries (which is unknown). By testing the first version of my solution I got TLE and this is when I realised that the number of queries can be really large (I saw a test case with 20K queries).

If there are a lot of queries it makes sense to do as much pre-processing as possible. So after getting the TLE with 20K queries I went for a white list approach. Which got me another TLE of a case with a large N and small B.

So I went for a balance between the black and white list: if B is greater than N // 3 than it makes sense to do a white list.

This is, essentially, a bit of LC hacking (the solution was informed by the 2 TLEs) so take it for what it is.

Complexity for the preprocessing is N + B for the white list approach and just B for the black list one.

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.b, self.ra, self.l = frozenset(blacklist), range(N), len(blacklist) > N // 3
        if self.l: self.ra = [x for x in self.ra if x not in self.b] #white list
        self.r = random.choices(self.ra, k = 1000)

    def pick(self) -> int:
        while True:
            if not self.r: self.r = random.choices(self.ra, k = 1000)
            c = self.r.pop()
            if self.l: return c
            elif c not in self.b: return c  #white list
"""