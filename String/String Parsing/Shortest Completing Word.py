"""
748. Shortest Completing Word
Easy
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

Example 1:

Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.
Example 2:

Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
Example 3:

Input: licensePlate = "Ah71752", words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
Output: "husband"
Example 4:

Input: licensePlate = "OgEu755", words = ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]
Output: "enough"
Example 5:

Input: licensePlate = "iMSlpe4", words = ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]
Output: "simple"

Constraints:

1 <= licensePlate.length <= 7
licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
1 <= words.length <= 1000
1 <= words[i].length <= 15
words[i] consists of lower case English letters.
"""

#31%
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        c_L = Counter()
        for i in licensePlate:
            if i in string.ascii_letters:
                c_L[i.lower()] += 1
        # print(c_L)

        possibilities = []
        for i in words:
            c_W = Counter()
            for letter in i:
                c_W[letter] += 1
            good = True
            for letter in c_L:
                if c_L[letter] > c_W[letter]:
                    good = False
            if good:
                possibilities.append(i)
        # print(possibilities)
        s = sorted(possibilities, key=lambda e: (len(e)))
        # print(s)
        return s[0]

"""
7.2%
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        c_L = Counter()
        for i in licensePlate:
            if i in string.ascii_letters:
                c_L[i.lower()] += 1
        
        words.sort(key=len)
        for i in words:
            c_W = Counter()
            for letter in i:
                c_W[letter] += 1
            good = True
            for letter in c_L:
                if c_L[letter] > c_W[letter]:
                    good = False
            if good:
                return i
"""

"""
#This solution is very similar to mine with some cool optimizations.
#Their c_L was made in the same time as mine but using list comprehension so their code is more compact
#They narrow down the word list by comparing sets. This makes the sort by length that they perform way more efficient than otherwise.
#The key optimization of their solution was sorting by length before going through the wordlist so that way they can return the first good possibility

sample 52 ms submission
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        c = Counter([alpha for alpha in licensePlate.lower() if alpha.isalpha()])
        
        # words.sort(key=len)
        s = set(c)
        
        w = [i for i in words if s.issubset(set(i))]
        w.sort(key=len)
        # while
        for i in range(len(w)):
            
            counter = Counter(w[i])
            ans = True
            for key in c:
                if c[key] > counter[key]:
                    ans = False
            
            if ans:
                return w[i]
                
"""