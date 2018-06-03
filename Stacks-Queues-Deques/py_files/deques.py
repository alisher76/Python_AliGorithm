"""
A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue.
It has two ends, a front and a rear, and the items remain positioned in the collection. What makes a
deque different is the unrestrictive nature of adding and removing items. New items can be added at either
the front or the rear. Likewise, existing items can be removed from either end. In a sense, this hybrid linear
structure provides all the capabilities of stacks and queues in a single data structure.

It is important to note that even though the deque can assume many of the characteristics of stacks and queues,
it does not require the LIFO and FIFO orderings that are enforced by those data structures. It is up to you to
make consistent use of the addition and removal operations.

Methods and Attributes
Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the deque. It needs no parameters and returns an integer.
"""
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


from nose.tools import assert_equal


class TestDeque:

    def testEmpty(self, deque):
        assert_equal(deque.isEmpty(), True)
        print("Test Passed")


    def testContains(self,deque):
        assert_equal(deque.size(), 1)
        print("Contains passed TestPasses")


    def testFront(self,deque):
        assert_equal(deque[len(deque.items) - 1], 5)
        print("Front TestPasses")

    def testRear(self, deque):
        assert_equal(deque.items[0], 2)
        print("test Rear Passed")

d = Deque()
t = TestDeque()
t.testEmpty(d)
d.addFront(5)
d.addRear(2)
t.testFront(d)
t.testRear(d)
