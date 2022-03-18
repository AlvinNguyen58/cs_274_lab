from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node():
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=np.object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key: int) -> int:
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object) -> object:
        # todo
        h = self._hash(key)
        for i in range(len(self.t[h]) - 1):
            if self.t[h][i].key == key:
                return self.t[h][i].value
        return None
        pass

    def add(self, key: object, value: object):
        # todo
        if self.find(key) is not None:
            return False
        else:
            hash_value = self._hash(key)
            self.t[hash_value].append(key, value)
            self.n += 1
        pass

    def remove(self, key: int) -> object:
        # todo
        if self.find(key) is None:
            return None
        else:
            hash_value = self._hash(key)
            list = self.t[hash_value]
            temp = None
            for i in range(len(list) - 1):
                if list[i].key == key:
                    self.n -= 1
                    temp = list.remove(i)
        if len(self.t) > 3 * self.n:
            self.resize()
        return temp
        pass

    def resize(self):
        # todo
        if self.n == 2 ** self.d:
            self.d += 1
        if self.d ** 2 >= 3 * self.n:
            self.d -= 1
        temp = self.alloc_table(self.d)
        for i in range(len(self.t - 1)):
            for j in range(len(self.t[i] - 1)):
                current_element = self.t[i].get[j]
                h = hash(current_element.key)
                temp[h].append(current_element)
        t = temp
        pass

    def __str__(self):
        s = "\n"
        for i in range(len(self.t)):
            s += str(i) + " : "
            for j in range(len(self.t[i])):
                k = self.t[i].get(j) # jth node at ith list
                s += "(" + str(k.key) + ", " + str(k.value) + "); "

            s += "\n"
        return s
