"""
40. Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

#5%
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates)<target:
            return []
        self.answer = []
        candidates.sort()
        def helper(candidates,target,curr=[]):
            temp = []
            for j in self.answer:
                temp.append(j[:len(curr)+1])
            print(temp)
            for i in range(len(candidates)):
                calc = target-candidates[i]
                if calc>0:
                    #print(candidates,candidates[i],bisect.bisect_right(candidates, candidates[i]))
                    if curr+[candidates[i]] not in temp:
                        helper(candidates[i+1:],calc,curr+[candidates[i]])
                if calc==0 and curr+[candidates[i]] not in self.answer:
                    self.answer.append(curr+[candidates[i]])
                    break
        helper(candidates,target)
        return self.answer

"""
Solution
Overview
As one might figure from the title of this problem, this is an extention or variation of an earlier problem called 39. Combination Sum. Therefore, it would be helpful if one starts from the previous problem before tackling this one.

There are a series of problems on the theme of combination sum, as one will find out later. These problems differ on the conditions such as whether there are duplicate numbers in the input list or whether a number can be used multiple times in a combination. Despite of all the differences, the key algorithm to solve the combination sum problems remains the same, which is called backtracking.

In this article, we will present several approaches which are all based on the backtracking algorithm.

Approach 1: Backtracking with Counters
Intuition

As a reminder, backtracking is a general algorithm for finding all (or some) solutions to some computational problems. The idea is that it incrementally builds candidates to the solutions, and abandons a candidate ("backtrack") as soon as it determines that the candidate cannot lead to a final solution.

In our problem, we could incrementally build the combination by adding numbers one at a time, and once we find the current combination is not valid, we backtrack (by abondoning the last number we added to the combination) and try another candidate.

As we mentioned before, this problem is an extention of an earlier problem called 39. Combination Sum. As it turns out, we could build the solutions upon the solutions to the problem of 39. Combination Sum, by incorporating the differences between the problems.

There are two differences between this problem and the earlier problem:

In this problem, each number in the input is not unique. The implication of this difference is that we need some mechanism to avoid generating duplicate combinations.

In this problem, each number can be used only once. The implication of this difference is that once a number is chosen as a candidate in the combination, it will not appear again as a candidate later.

There are several ways to adapt the solutions of 39. Combination Sum to solve this problem.

In this approach, we will present a solution with the concept of counter. Rather than treating each number as a candidate, we treat groups of unique numbers as candidates.

To demonstrate the idea, we showcase how it works with a concrete example in the following graph:

counter demo

As one can see from the above graph, if we treat each appearance of the number 2 as a candidate, then we would generate multiple instances of the same combination of [2, 2]. For instance, the first and second appearances of the number 2 will lead to the same combination as the second and the third appearances of the number 2.

However, we could count the appearance of each unique number. And then we can use the generated counter table during the construction of the combination.

For instance, starting from the empty combination, we first pick the number 2 as the first candidate into the combination. In the counter table, we then update the count of the number 2, which remains 2 instances rather than 3. In the next step, again we pick another instance of the number 2 into the combination. With this pick, we reach the desired target number which is 4.

As one can see, with the counter table, at each step, we could ensure that each combination we generate would be unique at the end.

Algorithm

Here are a few steps on how we can implement the above intuition:

First of all, we build a counter table out of the given list of numbers.

We would then use this counter table during our backtracking process, which we define as the function backtrack(comb, remain, curr, candidate_groups, results). In order to keep the state of each backtracking step, we use quite a few parameters in the function, which we elaborate as follows:

comb: the combination we built so far at each step.
remain: the remaining sum that we need to fill, in order to reach the target sum.
curr: the cursor that points to the current group of number that we are using from the counter table.
counter: the current counter table.
results: the final combinations that have the target sum.
At each invocation of the backtracking function, we first check if we reach the target sum (i.e. sum(comb) = target), and if we should stop the exploration simply because the sum of current combination goes beyond the desired target.

If there is still some remaining sum to fill, we will then iterate through the current counter table to pick the next candidate.

Once we pick a candidate, we then continue the exploration by invocating the backtrack() function with the updated states.
More importantly, at the end of each exploration, we need to revert the state we updated before, in order to start off a clean slate for the next exploration. It is due to this backtracking operation, the algorithm got its name.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                # make a deep copy of the current combination
                #   rather than keeping the reference.
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]

                if freq <= 0:
                    continue

                # add a new element to the current combination
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)

                # continue the exploration with the updated combination
                backtrack(comb, remain - candidate, next_curr, counter, results)

                # backtrack the changes, so that we can try another candidate
                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []  # container to hold the final combinations
        counter = Counter(candidates)
        # convert the counter table to a list of (num, count) tuples
        counter = [(c, counter[c]) for c in counter]

        backtrack(comb = [], remain = target, curr = 0,
                  counter = counter, results = results)

        return results

Complexity Analysis

Let NN be the size of the input array.

Time Complexity: \mathcal{O}(2^N)O(2 
N
 )

In the worst case, our algorithm will exhaust all possible combinations from the input array. Again, in the worst case, let us assume that each number is unique. The number of combination for an array of size NN would be 2^N2 
N
 , i.e. each number is either included or excluded in a combination.

Additionally, it takes \mathcal{O}(N)O(N) time to build a counter table out of the input array.

Therefore, the overall time complexity of the algorithm is dominated by the backtracking process, which is \mathcal{O}(2^N)O(2 
N
 ).

Space Complexity: \mathcal{O}(N)O(N)

We first build a counter table, which in the worst case will consume \mathcal{O}(N)O(N) space.

We use the variable comb to keep track of the current combination we build, which requires again \mathcal{O}(N)O(N) space.

In addition, we apply recursion in the algorithm, which will incur additional memory consumption in the function call stack. In the worst case, the stack will pile up to \mathcal{O}(N)O(N) space.

To sum up, the overall space complexity of the algorithm is \mathcal{O}(N) + \mathcal{O}(N) + \mathcal{O}(N) = \mathcal{O}(N)O(N)+O(N)+O(N)=O(N).

Note: we did not take into account the space needed to hold the final results of combination in the above analysis.

Approach 2: Backtracking with Index
Intuition

There is another way to adapt the solution of 39. Combination Sum.

Rather than building a counter table to group the numbers together explicitly, we could sort the input, which could also group all the same numbers together.

Similar to the solution of 39. Combination Sum, we iterate through the sorted input array, via backtracking to build the combinations.

In addition, we need to do some tricks with the index of the iteration, in order to avoid generating duplicated combinations.

We demonstrate the idea with the same example in the previous approach, i.e. input = [2, 5, 2, 2].

index demo

As we can see from the above graph, once we sort the input array, the occurrance of each unique number would be adjacent to each other.

In the above graph, we show the moment we start to process the group of number 2, with the iteration index pointed to the beginning of the group.

Next, we need to move the index forward, in order to choose the next number to be added to the combination. More importantly, we need to skip certain positions, in order to avoid the generation of duplicated combinations. We skip the position if the following two condtions are met:

1). next_curr > curr: we will pick the number at the current curr position into the combination, regardless the other conditions. This is important, since the iteration should allow us to select multiple instances of a unique number into the combination.

2). candidates[next_curr] == candidates[next_curr-1]: we will skip the occurances all repetitive numbers in-between, e.g. we skip the second and third occurance of number 2 in this round of backtracking.

The combined effects of the above sorting and iterating operations are equivalent to the previous approach with counter table.

Algorithm

It would be clearer to see how the above tricks with index play out in the algorithm.

Similiar to the previous approach, we implement the backtracking process with the function named backtrack(comb, remain, curr, results), but with less parameters, compared to the previous approach.

The bulk of the function remains the same as the solution of 39. Combination Sum, except the specific conditions on the index as we discussed before.

In addition, we optimize the backtracking a bit by adopting the measure of early stopping, i.e. once the sum of current combination exceeds the target, we can stop the exploration for the rest of the numbers. Because all the numbers are positve, as specified in the problem, the sum of combination will increase monotonically. It is needless to explore more combinations whose sum goes beyond the desired target.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, results):

            if remain == 0:
                # make a deep copy of the resulted combination
                results.append(list(comb))
                return

            for next_curr in range(curr, len(candidates)):

                if next_curr > curr \
                  and candidates[next_curr] == candidates[next_curr-1]:
                    continue

                pick = candidates[next_curr]
                # optimization: skip the rest of elements starting from 'curr' index
                if remain - pick < 0:
                    break

                comb.append(pick)
                backtrack(comb, remain - pick, next_curr + 1, results)
                comb.pop()

        candidates.sort()

        comb, results = [], []
        backtrack(comb, target, 0, results)

        return results

Complexity Analysis

Let NN be the size of the input array.

Time Complexity: \mathcal{O}(2^N)O(2 
N
 )

In the worst case, our algorithm will exhaust all possible combinations from the input array, which in total amounts to 2^N2 
N
  as we discussed before.

The sorting will take \mathcal{O}(N \log N)O(NlogN).

To sum up, the overall time complexity of the algorithm is dominated by the backtracking process, which is \mathcal{O}(2^N)O(2 
N
 ).

Space Complexity: \mathcal{O}(N)O(N)

We use the variable comb to keep track of the current combination we build, which requires \mathcal{O}(N)O(N) space.

In addition, we apply recursion in the algorithm, which will incur additional memory consumption in the function call stack. In the worst case, the stack will pile up to \mathcal{O}(N)O(N) space.

To sum up, the overall space complexity of the algorithm is \mathcal{O}(N) + \mathcal{O}(N) = \mathcal{O}(N)O(N)+O(N)=O(N).

Note: we did not take into account the space needed to hold the final results of combination in the above analysis.
"""
"""
#100%
#sample 24 ms submission
class Solution:
    def combinationSum2(self, nums, target: int):
        output = []
        size = len(nums)
        nums.sort()
        
        def helper(start, currList, currTarget):
            if currTarget == 0:
                output.append(currList[:])
            
            for i in range(start, size):
                if currTarget - nums[i] < 0:
                    break
                    
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                helper(i + 1, currList + [nums[i]], currTarget - nums[i])
        
        helper(0, [], target)
        return output

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.combinationSum2(input1,input2)
        print(ans)
        return ans

assert test([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 24) == [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
"""