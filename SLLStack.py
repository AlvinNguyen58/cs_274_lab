from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x: np.object):
            self.next = None
            self.x = x

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def push(self, x: np.object):
        # todo
        u = self.Node(x)
        u.next = self.head
        self.head = u
        if self.n == 0:
            self.tail = u
        self.n += 1
        return x
        pass

    def pop(self) -> np.object:
        # todo
        if self.n == 0:
            raise IndexError() # checking precondition
        pop = self.head.x
        self.head = self.head.next
        if self.n - 1 == 0:
            tail = None
        return pop
        pass

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
