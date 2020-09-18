#54%
"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5



Example 2:

Input: 3
Output: False

"""
import timeit
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def isPerfectSquare(num: int) -> bool:
            k = num ** (1 / 2)
            if k.is_integer(): #if (k == (int) k)
                return True
            else:
                return False

        for a in range(math.ceil(math.sqrt(c))+1):
            test = c-a**2
            if test >= 0 and isPerfectSquare(test):
                return True
        return False

if __name__ == '__main__':
    def test(instructions):
        Test = Solution()
        #print(Test.judgeSquareSum(c))

    c = 0 #121 True
    test(c)

    c = 2 #121 True
    test(c)

    c = 1000000000 #25 True
    test(c)

    c = 3 #2 False
    test(c)

    c = 5 #1 True
    test(c)

    print(timeit.timeit("test(1000000000)", setup="from __main__ import test", number=10))

"""
Approach 1: Brute Force
public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            for (long b = 0; b * b <= c; b++) {
                if (a * a + b * b == c)
                    return true;
            }
        }
        return false;
    }
}

Approach 2: Better Brute Force
We can improve the last solution, if we make the following observation. For any particular aaa chosen, the value of bbb required to satisfy the equation a2+b2=ca^2 + b^2 = ca2+b2=c will be such that b2=c−a2b^2 = c - a^2b2=c−a2.

public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            int b =  c - (int)(a * a);
            int i = 1, sum = 0;
            while (sum < b) {
                sum += i;
                i += 2;
            }
            if (sum == b)
                return true;
        }
        return false;
    }
}

Approach 3: Using Sqrt Function
public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            double b = Math.sqrt(c - a * a);
            if (b == (int) b)
                return true;
        }
        return false;
    }
}

Approach 4: Binary Search
public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            int b = c - (int)(a * a);
            if (binary_search(0, b, b))
                return true;
        }
        return false;
    }
    public boolean binary_search(long s, long e, int n) {
        if (s > e)
            return false;
        long mid = s + (e - s) / 2;
        if (mid * mid == n)
            return true;
        if (mid * mid > n)
            return binary_search(s, mid - 1, n);
        return binary_search(mid + 1, e, n);
    }
}

Approach 5: Fermat Theorem
public class Solution {
    public boolean judgeSquareSum(int c) {
        for (int i = 2; i * i <= c; i++) {
            int count = 0;
            if (c % i == 0) {
                while (c % i == 0) {
                    count++;
                    c /= i;
                }
                if (i % 4 == 3 && count % 2 != 0)
                    return false;
            }
        }
        return c % 4 != 3;
    }
}
"""