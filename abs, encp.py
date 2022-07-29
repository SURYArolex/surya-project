class Library:
    def __init__(self,books):
        self.books = books

    def listofbooks(self):
        print("Available Books in Library")
        for book in self.books:
            print(book)

    def borrowbooks(self,borrowbook):
        if borrowbook in self.books:
            print("Your Book is Available Get your Book Now")
            self.books.remove(borrowbook)
        else:
            print("Book is not Available")
    def receivebook(self,receivebook):
        print("You have Returned the Book")
        self.books.append(receivebook)
books = ['c', 'c++', 'java', 'DSA', 'python', 'rdbms', 'mobile computing',]
jp = Library(books)

msg = """
      **** 1.Display Book ****
      **** 2.Borrow  Book ****
      **** 3.Return  Book ****
"""
while True:
    print(msg)
    ch = int(input("----- Enter your Choice -------: "))
    if ch == 1:
        jp.listofbooks()
    elif ch == 2:
        book = input("----- Enter Book Name To Borrow:")
        jp.borrowbooks(book)
    elif ch == 3:
        book = input("----- Enter Book Name To Return:")
        jp.receivebook(book)
    else:
        print(" **** Your choice is Incorrect ")
        print(" **** Thank you **** Please come again !!!! ")
        quit()