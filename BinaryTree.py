import ArrayQueue


class BinaryTree:
    class Node:
        def __init__(self, x: object, v=None):
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_key(self, x):
            self.x = x

        def set_val(self, v):
            self.v = v

        def insert_left(self):
            self.left = BinaryTree.Node('')
            self.left.parent = self
            return self.left

        def insert_right(self):
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

        def __str__(self):
            if self.v is None:
                return str(self.x)
            return f"({self.v})"

    def __init__(self):
        self.r = None

    def depth(self, u: Node) -> int:
        # todo
        current = u
        d = 0
        while current is not self.r:
            current = current.parent
            d += 1
        return d

    def _size(self, u: Node) -> int:
        # todo
        if u is None:
            return 0
        return 1 + self._size(u.left) + self._size(u.right)

    def size(self) -> int:
        return self._size(self.r)

    def size2(self) -> int:
        # todo
        u = self.r
        prev = None
        n = 0
        while u is not None:
            if prev == u.parent:
                n += 1
                if u.left is not None:
                    next = u.left
                elif u.right is not None:
                    next = u.right
                else:
                    next = u.parent
            elif prev == u.left:
                if u.right is not None:
                    next = u.right
            else:
                next = u.parent
            prev = u
            u = next
        return n

    def _height(self, u: Node) -> int:
        # todo
        if u is None:
            return 0
        return 1 + max(self._height(u.left), self._height(u.right))

    def height(self) -> int:
        return self._height(self.r)

    def _in_order(self, u: Node, arr) -> list:
        # todo
        if u:
            self._in_order(u.left, arr)
            arr.append(u.__str__())
            self._in_order(u.right, arr)
        return arr

    def in_order(self) -> list:
        arr = []
        return self._in_order(self.r, arr)

    def _pre_order(self, u: Node, arr: list) -> list:
        # todo
        if u:
            arr.append(u.__str__())
            self._pre_order(u.left, arr)
            self._pre_order(u.right, arr)
        return arr

    def pre_order(self) -> list:
        arr = []
        return self._pre_order(self.r, arr)

    def _post_order(self, u: Node, arr: list) -> list:
        # todo
        if u:
            self._post_order(u.left, arr)
            self._post_order(u.right, arr)
            arr.append(u.__str__())
        return arr

    def post_order(self) -> list:
        arr = []
        return self._post_order(self.r, arr)

    def bf_traverse(self):
        # todo
        q = ArrayQueue.ArrayQueue()
        arr = []
        if self.r is not None:
            q.add(self.r)
        while q.size() > 0:
            u = q.remove()
            arr.append(u.__str__())
            if u.left is not None:
                q.add(u.left)
            if u.right is not None:
                q.add(u.right)
        return arr

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left != None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def __str__(self):
        nodes = self.bf_traverse()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)
