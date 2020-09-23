class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item #Data stored in the Node
        self.next = None #Next Node that contains data (item of larger value or None)
        self.prev = None #Previous Node that contains data (item of smaller value or None)

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''
    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.dummy = None #Should be the lowest value of the list

    # None -> Boolean
    # Returns True if list empty, false otherwise
    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.dummy == None

    # number -> Boolean
    # Returns True if item is added to list, false otherwise
    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        iterate = self.dummy
        if self.is_empty(): #Empty list so place item as first item
            self.dummy = Node(item)
            return True
        while iterate.item < item: #Iterate through ordered list until iterate contains item that is greater than (or equal to) the item you need to insert or until you reach  the end of the list
            if iterate.next != None:
                iterate = iterate.next
            else: 
                break #The end of the list is reached
        if iterate.item == item:#If the item is already in the list, do not add it again and return False.
            return False 
        if iterate.next == None and iterate.item < item:#If item is the new largest item
            new = Node(item)
            new.prev = iterate
            iterate.next = new
            return True
        #insert item at front or middle
        new = Node(item)
        new.next = iterate
        new.prev = iterate.prev
        #insert middle
        if iterate.prev != None:
            iterate.prev.next = new
        #insert front
        else:
            self.dummy = new
        iterate.prev = new
        return True

    # Number -> Boolean
    # Returns True if item was removed from list, false otherwise
    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        if self.is_empty(): #Empty list so return False
            return False
        if self.dummy.item == item: # item is first in list
            self.dummy = self.dummy.next
            if self.size() != 0:
                self.dummy.prev = None
            return True
        iterate = self.dummy
        while iterate.item != item:# iterate through list until matching or at end of list
            if iterate.next != None:
                iterate = iterate.next
            else:
                break
        if iterate.next != None: #item is in middle of list
            iterate.prev.next = iterate.next
            iterate.next.prev = iterate.prev
            return True
        if iterate.item == item: #item is in end of list
            iterate.prev.next = None
            return True
        else: #item is not in list
            return False
    
    # Number -> Number
    # Returns index of number if list contains number, None otherwise
    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        iterate  = self.dummy
        index = 0
        # iterate through list unless iterate is None which has no attribute 'item' so item not in list
        try:
            while iterate.item != item:
                iterate = iterate.next
                index += 1
        except:
            return None #iterate == None
        return index#iterate.item is item so return index

    # Number -> Number
    # Returns number at index if list contains index, raises Index Error otherwise
    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        
        if index < 0:
            raise IndexError("Index is negative")

        iterate = self.dummy
        while index != 0:
            try:
                iterate = iterate.next
                index = index - 1
                if iterate == None:#if given index is 1 over max index
                    raise IndexError("Index is >= size of list")
            except:
                if iterate == None:
                    raise IndexError("Index is >= size of list")
        # index is valid and we are at correct position
        self.remove(iterate.item)
        return iterate.item

    # Number -> Boolean
    # Returns index of number if list contains number, None otherwise
    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.find_item(self.dummy, item)

    # Node, number -> Boolean
    # Returns True if item is found, False if item is not in list
    def find_item(self, iterate, item):
        if iterate == None:
            return False
        else:
            return (iterate.item == item) or self.find_item(iterate.next, item)

    # None -> List
    # Returns python list representation of ordered list
    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        iterate = self.dummy
        ordered_list = []

        while iterate != None:
            ordered_list.append(iterate.item)
            iterate = iterate.next
        return ordered_list

    # None -> List
    # Returns python list representation of ordered list (but in reverse order)
    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        ordered_list = self.python_list()
        return self.reverse_list(ordered_list)

    # List -> List
    # Reverses ordered list
    def reverse_list(self, ordered_list):
        if len(ordered_list) == 0:
            return []
        reversed_list = [ordered_list[-1]] + self.reverse_list(ordered_list[:-1]) #Appends the rightmost item of the ordered list to the reversed list and then appends from right to left
        return reversed_list

    # None -> int
    # Returns index of number if list contains number, None otherwise
    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.count_indices(self.dummy)

    # Node -> int
    # Recursively counts the number of items in a list
    def count_indices(self, iterate):
        if iterate == None:
            return 0
        else:
            return 1 + self.count_indices(iterate.next)






