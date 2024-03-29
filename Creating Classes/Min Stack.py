"""
155. Min Stack
Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:

    Methods pop, top and getMin operations will always be called on non-empty stacks.
"""
#17%
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> None:
        self.l.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return min(self.l)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
#Stores the minimum value (that was put in the stack before that element) every time a new item is pushed
class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        minv = x
        if self.stack: minv = min(self.stack[-1][1], minv)
        self.stack.append((x, minv))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""