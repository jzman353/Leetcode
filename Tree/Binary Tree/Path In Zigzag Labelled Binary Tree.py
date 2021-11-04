"""
1104. Path In Zigzag Labelled Binary Tree
Medium

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]

Constraints:

1 <= label <= 10^6
"""
#68%
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        #14//2 = 7  7//2 = 3 3//2 = 1 so the normally indexed tree would be 1,3,7,14
        #note that we only need to change the odd rows after one
        #26//2 = 13 13//2 = 6 6//2 = 3 3//2 = 1 1,3,6,13,26
        #note that we only have to change the even rows
        #Final comment: All the numbers that are 2 rows away from the final number are correct and the 1 is correct
        answer = []
        while label > 1:
            answer.append(label)
            label //= 2
        answer.append(1)
        answer.reverse()
        for i in range(len(answer)-2,0,-2):
            #print(i)
            #print((3*2**i-1)/2)
            #print(answer[i]-2*(answer[i]-(3*2**i-1)/2))
            #print(-answer[i] + 3*2**i-1)
            answer[i] = -answer[i] + 3*2**i-1
        return answer

"""
sample 16 ms submission
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = [label]
        i = 1
        while 2 ** i <= label:
            i += 1
        i -= 1
        while i:
            temp = (label - 2 ** i) // 2 + 1
            label = 2 ** i - temp
            i -= 1
            res.append(label)
        return reversed(res)  
"""