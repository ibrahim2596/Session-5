class Book:
    def __init__(self , title , author , ISBN):
        self.title = title
        self.author = author
        self.__ISBN = ISBN
        self.available = True 
    def display_info(self):
        print(f"{self.title}")
        print(f"for: {self.author}")
        print(f"ISBN: {self.__ISBN}")
        print(f"Available: {self.available}") 
    def is_available(self):
        return self.available
    def borrow_book(self):
        self.available = False
    def return_book(self):
        self.available = True
    def ISBN(self):
        return f"{self.__ISBN}"
    def get_ISBN(self):
        return self.__ISBN
    def set_ISBN(self , new_ISBN):
        self.__ISBN = new_ISBN
    
class Memeber:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id
        self.borrowed_books = []
    def membership_id(self):
        return f"{self.__membership_id}"
    def get_membership_id(self):
        return self.__membership_id
    def member_info(self):
        print(f"Member: {self.name}")
        print(f"Membership ID: {self.__membership_id}")
    def set_membeship_id(self , new_membeship_id):
        self.__membership_id = new_membeship_id

    def borrow_book(self, book):
        if book.is_available():                 #is_available here for the Book in Class Book
            self.borrowed_books.append(book)    #add the book to [] that done at borrowed_books by the member
            book.borrow_book()                  #to know the book is borrowed
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)   ##remove the book from [] that done at borrowed_books by the member
            book.return_book()                 #to know the book is returned
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} doesn't borrow {book.title}")
            
class StaffMember(Memeber):
    def __init__(self, name, membership_id , staff_id):
        super().__init__(name , membership_id)
        self.staff_id = staff_id
    def add_book(self , title , author , ISBN):
        add_book = Book(title , author , ISBN)      #Used Book class to add the book 
        print(f"Staff member {self.name} added {add_book.title}")
        return add_book 