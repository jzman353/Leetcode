"""
225. Implement Stack using Queues
Easy

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False


Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.


Follow-up: Can you implement the stack using only one queue?
"""
#60%
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []



    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.values.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.values.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.values[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.values



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
Using deque:
class MyStack:
    
    def __init__(self):
        self.queue = collections.deque()
        self.size = 0
        
    def push(self, x):
        self.queue.append(x)
        for _ in range(self.size):
            self.queue.append(self.queue.popleft())
        self.size += 1

    # @return nothing
    def pop(self):
        self.size -= 1
        return self.queue.popleft()
        

    # @return an integer
    def top(self):
        # queue peek operation
        return self.queue[0]

    # @return an boolean
    def empty(self):
        print(self.size)
        if self.size==0:
            return True
        else:
            return False
"""