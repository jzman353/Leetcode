'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.

The greatest common divisor must be a prefix of each string, so we can try all prefixes.

Runtime: 80 ms Beats 5%
Memory Usage: 13.8 MB
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_List=[]
        separator=""
        if(len(str1)<len(str2)):
            for i in range(len(str1)):
                if str1[i]==str2[i]:
                    gcd_List.append(str1[i])
                else:
                    break
            #print(gcd_List)
            if(gcd_List==[]):
                return ""
            while(len(str1)%len(gcd_List)!=0 or len(str2)%len(gcd_List)!=0):
                gcd_List=gcd_List[:int(len(gcd_List)-1)]
            #print(gcd_List)
            print(gcd_List*int((len(str2)/len(gcd_List))))
            if separator.join(gcd_List*int((len(str2)/len(gcd_List))))==str2:
                return separator.join(gcd_List)
            else:
                return ""
        else:
            for i in range(len(str2)):
                if str1[i]==str2[i]:
                    gcd_List.append(str1[i])
                else:
                    break
            #print(gcd_List)
            if(gcd_List==[]):
                return ""
            while(len(str1)%len(gcd_List)!=0 or len(str2)%len(gcd_List)!=0):
                gcd_List=gcd_List[:int(len(gcd_List)-1)]
            #print(gcd_List)
            #print(gcd_List*int((len(str1)/len(gcd_List))))
            if separator.join(gcd_List*int(len(str1)/len(gcd_List)))==str1:
                return separator.join(gcd_List)
            else:
                return ""
            
            
'''
Runtime: 28 ms

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        
        if len2 > len1:
            return self.gcdOfStrings(str2,str1)
        
        if str1 == str2:
            return str2
        elif str1[:len2] == str2:
            return self.gcdOfStrings(str1[len2:],str2)
        else:
            return ''

Runtime: 28 ms
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        
        if len2 > len1:
            return self.gcdOfStrings(str2,str1)
        
        if str1 == str2:
            return str2
        elif str1[:len2] == str2:
            return self.gcdOfStrings(str1[len2:],str2)
        else:
            return ''

Runtime: 12 ms

class Solution:
    def gcd(self, a,b):
        if b==0:
            return a
        else:
            return self.gcd(b,a%b)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        t1= len(str1)
        t2 = len(str2)
        t = self.gcd(t1,t2)
        
        if len(str1) > len(str2):
            if str1 == str2 + str1[:t1-t2]:
                return str1[:t]
            else:
                return ""
        elif len(str1) < len(str2):
            if str2 == str1 + str2[:t2-t1]:
                return str2[:t]
            else:
                return ""
        else:
            if str1 == str2:
                return str1[:t]
            else:
                return ""


'''