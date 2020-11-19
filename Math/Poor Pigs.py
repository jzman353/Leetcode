"""
458. Poor Pigs
Hard

There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. They all look identical. If a pig drinks the poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?

Answer this question, and write an algorithm for the general case.



General case:

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the poisonous bucket within p minutes? There is exactly one bucket with poison.



Note:

    A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
    After a pig has instantly finished drinking buckets, there has to be a cool down time of m minutes. During this time, only observation is allowed and no feedings at all.
    Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).

"""

# There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. They all look identical. If a pig drinks the poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?
# You could definitely do it with 1000 pigs in 15 minutes
# If you had 250 pigs you could have them sample one new bucket every 15 miunutes until one dies
# If you had 125 pigs you could have them each sample 8 buckets and then have 8 of the remaining 124 pigs try the 8 that the dead pig tried  30 min
# If you had 1000/15/4 = 62.5 = 63 pigs, you can have each sample 16 buckets, then use 16 of the remaining pigs to figure out which has poison 30 min
# With 32 pigs, each can sample 31 buckets with one sampling 32, then the remaining 31 pigs can find the 1/31 or 1/32 with poison in two tries 45 min
# With 16 pigs, half of them will sample 62 and the other half will sample 63 buckets. With the remaining 15 pigs, each can sample 4-5 buckets. With the remaining 14 pigs, 5 of them can test the remaining 4-5 uncertain buckets
# With 8 pigs, every pig will sample 125 buckets, the remaining 7 pigs will sample 18 buckets each, the remaining 6 pigs will sample 3 buckets each, the remaining 5 pigs can find the 1/3 poisin bucket
# With 7 pigs, every pig will sample 143 buckets, the remaining 6 pigs will sample 21 buckets each, the remaining 5 pigs will sample 5 buckets each, the remaining 4 pigs can't cant sample all 5 to make a final determination
# Leetcode says we can do it with 5
# With 5 pigs,
# 1. every pig will sample 200 buckets > does not work
# 2. With five pigs, there will be 4 overlaps. Some of the sections overlap the two pigs, meaning that both will die.
# 1000/(5+4) = 112 bucket sections. All of the pigs will cover two sections
#If two pigs die, the remaining 3 pigs will need to find the bucket among 112
#112/(3+2) = 23
# If two of the pigs die, one will need to find the bucket among 23
# 3. For the first round, no pigs overlap.
# 4 pigs remain, find among 200
# 200/(4+3) = 29 with 2 pigs
#One key to solving this problem is understanding that at least one group of buckets should go untested each round. In this case, more information is found and all the pigs survive
# 4. 1000/(10) = 100 bucket sections among 5 pigs (each overlaps 2 and last one is left undrank)
# 100/6 = 16 among 3 pigs
#Doesn't work

#https://leetcode.com/problems/poor-pigs/discuss/935172/Two-diagrams-to-help-understanding
#If one round, use base 1+1=2
#If N=8, in base 2 that will be 000-111 when zero encoded
# Each pig will be a digit (ones, tens, hundreds). If the digit is 1, the pig will drink it.
# If N=9 and rounds = 2, use base 2+1=3
#One pig will encode the first digit and the other will encode the second digit.
#No pig will drink the bits that are 0s
#If a pig dies in round 1, their respective digit is a 2
#If a pig dies in round 2, their respective digit is a 1
#If they survive all rounds, their respective digit is a 0

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest//minutesToDie
        i = 0
        while (rounds+1)**(i) < buckets: # rounds+1 is the base, (rounds+1)**(i) is the number of states that can be represented
            i += 1
        return i

if __name__ == '__main__':
    def test(input1, input2, input3):
        Test = Solution()
        ans = Test.poorPigs(input1, input2, input3)
        print(ans)
        return ans

    assert test(1000, 15, 60) == 5
    assert test(1, 15, 60) == 0
    assert test(1, 60, 60) == 0

"""
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets)/log(minutesToTest//minutesToDie + 1))
"""