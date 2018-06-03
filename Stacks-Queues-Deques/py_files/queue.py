"""
A queue is an ordered collection of items where the addition of new items happens at one end,
called the “rear,” and the removal of existing items occurs at the other end, commonly called the “front.”
As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that
time when it is the next element to be removed.

The most recently added item in the queue must wait at the end of the collection. The item that has been in the
collection the longest is at the front. This ordering principle is sometimes called FIFO, first-in first-out.
It is also known as “first-come first-served.”

The simplest example of a queue is the typical line that we all participate in from time to time.
We wait in a line for a movie, we wait in the check-out line at a grocery store, and we wait in the cafeteria line.
The first person in that line is also the first person to get serviced/helped.

Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the queue. It needs no parameters and returns an integer.
"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

from nose.tools import assert_equal

class TestQueue:

    def testIsEmtpty(self,queue):
        assert_equal(queue.isEmpty(), True)
        print("Is Empty Passed")

    def testItemsNotEmpty(self,queue):
        assert_equal(queue.isEmpty(), False)
        print("Is not empty Passed")

t = TestQueue()
q = Queue()
t.testIsEmtpty(q)
q.enqueue(4)
t.testItemsNotEmpty(q)