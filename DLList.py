from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: np.object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        # todo
        if i < self.n / 2:
            p = self.dummy.next
            for k in range(0, i):
                p = p.next
        else:
            p = self.dummy
            for k in range(self.n, i, -1):
                p = p.prev
        return p
        pass

    def get(self, i) -> np.object:
        # todo
        return self.get_node(i).x
        pass

    def set(self, i: int, x: np.object) -> np.object:
        # todo
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y
        pass

    def add_before(self, w: Node, x: np.object) -> Node:
        # todo
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u
        pass

    def add(self, i: int, x: np.object):
        # todo
        self.add_before(self.get_node(i), x)
        pass

    def _remove(self, w: Node):
        # todo
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        pass

    def remove(self, i: int):
        if i < 0 or i > self.n or self.n == 0:
            raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: np.object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        # todo
        for i in range(0, round(self.n/2)):
            if self.get(i) != self.get(self.n - i - 1):
                return False
        return True
        pass

    def reverse(self):
        current = self.dummy.next
        head = current
        prev = self.dummy
        while current != self.dummy:
            temp = current.next
            current.next = prev
            current.prev = temp
            prev = current
            current = temp
        self.dummy.next = prev
        self.dummy.prev = head


    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
