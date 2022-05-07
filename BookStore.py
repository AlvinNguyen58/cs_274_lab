import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import MaxQueue
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import AdjacencyList
import time

import algorithms


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)

            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        # todo
        n = 0
        for i in range(self.bookCatalog.size()):
            if n >= 50:
                break
            book = self.bookCatalog.get(i)
            if infix in book.title:
                print(book)
                n += 1
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            info = u.__str__()
            print(f"removeFromShoppingCart {info}")
        elapsed_time = time.time() - start_time
        print(f"Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        print(self.shoppingCart.max())

    def addBookByKey(self, key):
        start_time = time.time()
        if self.bookIndices.find(key) is not None:
            b = self.bookIndices.find(key)
            s = self.bookCatalog.get(b)
            self.shoppingCart.add(s)
            print(f"Added title: {s.title}")
        else:
            print("Book not found.")
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix):
        start_time = time.time()
        if self.sortedTitleIndices.find(prefix) is not None:
            b = self.sortedTitleIndices.find(prefix)
            s = self.sortedTitleIndices.get(b)
            self.shoppingCart.add(s)
            print(f"Added title: {s.title}")
        else:
            print("Book not found.")
        elapsed_time = time.time() - start_time
        print(f"addBookByPrefix Completed in {elapsed_time} seconds")

    def bestsellers_with(self, infix, structure, n=0):
        if infix == "":
            raise IndexError("Invalid infix.")
        else:
            start_time = time.time()
            if structure == 1:

                bestsellers = BinarySearchTree.BinarySearchTree()
                for i in range(self.bookCatalog.size()):
                    b = self.bookCatalog.get(i)
                    if bestsellers.size() > n:
                        break
                    if infix in b.title:
                        bestsellers.add(b.rank, b)
                a = bestsellers.in_order()
                for b in a:
                    print(b.__str__())

            elif structure == 2:
                start_time = time.time()
                bestsellers = BinaryHeap.BinaryHeap()
                for i in range(self.bookCatalog.size()):
                    b = self.bookCatalog.get(i)
                    if bestsellers.size() > n:
                        break
                    if infix in b.title:
                        b.rank = b.rank * -1
                        bestsellers.add(b)
                for i in range(bestsellers.size()):
                    book = bestsellers.remove()
                    book.rank = book.rank * -1
                    print(book)
                else:
                    print("Invalid data structure.")
            elapsed_time = time.time() - start_time
            print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")

    def sort_catalog(self, s):
        start_time = time.time()
        if s == 1:
            algorithms.merge_sort(self.bookCatalog)
        elif s == 2:
            algorithms.quick_sort(self.bookCatalog)
        elif s == 3:
            algorithms.quick_sort(self.bookCatalog, False)
        else:
            print("Invalid algorithm")
        elapsed_time =time.time() - start_time
        print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")

    def search_by_prefix(self, prefix, algo):
        start_time = time.time()
        n = 0
        if algo == 1:
            book_copy = self.bookCatalog
            while algorithms.linear_search(book_copy, prefix) != -100:
                print(book_copy.remove(algorithms.linear_search(book_copy, prefix)))
                n += 1
        elif algo == 2:
            book_copy = self.bookCatalog
            algorithms.quick_sort(book_copy)
            while algorithms.binary_search(book_copy, prefix) != -100:
                print(book_copy.remove(algorithms.binary_search(book_copy, prefix)))
                n += 1
        else:
            print("Invalid algorithm")
        elapsed_time = time.time() - start_time
        print(f"Found {n} of books with prefix {prefix} in {elapsed_time}")

    def display_catalog(self, n):
        i = 0
        for book in self.bookCatalog:
            if i >= int(n):
                break
            print(book)
            i += 1