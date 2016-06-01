import Book

class Library(self):
	def __init__(self):
		self.shelf=[]
	
	def add_books(self,books):
		for book in books:
			self.shelf.append(book)

	def generate_books(self,n):
		import random
		self.add_books([random.randint(100000,999999) for _ in range(n)])
		
		
