from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def clear(self):
        self.r = None
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = None
        return u

    def find_eq(self, x: object) -> object:
        # todo
        temp = self.r
        while temp is not None:
            if x < temp.x:
                temp = temp.left
            elif x > temp.x:
                temp = temp.right
            else:
                return temp
        return temp

    def find_last(self, x: object) -> BinaryTree.Node:
        # todo
        w = self.r
        prev = None
        while w is not None:
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev

    def find(self, x: object) -> object:
        # todo
        w = self.r
        z = None
        while w is not None:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return z

    def add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        # todo
        if p is None:
            self.r = u
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True

    def add_node(self, u: BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)

    def add(self, key: object, value: object) -> bool:
        # todo
        p = self.find_last(key)
        return self.add_child(p, BinaryTree.Node(key, value))

    def get(self, key: object) -> object:
        # todo
        x = self.find(key)
        if x is not None:
            return x.v
        else:
            return None

    def splice(self, u: BinaryTree.Node):
        # todo
        if u.left is not None:
            s = u.left
        else:
            s = u.right

        p = None

        if self.r is u:
            self.r = s
        else:
            p = u.parent
            if u == p.left:
                p.left = s
            else:
                p.right = s
        if s is not None:
            s.parent = p
        self.n -= 1

    def remove_node(self, u: BinaryTree.Node):
        # todo
        if u is not None:
            if u.right is None or u.left is None:
                self.splice(u)
            else:
                w = u.right
                while w.left is not None:
                    w = w.left
                u.x = w.x
                u.v = w.v
                self.splice(w)
            return u.v
        return None

    def remove(self, x: object) -> bool:
        # todo
        w = self.find(x)
        self.remove_node(w)
        pass

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.x
            u = self.next_node(u)
