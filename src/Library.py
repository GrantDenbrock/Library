import Book

class library(self):
	def __init__(self):
		self.shelf=[]
	
	def addbook(self,books):
		for book in books:
			self.shelf.append(book)
