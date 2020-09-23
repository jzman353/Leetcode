
class Node:
  def __init__(self, item):
    self.item = item
    self.next = None
    self.prev = None

class Queue:
  '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

  def __init__(self, capacity):
    #Creates an empty Queue with a specified capacity
    self.capacity = capacity
    self.head = None    #First item in, first item ready to go out
    self.tail = None    #Last item in, last item ready to go out
    self.num_items = 0  #Count of the total values in the Queue

  def is_empty(self):
    '''Returns True if the Queue is empty, and False otherwise
       MUST have O(1) performance'''
    return self.num_items == 0

  def is_full(self):
    '''Returns True if the Queue is full, and False otherwise
       MUST have O(1) performance'''
    return self.num_items == self.capacity

  def enqueue(self, item):
    '''If Queue is not full, enqueues (adds) item to Queue 
       If Queue is full when enqueue is attempted, raises IndexError
       MUST have O(1) performance'''
    if self.is_full(): 
      raise IndexError("queue is full")#Raises IndexError when Queue is full
    if self.is_empty(): #Fills the first item in the queue
        self.head = Node(item) 
        self.tail = self.head 
    else: #Fills every item after the first item in the queue
        self.tail.next = Node(item) 
        self.tail.next.prev = self.tail 
        self.tail = self.tail.next
    self.num_items = self.num_items+1

  def dequeue(self):
    '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
       If Queue is empty when dequeue is attempted, raises IndexError
       MUST have O(1) performance'''
    if self.is_empty():
        raise IndexError("queue is empty")#Raises IndexError when Queue is empty
    if self.num_items == 1: #Removes the final value in the queue
        temp = self.head.item 
        self.head.prev = None
        self.num_items = self.num_items-1
        return temp
    else:                   #Removes a value in the queue as long as it isn't the last one
        temp = self.head.item 
        self.head = self.head.next
        self.head.prev = None
        self.num_items = self.num_items-1
        return temp

  def size(self):
    '''Returns the number of elements currently in the Queue, not the capacity
       MUST have O(1) performance'''
    return self.num_items

  def get_head(self):
    return self.head.item

  def get_tail(self):
    return self.tail.item

