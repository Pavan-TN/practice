# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Library Class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book.title, "-", book.author)

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book issued successfully")
                return
        print("Book not available")

    def return_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print("Book returned successfully")


# User Login Class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        u = input("Enter username: ")
        p = int(input("Enter password: "))

        if u == self.username and p == self.password:
            print("Login Successful")
            return True
        else:
            print("Login Failed")
            return False


# Create Library
lib = Library()

lib.add_book(Book("Python", "Guido"))
lib.add_book(Book("AI Basics", "John"))
lib.add_book(Book("Data Science", "Andrew"))

# Create User
user = User("pavan", 1234)

# Login Check
if user.login():

    lib.show_books()

    while True:
        print("\n1.Issue Book")
        print("2.Return Book")
        print("3.Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter book title: ")
            lib.issue_book(name)

        elif choice == 2:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            lib.return_book(title, author)

        elif choice == 3:
            print("Thank you")
            break