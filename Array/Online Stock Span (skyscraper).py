'''
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

 

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.
 

Note:

Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.
'''

#Doesn't accept this solution anymore because too slow
class StockSpanner:

    def __init__(self):
        self.stock_prices = []
        self.prev_max = 0
        self.prev_output = 1
        self.prev_output_index = 0
        self.max = 0
        

    def next(self, price: int) -> int:
        self.stock_prices.append(price)
        if len(self.stock_prices) == 1:
            self.max = price
            return 1
        else:
            output = 1
            
            '''
            if price > self.stock_prices[len(self.stock_prices)-2] and price < self.prev_max:
                self.prev_output += 1
                return self.prev_output
            elif price < self.stock_prices[len(self.stock_prices)-2]:
                self.prev_output = 1
                return 1
            else:
            '''
            #if price < self.prev_max:
            if price >= self.max:
                self.max = price
                return len(self.stock_prices)
            for count,item in enumerate(self.stock_prices[len(self.stock_prices)-2::-1]):
                #print("count: "+str(count))
                if item <= price:
                    output += 1
                else:
                    self.prev_max = item
                    self.prev_output_index = count
                    break
                #print(output)
                #print()
            self.prev_output = output
            return output
            '''
            else:
                output = self.prev_output
                print("go: "+str(len(self.stock_prices)-2-self.prev_output_index))
                print(str(self.stock_prices[len(self.stock_prices)-2-self.prev_output_index]))
                print(self.prev_output_index)
                print()
                for item in self.stock_prices[len(self.stock_prices)-2-self.prev_output_index::-1]:
                    #print(item)
                    #print(price)
                    if item <= price:
                        output += 1
                    else:
                        self.prev_max = item
                        break
                    #print(output)
                    #print()
                self.prev_output = output
                return output
            '''
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

'''
Approach 1: Stack
Intuition

Clearly, we need to focus on how to make each query faster than a linear scan. In a typical case, we get a new element like 7, and there are some previous elements like 11, 3, 9, 5, 6, 4. Let's try to create some relationship between this query and the next query.

If (after getting 7) we get an element like 2, then the answer is 1. So in general, whenever we get a smaller element, the answer is 1.

If we get an element like 8, the answer is 1 plus the previous answer (for 7), as the 8 "stops" on the same value that 7 does (namely, 9).

If we get an element like 10, the answer is 1 plus the previous answer, plus the answer for 9.

Notice throughout this evaluation, we only care about elements that occur in increasing order - we "shortcut" to them. That is, from adding an element like 10, we cut to 7 [with "weight" 4], then to 9 [with weight 2], then cut to 11 [with weight 1].

A stack is the ideal data structure to maintain what we care about efficiently.

Algorithm

Let's maintain a weighted stack of decreasing elements. The size of the weight will be the total number of elements skipped. For example, 11, 3, 9, 5, 6, 4, 7 will be (11, weight=1), (9, weight=2), (7, weight=4).

When we get a new element like 10, this helps us count the previous values faster by popping weighted elements off the stack. The new stack at the end will look like (11, weight=1), (10, weight=7).

Complexity Analysis

Time Complexity: O(Q), where Q is the number of calls to StockSpanner.next. In total, there are Q pushes to the stack, and at most Q pops.

Space Complexity: O(Q).

Runtime: 460 ms Beats 72%
class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight

Runtime: 424 ms
class StockSpanner:

    def __init__(self):
        self.stack = []    

    def next(self, price: int) -> int:
        res = 1
        stack = self.stack
        while stack and stack[-1][0] <= price:
            _, prev = stack.pop()
            res += prev
        stack.append((price, res))
        # print(stack)
        return res
'''




