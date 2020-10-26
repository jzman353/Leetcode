"""Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

#119/154 Wrong Answer
def insert(intervals, newInterval):
    total_intervals = []
    output = []
    def prep_total_intervals(total_intervals, interval):
        total_intervals.append(interval[0])
        if interval[1] - interval[0] > 0:
            total_intervals.append(interval[0] + .5)
            total_intervals.append(interval[1])
        return total_intervals

    for interval in intervals:
        prep_total_intervals(total_intervals,interval)

    for i in range(newInterval[0],newInterval[1]+1):
        if i not in total_intervals:
            total_intervals.append(i)
        if i != newInterval[1]:
            if i + .5 not in total_intervals:
                total_intervals.append(i + .5)
    print(total_intervals)
    total_intervals = sorted(total_intervals)

    temp = [total_intervals[0]]
    new = False
    double = False
    for i in range(1,len(total_intervals)):
        if new:
            if not double:
                temp = [total_intervals[i-1]]
            else:
                temp = [total_intervals[i]]
                double = False
            new = False
        else:
            if i != len(total_intervals)-1:
                if ".5" in str(total_intervals[i]) or ".5" in str(total_intervals[i-1]):
                    continue
                else:
                    temp.append(total_intervals[i-1])
                    output.append(temp)
                    new = True
                if ".5" not in str(total_intervals[i-1]) and ".5" not in str(total_intervals[i]) and ".5" not in str(total_intervals[i + 1]):
                    output.append([total_intervals[i],total_intervals[i]])
                    new = True
                    double = True
                    continue
            else:
                if ".5" not in str(total_intervals[i - 1]):
                    temp.append(total_intervals[i-1])
                    output.append(temp)
                    output.append([total_intervals[i], total_intervals[i]])
                else:
                    temp.append(total_intervals[i])
                    output.append(temp)
    return output

"""#28/154 Memory limit exceeded #[[1,5],[10,11],[15,2147483647]],[5,7]
def insert(intervals, newInterval):
    total_intervals = []
    output = []
    for interval in intervals:
        for i in range(interval[0],interval[1]+1):
            total_intervals.append(i)
            if i != interval[1]:
                total_intervals.append(i+.5)
    for i in range(newInterval[0],newInterval[1]+1):
        if i not in total_intervals:
            total_intervals.append(i)
        if i != newInterval[1]:
            if i + .5 not in total_intervals:
                total_intervals.append(i + .5)
    #print(total_intervals)
    total_intervals = sorted(total_intervals)

    temp = [total_intervals[0]]
    new = False
    double = False
    for i in range(1,len(total_intervals)):
        if new:
            if not double:
                temp = [total_intervals[i-1]]
            else:
                temp = [total_intervals[i]]
                double = False
            new = False
        else:
            if i != len(total_intervals)-1:
                if ".5" in str(total_intervals[i]) or ".5" in str(total_intervals[i-1]):
                    continue
                else:
                    temp.append(total_intervals[i-1])
                    output.append(temp)
                    new = True
                if ".5" not in str(total_intervals[i-1]) and ".5" not in str(total_intervals[i]) and ".5" not in str(total_intervals[i + 1]):
                    output.append([total_intervals[i],total_intervals[i]])
                    new = True
                    double = True
                    continue
            else:
                if ".5" not in str(total_intervals[i - 1]):
                    temp.append(total_intervals[i-1])
                    output.append(temp)
                    output.append([total_intervals[i], total_intervals[i]])
                else:
                    temp.append(total_intervals[i])
                    output.append(temp)
    return output"""

print(insert([[1,3],[6,9]], [2,5])) #[[1,5],[6,9]]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) #[[1,2],[3,10],[12,16]]
print(insert([[0,1],[5,5],[6,7],[9,11]], [12,21])) #[[0, 1], [5, 5], [6, 7], [9, 11], [12, 21]]
print(insert([[0,1],[5,5]], [1,2])) #[[0, 2], [5, 5]]

#print(insert([[1,5],[10,11],[15,2147483647]],[5,7])) #28/154
print(insert([[1,5]], [2,3])) # [[1,5]] #119/154

"""
def insert(self, intervals, I):
    #res contains all the intervals before any influence from the newly inserted interval, i counts the number of intervals that will come after any influence from the newly inserted interval
    res, i = [], -1
    for count, (x, y) in enumerate(intervals):
        #If the current interval comes before any influence from the newly inserted interval
        if y < I[0]:
            res.append([x, y])
        #If the current interval comes after any influence from the newly inserted interval
        elif I[1] < x:
            i -= 1
            break
        #If there is some overlap
        else:
            I[0] = min(I[0], x)
            I[1] = max(I[1], y)
            
    return res + [I] + intervals[i+1:]
"""