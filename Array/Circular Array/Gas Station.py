#12.6%
"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

    If there exists a solution, it is guaranteed to be unique.
    Both input arrays are non-empty and have the same length.
    Each element in the input arrays is a non-negative integer.

Example 1:

Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input:
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        size = len(gas)
        i=0
        while i < size:
            Reset = False
            gas_quantity = gas[i]
            j = 1
            while i+j < size and not Reset:
                gas_quantity -= cost[i + j - 1]
                if gas_quantity < 0:
                    i += 1
                    j = 1
                    Reset = True
                else:
                    gas_quantity += gas[i + j]
                    j += 1
            j = 0
            while j < i and not Reset:
                gas_quantity -= cost[j - 1]
                if gas_quantity < 0:
                    i += 1
                    j = 1
                    Reset = True
                else:
                    gas_quantity += gas[j]
                    j += 1
            if j == i:
                gas_quantity -= cost[j - 1]
                if gas_quantity < 0:
                    return -1
                else:
                    return i
        if i == size:
            return -1


if __name__ == '__main__':
    def test(input1,input2):
        Test = Solution()
        ans = Test.canCompleteCircuit(input1,input2)
        print(ans)

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    test(gas, cost)

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    test(gas, cost)

"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        minSpare = 99999
        spare = index = 0
        for i,v in enumerate(zip(gas,cost)):
            spare += v[0] - v[1]
            if spare <= minSpare:
                minSpare = spare
                index = i
        if spare < 0: return -1
        return (index + 1)%len(gas)
        
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1
"""