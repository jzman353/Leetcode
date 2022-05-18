"""
969. Pancake Sorting
Medium

Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

Example 1:

Input: arr = [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [1, 4, 2, 3]
After 2nd flip (k = 2): arr = [4, 1, 2, 3]
After 3rd flip (k = 4): arr = [3, 2, 1, 4]
After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
Example 2:

Input: arr = [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= arr.length
All integers in arr are unique (i.e. arr is a permutation of the integers from 1 to arr.length).
"""
#15%
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        inx = len(arr)
        while inx>0:
            #print(inx)
            maxx = -math.inf
            maxx_inx = 0
            for i in range(inx):
                if arr[i]>maxx:
                    maxx = arr[i]
                    maxx_inx = i
            if maxx_inx == inx-1:
                pass
            elif maxx_inx == 0:
                #print(4,arr,arr[0:inx][::-1]+arr[inx:])
                arr = arr[0:inx][::-1]+arr[inx:]
                answer.append(inx)
            else:
                #print(1,arr)
                arr = arr[0:maxx_inx+1][::-1]+arr[maxx_inx+1:]
                #print(2,arr,inx)
                arr = arr[0:inx][::-1]+arr[inx:]
                #print(3,arr)
                answer.extend([maxx_inx+1,inx])
            inx -= 1
        return answer

"""
sample 28 ms submission
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            res.extend([i+1, x])
            arr = arr[:i:-1] + arr[:i]
            
        return res

Solution
Approach 1: Sort like Bubble-Sort
Intuition

One might argue that this is an awkward question to do things. Indeed, it is not the most practical operation that one can have with the pancake flipping, in order to sort a list.

However awkward the problem might be, it is the game that we play with. And in order to win the game, we have to play by the rules. Actually, from this perspective, this problem does share some similarity with the Rubik's cube, i.e. one cannot move one tile without moving other tiles along with. Let us get on with it, by playing a few rounds ourselves to get the hang of the problem.

Given the input of [3, 2, 4, 1], the desired sorted output would be [1, 2, 3, 4].

As a reminder, the only operation that we could perform in order to move the elements in the list, is the so-called pancake flip, which is to reverse a prefix of the list.

Starting from the largest value in the list, i.e. 4 in the example, its desired position would be the tail of the list. While in the input, it is located at the third of the list, if we look at the list from left to right.

In order to move the value of 4 to its desired position, we could perform the following two steps:

Firstly, we do the pancake flip on the prefix of [3, 2, 4]. With this operation, we then move the value 4 to the head of the updated list as [4, 2, 3, 1].
flip to head

Now that, the value 4 is located at the head of the list, we could now perform another pancake flip on the entire list, which would get us the list of [1, 3, 2, 4].
flip to tail

Voila. With the obtained list of [1, 3, 2, 4], we are now one step closer to our final goal, with the value 4 now at its proper place. For the following steps, we only need to focus on the sublist of [1, 3, 2].

If one looks over the above steps again, it might ring a bell to a well-known algorithm called bubble sort.

Indeed, we share the same strategy as the bubble sort, by sinking the numbers to the bottom one by one.

Here we can make a statement that for any given number, in order to move it to any desired position, it takes at most two pancake flips to do so.

The idea is simple. First we move the number to the head of the list, then we can switch it with any other element by performing another pancake flip.

Algorithm

One can inspire from the bubble sort to implement the algorithm.

First of all, we implement a function called flip(list, k), which performs the pancake flip on the prefix of list[0:k] (in Python).

The main algorithm runs a loop over the values of the list, starting from the largest one.

At each round, we identify the value to sort (named as value_to_sort), which is the number we would put in place at this round.

We then locate the index of the value_to_sort.

If the value_to_sort is not at its place already, we can then perform at most two pancake flips as we explained in the intuition.

At the end of the round, the value_to_sort would be put in place.

sort like bubble-sort
sink the largest number to the bottom at each round
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1

        ans = []
        value_to_sort = len(A)
        while value_to_sort > 0:
            # locate the position for the value to sort in this round
            index = A.index(value_to_sort)

            # sink the value_to_sort to the bottom,
            #   with at most two steps of pancake flipping.
            if index != value_to_sort - 1:
                # flip the value to the head if necessary
                if index != 0:
                    ans.append(index+1)
                    flip(A, index+1)
                # now that the value is at the head, flip it to the bottom
                ans.append(value_to_sort)
                flip(A, value_to_sort)

            # move on to the next round
            value_to_sort -= 1

        return ans

Complexity Analysis

Let NN be the length of the input list.

Time Complexity: \mathcal{O}(N^2)O(N 
2
 )

In the algorithm, we run a loop with NN iterations.

Within each iteration, we are dealing with the corresponding prefix of the list. Here we denote the length of the prefix as kk, e.g. in the first iteration, the length of the prefix is NN. While in the second iteration, the length of the prefix is N-1N−1.

Within each iteration, we have operations whose time complexity is linear to the length of the prefix, such as iterating through the prefix to find the index, or flipping the entire prefix etc. Hence, for each iteration, its time complexity would be \mathcal{O}(k)O(k)

To sum up all iterations, we have the overall time complexity of the algorithm as \sum_{k=1}^{N} \mathcal{O}(k) = \mathcal{O}(N^2)∑ 
k=1
N
​
 O(k)=O(N 
2
 ).

Space Complexity: \mathcal{O}(N)O(N)

Within the algorithm, we use a list to maintain the final results, which is proportional to the number of pancake flips.

For each round of iteration, at most we would add two pancake flips. Therefore, the maximal number of pancake flips needed would be 2\cdot N2⋅N.

As a result, the space complexity of the algorithm is \mathcal{O}(N)O(N). If one does not take into account the space required to hold the result of the function, then one could consider the above algorithm as a constant space solution.
"""