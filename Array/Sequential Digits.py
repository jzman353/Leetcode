#75.19

"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

 

Constraints:
    10 <= low <= high <= 10^9
"""
import timeit

class Solution:
    def sequentialDigits(self, low: int, high: int):
        ans = []
        num_digits_low = (len(str(low)))
        num_digits_high = (len(str(high)))
        break2 = False
        for digit in range(num_digits_high-num_digits_low+1):
            if digit > 7:
                break
            for i in range(1,9):
                temp = 0
                length = num_digits_low+digit
                for j in range(length):
                    if i+length-1 < 10:
                        temp = temp + (i+j)*10**(num_digits_low-(j+1))
                    else:
                        temp = 0
                        break2 = True
                        break
                if break2:
                    break2 = False
                    break
                temp = round(10**(digit)*temp)
                if temp <= high and temp >= low and temp != 0:
                    ans.append(temp)
        return ans


if __name__ == '__main__':
    def test(input1,input2):
        Test = Solution()
        ans = Test.sequentialDigits(input1,input2)
        print(ans)


    low = 10
    high = 70
    test(low, high)
    low = 100
    high = 300
    test(low,high)
    low = 1000
    high = 13000
    test(low, high)
    low = 10
    high = 13000
    test(low, high)
    low = 13000
    high = 1300000000000000000
    test(low, high)
    low = 10
    high = 1300000000000000000
    test(low, high)


    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))

    """
    def sequentialDigits(self, low: int, high: int) -> List[int]:
    out = []
    queue = deque(range(1,10))
    while queue:
        elem = queue.popleft()
        if low <= elem <= high:
            out.append(elem)
        last = elem % 10
        if last < 9: queue.append(elem*10 + last + 1)
                
    return out
        
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        arr = set()
        num = low
        while num <= high:
            step = 10**int(len(str(num))-1)
            curr = num//step
            n = curr+1
            for i in range(n, 10):
                curr = curr *10 + n
                n +=1
                if curr <= high and curr >= low and n <= 10:
                    arr.add(curr)
            num += step
        return sorted(arr)
    """