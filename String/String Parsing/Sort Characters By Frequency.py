'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Runtime: 84 ms (Beats 14%)
Memory Usage: 15.3 MB
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter()
        for letter in s:
            cnt[letter] += 1
        data =  cnt.most_common()
        output = ''
        for i in range(len(data)):
            if data[i][1] == 1:
                output += data[i][0]
            else:
                for j in range(data[i][1]):
                    output += data[i][0]
        return output

'''
Better:
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter()
        for letter in s:
            cnt[letter] += 1
        data =  cnt.most_common()
        output = ''
        for i in range(len(data)):
            output += data[i][0] * data[i][1]
        return output
'''

'''
Runtime: 36 ms
class Solution(object):
    def frequencySort(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([char * times for char, times in collections.Counter(str).most_common()])

Runtime: 20 ms
#uses heapq, which is a min heap setup
#uses negative freq because it wants the highest frequency to be the first 
#available in the queue but then uses negative again to make it a 
#positive number again


import collections 
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        counterMap = collections.Counter(s)
        res = ''
        hq = []
        for char, freq in counterMap.items():
            heapq.heappush(hq, (-freq, char))

        while hq:
            freq, char = heapq.heappop(hq)
            res += -freq*char
            
        return res
'''

'''
import collections
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        letterCountDict = {}
        
        for letter in s:
            if letter in letterCountDict:
                letterCountDict[letter]+=1
            else:
                letterCountDict[letter]=1
            
        heap = []
        result = []
        
        for key,value in letterCountDict.items():
            heap.append((-value,key))
        
        heapq.heapify(heap)
            
        
        while(len(heap) != 0):
            value, letter = heapq.heappop(heap)
            value*=-1
            for i in range(value):
                result.append(letter)
        
        return ''.join(result)
'''
