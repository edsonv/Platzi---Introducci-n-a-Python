class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"El título '{self.title}' ha sido prestado.")
        else:
            print(f"El título '{self.title}' no está disponible.")

    def return_book(self):
        self.is_available = True
        print(f"el título '{self.title}' ha sido devuelto.")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro '{book.title}' no está disponible.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro '{book.title}' no está en la lista de prestados.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro '{book.title}' ha sido añadido a la biblioteca.")

    def add_user(self, user):
        self.users.append(user)
        print(f"El usuario '{user.name}' ha sido añadido a la biblioteca.")

    def list_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.is_available:
                print(f"- {book.title} por {book.author}")


book1 = Book("El Principito", "Antoine de Saint-Exupéry")
book2 = Book("1984", "George Orwell")
book3 = Book("Cien años de soledad", "Gabriel García Márquez")

user1 = User("Juan Pérez", "001")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_user(user1)
library.list_available_books()

user1.borrow_book(book1)
library.list_available_books()

user1.return_book(book1)

library.list_available_books()
