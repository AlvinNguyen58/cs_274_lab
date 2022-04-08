from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0
        
    def clear(self):
        self.r = None
        self.n = 0

    def new_node(self, x, v=None):
        u = BinaryTree.Node(x, v)
        u.left = u.right = u.parent = None
        return u

    def find_eq(self, x : object) -> object:
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
        
    def find_last(self, x : object) -> BinaryTree.Node:
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

        pass

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
        
    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
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
        
    def add_node(self, u : BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)

    def add(self, key : object, value : object) -> bool:
        # todo
        p = self.find_last(key)
        return self.add_child(p, self.new_node())

    def get(self, key : object) -> object:
        # todo

        pass
    
    def splice(self, u: BinaryTree.Node):
        # todo
        if u.left is None:
            s = u.left
        else:
            s = u.right
        if u is self.r:
            self.r = s
            p = None
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s is None:
            s.parent = p
        self.n -= 1

    def remove_node(self, u : BinaryTree.Node):
        # todo
        pass 

    def remove(self, x : object) -> bool:
        # todo
        pass 
             
    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.x
            u = self.next_node(u)


            
