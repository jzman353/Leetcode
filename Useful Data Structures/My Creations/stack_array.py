class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''
    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.top = 0

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        if self.top == 0:
          return True
        else:
          return False

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        if self.top == self.capacity:
        	return True
        else:
        	return False

    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
       	  raise IndexError("stack is full")
        else:
          #Push
          self.items[self.top] = item
          self.top = self.top+1
          

    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
          raise IndexError("stack is empty")
        else:
          #pop
          temp = self.items[self.top-1]
          self.items[self.top-1]=None
          self.top=self.top-1
          return temp
          

    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
          raise IndexError("stack is empty")
        else:
          #peek
          return self.items[self.top-1]
        
    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.top
