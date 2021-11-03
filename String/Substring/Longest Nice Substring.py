"""
1763. Longest Nice Substring
Easy

A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
Example 4:

Input: s = "dDzeE"
Output: "dD"
Explanation: Both "dD" and "eE" are the longest nice substrings.
As there are multiple longest nice substrings, return "dD" since it occurs earlier.

Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.
"""
#53%
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ss = set(s)
        ans = ""
        upper_and_lower = []
        #print(ord("A"),ord("a"))
        for i in ss:
            if chr(ord(i)+32) in ss or chr(ord(i)-32) in ss:
                upper_and_lower.append(i)
        #print(upper_and_lower)
        for i in range(len(s)-1):
            curr = s[i]
            for j in range(i+1,len(s)):
                if s[j] not in upper_and_lower:
                    break
                curr += s[j]
                temp = set(curr)
                if len(curr) > len(ans):
                    for k in temp:
                        if chr(ord(k)+32) not in temp and chr(ord(k)-32) not in temp:
                            break
                    else:
                        ans = curr
            if len(s)-i < len(ans):
                break
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.longestNiceSubstring(input1)
        print(ans)
        return ans

    assert test("YazaAay") == "aAa"
    assert test("Bb") == "Bb"
    assert test("c") == ""
    assert test("dDzeE") == "dD"

"""
This solution is extremely elegant. The first thing that stands out to me is the use of recusion and the c.caseswap() 
which I haven't seen before. The recursion basically asks it to find the problematic letters and then run the function 
again on two possible strings without them (before and after but leaving out all other problematic letters found 
previously). max(s0, s1, key=len) sorts by length. Very well thought out solution.
sample 16 ms submission
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: return ""
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss:
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s

This will take me some time to process
sample 20 ms submission
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        X = defaultdict(list)
        for i, x in enumerate(s):
            bisect.insort(X[x], i)
        
        self.ns = ''
        def longestNiceSubstring_(i=0, j=len(s)):
            if j <= i + 1:
                return
            
            k = i
            for t in range(i, j):
                x = X[s[t].upper()] if s[t].islower() else X[s[t].lower()]
                l = bisect.bisect_left(x, k)
                if l == len(x) or x[l] >= j:
                    if t - k > len(self.ns):
                        longestNiceSubstring_(k, t)
                    
                    k = t + 1
            
            if j - k > len(self.ns):
                if k > i:
                    longestNiceSubstring_(k, j)
                    
                else:
                    self.ns = s[i:j]
        
        longestNiceSubstring_()
        return self.ns

This is typically a divide and conquer problem, and can be solve with the time complexity O(N)

But in the contest, many people just use brute force and solve it using O(N^2). This method can save them a lot of time, and get better standing. And in the practise, many people just get accepted using brute force and move on.

However, this is not good for them because in the real interview, the interviewer will not satisfy if you only present him or her brute force method. It can only waste him or her good chance to practise divide and conquer method.

So, please add some large test cases 1<=n<=10^5, and mark this problem an medium problem.

Here is my O(N) solution, for each s, we try to find the location of any character for appear only in either uppercase or lowercase, and split the string by these characters. Then for each splited substring, do the same thing, until it can not be splited. return the longest substring with first appearance.

(As some people point out, this is actually NlgN because of the sorting part)

        def getsplit(subs):
            if len(subs)<2: return ""
            lcase = [[] for i in range(26)]
            ucase = [[] for i in range(26)]
			
			#lcase is the lowercase and ucase is the upper case
			
            for i in range(len(subs)):
                if ord(subs[i])-97>=0:  lcase[ord(subs[i])-97].append(i)
                else: ucase[ord(subs[i])-65].append(i)        
            part = [-1,len(subs)]
			
			# part is the index which  letter only appear in either upper case or lower case, and we append -1 and the length of substring for convenience 
                
            for k in range(26):
                if len(ucase[k])*len(lcase[k])==0 and len(ucase[k]) + len(lcase[k])>0:
                    for ele in ucase[k]+lcase[k]:
                        part.append(ele)              
						
            if len(part)==2: return subs         
            part = sorted(part)
            output = ""      
            for i in range(len(part)-1):
                newsub = subs[ (part[i]+1):part[i+1]]
                temp = getsplit(newsub)
                if len(temp)>len(output):
                    output = temp  
            return output
        
        return getsplit(s)

One line solution
class Solution: longestNiceSubstring = f = lambda _,s: next((max(_.f(s[:i]), _.f(s[i + 1:]), key=len) for i, c in enumerate(s) if c.swapcase() not in s), s)
"""