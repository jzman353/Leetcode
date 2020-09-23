class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be
        created. """
        self.heapList = [0]
        self.currentSize = 0
        self.capacity = capacity

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other
           items using the < operator"""
        if not self.is_full():
            self.heapList.append(item)
            self.currentSize = self.currentSize + 1
            self.perc_up(self.currentSize)
            return True
        else:
            return False

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        return self.heapList[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty():
            return None
        else:
            retval = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop()
            self.perc_down(1)
            return retval

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        i = 1
        output = []
        while i <= self.currentSize:
            output.append(self.heapList[i])
            i += 1
        return output

    def build_heap(self, alist):
        """Discards all items in the current heap and builds a heap from
        the items in alist using the bottom-up construction method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        if len(alist) <= self.capacity:
            pass
        else:
            self.capacity = len(alist)

        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        if self.currentSize <= 0:
            return True
        else:
            return False

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        if self.currentSize == self.capacity:
            return True
        else:
            return False

    def get_capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.currentSize

    # Used in dequeue
    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    # Used in dequeue (in percDown)
    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # Used in Enqueue
    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        self.build_heap(alist)
        next_item = self.dequeue()
        alist[:] = []
        while next_item is not None:
            alist.append(next_item)
            next_item = self.dequeue()
        alist.reverse()
