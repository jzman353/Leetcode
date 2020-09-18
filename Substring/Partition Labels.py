#0%
#Runtime: 212 ms
#Memory Usage: 13.8 MB
"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.



Note:

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.
"""

def partitionLabels(S: str):
    head_index = 0
    tail_index = S.rfind(S[head_index])+1
    substring = S[head_index:tail_index]
    sum = 0
    output = []
    while sum < len(S):
        done = False
        while not done:
            done = True
            for i in substring:
                if i in set(S[tail_index:]):
                    tail_index = S.rfind(i) + 1
                    substring = S[head_index:tail_index]
                    done = False
        output.append(substring)
        sum += len(substring)
        if sum == len(S):
            break
        head_index = tail_index
        tail_index = S.rfind(S[head_index])
        substring = S[head_index:tail_index+1]
    for count in range(len(output)):
        output[count] = len(output[count])
    return output







"""    for i in S[1:]:
        index_pos = get_index_positions(S,i)
        newlist = [S[0:min(index_pos)]"""

#print(partitionLabels("ababcbacadefegdehijhklij")) [9,7,8] #1/116
#print(partitionLabels("eaaaabaaec")) [9,1] #3/116
print(partitionLabels("qiejxqfnqceocmy")) #[13,1,1] #113/116

'''
20 ms
def partitionLabels(self, S: str) -> List[int]:
    last = {ch: idx for idx, ch in enumerate(S)}
    res = []
    start = 0
    end = 0
    for i in range(len(S)):
        end = max(end, last[S[i]])
        if i == end:
            res.append(end - start + 1)
            start = end + 1
            end = start

    return res
    
36 ms
def partitionLabels(self, S: str) -> List[int]:
    d = dict()
    for i, c in enumerate(S):
        if c not in d:
            d[c] = [i, i]
        else:
            d[c][1] = i
    partitions = [d[S[0]]]
    for c in d:
        if d[c][0] > partitions[-1][0]:
            if d[c][0] < partitions[-1][1] < d[c][1]:
                partitions[-1][1] = d[c][1]
            elif partitions[-1][1] < d[c][0]:
                partitions.append(d[c])
    print(partitions)
    for i in range(len(partitions)):
        partitions[i] = partitions[i][1] - partitions[i][0] + 1
    return partitions
'''