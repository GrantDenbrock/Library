import Book
from Sorting import *

class Library(object):
    sorting_algos = {'merge': merge,
                     'count': count,
                     'select': select,
                     'bubble':bubble,
                    }

    def __init__(self):
        self.shelf=[]
    
    def add_books(self,books):
        for book in books:
            self.shelf.append(book)

    def generate_books(self,n):
        import random
        self.add_books([random.randint(100000,999999) for _ in range(n)])
        
    def sort(self,algo='merge'):
        self.shelf = self.sorting_algos[algo](self.shelf)

    def __str__(self):
        return str(self.shelf)
