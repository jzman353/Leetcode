"""
1854. Maximum Population Year
Easy

You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.

Example 1:

Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
Example 2:

Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation:
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.

Constraints:

1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050
"""
#69%
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort(key=lambda x: x[0])
        years = Counter()
        for i in logs:
            for j in range(i[0],i[1]):
                years[j] += 1
        return years.most_common(1)[0][0]

"""
This solutions is a lot more efficient than mine. Mine will iterate through the span of all the lives while
this solution will only ever care about the indexes themselves. It correctly figures out that the earliest max
population year will have to be one within the list of birth years. Therefore, it just iterates through the birth years.
Deaths will cancel out (skip) births if they are the same year or if the death happened first and hasn't been accounted 
for yet. The current population only ever goes up because it is only allowed to go up if all the previous deaths are
accounted for and there is a new birth ready.

sample 24 ms submission
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        n = len(logs)
        birthes = sorted([birth for birth, _ in logs])
        deathes = sorted([death for _, death in logs])
        
        curr_population = 0
        max_population = 0
        max_population_year = -1
        death_ind = 0
        birth_ind = 0
        
        while birth_ind < n:
            if deathes[death_ind] <= birthes[birth_ind]:
                death_ind += 1
            else:
                curr_population += 1
                if curr_population > max_population:
                    max_population = curr_population
                    max_population_year = birthes[birth_ind]
            birth_ind += 1
        
        return max_population_year

This approach is a little less efficient because it doesn't skip over any births but is much more readable.
It also figures out that the result must be in the list of birth years and therefore doesn't care about the years
in between birth and death. It adds the net births-deaths for every year in the list of births and deaths. It would
look cleaner if they just used defaultdict(int)

sample 28 ms submission
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        yearToNumBirthsAndDeaths = {}
        
        for log in logs:
            if log[0] not in yearToNumBirthsAndDeaths:
                yearToNumBirthsAndDeaths[log[0]] = 1
            else:
                yearToNumBirthsAndDeaths[log[0]] += 1
            
            if log[1] not in yearToNumBirthsAndDeaths:
                yearToNumBirthsAndDeaths[log[1]] = -1
            else:
                yearToNumBirthsAndDeaths[log[1]] -= 1
        
        population = 0
        
        maxPop = 0
        
        yearOfMaxPop = 0
        
        for year in sorted(yearToNumBirthsAndDeaths):
            population += yearToNumBirthsAndDeaths[year]
            if population > maxPop:
                maxPop = population
                yearOfMaxPop = year
        
        return yearOfMaxPop

My version of this solution would look like this:
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = defaultdict(int)
        for i in logs:
            years[i[0]] += 1
            years[i[1]] -= 1
        max_pop = 0
        population = 0
        for i in sorted(years.keys()):
            population += years[i]
            if population > max_pop:
                max_pop = population
                max_year = i
        return max_year
"""