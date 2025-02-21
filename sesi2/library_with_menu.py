# Library Management System
# Class: Book
# Attributes: title, author, ISBN, available
# Methods: borrowbook(), returnbook()

class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available
        
    def borrowbook(self):
        if self.available:
            self.available = False
            print(f"{self.title} is borrowed.")
        else:
            print(f"{self.title} is not available.")
            
    def returnbook(self):
        if not self.available:
            self.available = True
            print(f"{self.title} is returned.")
        else:
            print(f"{self.title} is already available.")
            
books = []

while True:
    print("--Menu--")
    print("1. List Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    
    menu = input("Select menu: ")
    
    if menu == "1":
        for index, book in enumerate(books):
            print(f"{index+1} - {book.title}")
            
    elif menu == "2":
        title = input("Insert title: ")
        author = input("Insert author: ")
        ISBN = input("Insert ISBN: ")
        books.append(Book(title, author, ISBN))
        
    elif menu == "3":
        index = int(input("Choose book index: "))
        books[index-1].borrowbook()
        
    elif menu == "4":
        index = int(input("Choose book index: "))
        books[index-1].returnbook()
        
    elif menu == "5":
        break
        
    else:
        print("Invalid choice")