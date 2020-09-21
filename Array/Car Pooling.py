#15%
"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true

Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true

Constraints:

    trips.length <= 1000
    trips[i].length == 3
    1 <= trips[i][0] <= 100
    0 <= trips[i][1] < trips[i][2] <= 1000
    1 <= capacity <= 100000

Sort the pickup and dropoff events by location, then process them in order.
"""

import timeit
#To sort a list of lists, use itemgetter from operator or key=lambda

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        stack = []
        delete = []
        for i in trips:
            for count, j in enumerate(stack):
                if i[1] >= j[1]:
                    capacity += j[0]
                    delete.append(count)
            if delete:
                for j in reversed(delete):
                    stack.pop(j)
                delete = []
            capacity -= i[0]
            if capacity < 0:
                return False
            stack.append([i[0],i[2]])
        return True






if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.carPooling(input1,input2)
        print(ans)

    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    test(trips, capacity) #False
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 5
    test(trips, capacity) #True
    trips = [[2,1,5],[3,5,7]]
    capacity = 3
    test(trips, capacity) #True
    trips = [[3,2,7],[3,7,9],[8,3,9]]
    capacity = 11
    test(trips, capacity) #True
    trips = [[3, 7, 9], [3, 2, 7], [8, 3, 9]]
    capacity = 11
    test(trips, capacity)  # True
    #41
    trips = [[9,3,4],[9,1,7],[4,2,4],[7,4,5]]
    capacity = 23
    test(trips, capacity)  # True
    #14
    trips = [[10,5,7],[10,3,4],[7,1,8],[6,3,4]]
    capacity = 24
    test(trips, capacity)  # True

    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))

    """
    class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pois = []
        for num, start, end in trips:
            pois.extend([(start, num), (end, -num)])
        num_used = 0
        for _, num in sorted(pois):
            num_used += num
            if num_used > capacity:
                return False
        return True
        
    class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if trips is None or not trips:
            return True
        
        N = len(trips)
        
        schedule = []
        for t in trips:
            schedule.append((t[1], t[0]))
            schedule.append((t[2], -t[0]))
            
        schedule.sort()
        
        count = 0
        for s in schedule:
            count += s[1]
            if count > capacity:
                return False
            
        return True
    """