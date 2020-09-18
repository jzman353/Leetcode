#8.6%

"""Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

    0 <= i < j < k < arr.length
    |arr[i] - arr[j]| <= a
    |arr[j] - arr[k]| <= b
    |arr[i] - arr[k]| <= c

Where |x| denotes the absolute value of x.

Return the number of good triplets.



Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
"""
def countGoodTriplets(arr, a: int, b: int, c: int) -> int:
    try:
        ans = 0
        i = 0
        j = 1
        k = 2
        length = len(arr)
        while i < length - 2:
            while j < length - 1:
                while k < length:
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans+=1
                    k+=1
                j+=1
                k = j+1
            i+=1
            j = i+1
            k = j+1
        return ans
    except:
        return 0


print(countGoodTriplets([3,0,1,1,9,7],7,2,3))
print(countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1))
print(countGoodTriplets(arr = [7,3,7,3,12,1,12,2,3], a = 5, b = 8, c = 1))#16/92
