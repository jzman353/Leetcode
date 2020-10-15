"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It's guaranteed the answer fits on a 32-bit signed integer.

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""
'''
def numDistinct(s: str, t: str) -> int:
    new_dict = {}
    current_index_of_t = 0
    # for i in range(len(s)-1,-1,-1):
    for count, letter in enumerate(s):
        if letter not in new_dict.keys():
            new_dict[letter] = [count]
        else:
            new_dict[letter].append(count)
    print(new_dict)
    # for each letter in t,
    # take the first item in the list of the dictionary
    # key = letter
    # Find out if word is possible
    for count, letter1 in enumerate(t):
        for index1 in new_dict[letter1]:
            for count2, remaining_letter in enumerate(t[count+1:]):
                print(remaining_letter)
                stack = []
                for index2 in new_dict[remaining_letter]:
                    if index2 > index1:
                        stack.append([count+count2+1,index2])
                    else:
                        pass
                print(stack)
                #if stack:
'''
import collections
#class Solution(object):
def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    tPos = collections.defaultdict(list)
    dic = collections.defaultdict(int)
    dic[-1] = 1
    for i, e in enumerate(t):
        tPos[e].append(i)
    for c in s:
        locs = tPos[c]
        for idx in reversed(locs):
            dic[idx] += dic[idx-1]
    return dic[len(t)-1]
'''
def numDistinct(self, s: str, t: str) -> int:
        if not t: return 1
        if not s: return 0
        if s[0] != t[0]: return self.numDistinct(s[1:], t)
        return self.numDistinct(s[1:], t[1:]) + self.numDistinct(s[1:], t)
    
def numDistinct(self, s: str, t: str) -> int:
    def numDis(s, t, i, j, m):
        if j == len(t): return 1
        if i == len(s): return 0
        if m[i][j] is None: 
            if s[i] != t[j]: m[i][j] = numDis(s, t, i+1, j, m)
            else: m[i][j] = numDis(s, t, i+1, j+1, m) + numDis(s, t, i+1, j, m)
        return m[i][j]
    
    ls, lt = len(s), len(t)
    m = [[None] * lt for _ in range(ls)]
    return numDis(s, t, 0, 0, m)

def numDistinct(self, s: str, t: str) -> int:
    ls, lt = len(s), len(t)
    dp = [[0] * (lt+1) for _ in range(ls+1)]
    dp[0][0] = 1
    for i in range(1, ls+1): dp[i][0] = 1
    # for j in range(1, lt+1): dp[0][j] = 0
    for i in range(1, ls+1):
        for j in range(1, lt+1):
            dp[i][j] = dp[i-1][j]
            if s[i-1] == t[j-1]: dp[i][j] += dp[i-1][j-1]
    return dp[-1][-1]
    
int row = s.length()+1;
int col = t.length()+1;
vector<vector<long> > dp(row,vector<long>(col+1 , 0) );

//base case
for(int i=0; i<col; i++){
	dp[row-1][i] = 0;
}

for(int i=0; i<row; i++){
	dp[i][col-1] = 1;
}


for(int i = row-2; i>=0; i--){
	
	for(int j = col-2; j>=0; j--){
        long count =0;
		if(s[i] == t[j]){
			count+=dp[i+1][j+1];
		}
		count += dp[i+1][j];

		dp[i][j] = count;
	}
}

return dp[0][0] ;

class Solution:
	def numDistinct(self, s: str, t: str) -> int:
		# count the ending at s
		if len(s) < len(t): return 0
		dp = [0]  * (len(t) + 1)
		dp[0] = 1
		for c in s:
			bk = dp[:] # t may have duplicated c 
			for idx in range(len(t)):
				if not bk[idx]: 
					break
				elif c == t[idx]:
					dp[idx+1] = bk[idx+1] + bk[idx]
		return dp[-1]
		
class Solution:
    def numDistinct(self, s: str, t: str) -> int:        
#         dp[i][j] = number of subsequences till s[:i+1] that matches t[:j+1]
#             #    r   a   b   b   i   t
#         #   1.   0.  0   0.  0.  0.  0
#         r   1    1   0   0   0   0   0
#         a   1    1   1   0.  0.  0.  0
#         b   1    1.  1.  1.  0.  0.  0
#         b   1    1   1.  2.  1.  0.  0
#         b   1    1.  1   3.  3   0.  0
#         i   1    1.  1.  3.  3.  3.  0
#         t   1    1.  1.  3.  3.  3.  3

        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] != t[j-1]:
                    # When there is no match
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        return dp[len(s)][len(t)]
        
Bottom-Up
dp[index_t][index_s] = ( t[index_t] == s [index_s] ) * count
count = sum(dp[index_t - 1][ : index_s])( for index_t = 0, count = 1)
for example : t = "dogg", s = "dog"
dp[0] = 1 0 0 0
dp[1] = 0 1 1 0
dp[2] = 0 0 0 2
dp[j] only depends on dp[j-1] -> make 2D array -> 1D array

def numDistinct(self, s: str, t: str) -> int:
    len_s = len(s)
    len_t = len(t)
    
    dp = [ 1 * (t[0] == s[i]) for i in range(len_s)]
    for index_t in range(1,len_t):
        count = 0
        for index_s in range(len_s):
            if t[index_t] == s[index_s]:
                dp[index_s],count = count,count+dp[index_s]
            else:
                dp[index_s],count = 0 , count + dp[index_s]
    return sum(dp)
    
Top-Down (Faster)
straight forward:
if t[index_t] = s[index_s] -> choose or not choose
else -> not choose
backtrack to count faster

def numDistinct():
    import functools
    len_s = len(s)
    len_t = len(t)
    @functools.lru_cache(maxsize = None)
    def DFS(index_t,index_s):
        if index_t == len(t):
            return 1
        if len_t - index_t > len_s - index_s or t[index_t] not in s[index_s:]:
            return 0
        if t[index_t] == s[index_s]:
            return DFS(index_t+1,index_s+1) + DFS(index_t,index_s+1)
        else:
            return DFS(index_t,index_s+1)    
    return DFS(0,0)
    
This solution uses a map where keys are the characters, and we store the list of indices in t for each character. Hence we don't need to loop over the entire t, making our best case time complexity O(max(N,M)). The worst case is when both of the inputs are the repetitions of the same character . Then the loop will run O(NM) times.

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        c_indices = collections.defaultdict(list)
        max_counts = [1] + [0] * len(t) 
        for i, c in enumerate(t):
            c_indices[c].append(i + 1)
        for c in s:
            for i in reversed(c_indices[c]):
                max_counts[i] += max_counts[i - 1]
        return max_counts[-1]
        
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        tset = set(t)
        new_s = ''.join([x for x in s if x in tset])
        new_t = '#' + t
        dp_t = [0 for _ in range(len(new_t))]
        dp_t[0] = 1
        lookup = {q: [] for q in tset}
        for i in range(len(new_t)-1, 0, -1):
            lookup[new_t[i]].append(i)
            
        for s in new_s:
            for i in lookup[s]:
                dp_t[i] += dp_t[i-1]
        
        return dp_t[-1]
        
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if s == t:
            return 1
        
        return self.dfs(s, t, 0, 0, {})
    
    
    def dfs(self, s, t, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        n, m = len(s), len(t)
        
        if j == m:
            return 1
        
        if i == n:
            return 0
        
        res = self.dfs(s, t, i + 1, j, memo)
        
        if s[i] == t[j]:
            res += self.dfs(s, t, i + 1, j + 1, memo)
        
        memo[(i, j)] = res
        return res
        
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        positions = collections.defaultdict(list)
        
        for i, c in enumerate(s):
            positions[c].append(i)
        
        lastPos = []
        lastSum = []
        result = 0
        for i in range(len(t) - 1, -1, -1):
            c = t[i]
            if c not in positions:
                return 0
            pos = positions[c]
            
            if i != len(t) - 1:
                newSum = [0] * len(pos)
                reachedEnd = False #if our cur index reaches the end of last position list, we set the rest to 0
                for j in range(len(pos)):
                    if reachedEnd:
                        newSum[j] = 0
                        continue
                    index = bisect.bisect_right(lastPos, pos[j])
                    newSum[j] = lastSum[index] if index < len(lastSum) else 0
                    if index == len(lastSum):
                        reachedEnd = True
                lastSum = newSum
            else:
                lastSum = [1] * len(pos)
            
            lastPos = pos
            
            curSum = 0
            for k in range(len(lastSum) - 1, -1, -1):
                lastSum[k] = curSum + lastSum[k]
                curSum = lastSum[k]
            
            if i == 0:
                result = curSum
            
            
        return result
'''

#S = "rabbbit"
#T = "rabbit"

#S = "babgbag"
#T = "bag"

S = "babgbagaaaaaaaa"
T = "bag"
print(numDistinct(S, T))