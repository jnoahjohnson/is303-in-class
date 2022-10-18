class Book():
    def __init__(self, title, author, pages):
        # Protected Attribute
        self.__title = title
        self.author = author
        self.pages = pages

    def get_book_title(self):
        return self.__title

    def set_book_title(self, new_title):
        self.__title = new_title

class RomanceBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author, pages)
        self.genre = "Romance"

    def get_book_title(self):
        return "This is a romance book: " + self._title

newBook = RomanceBook("Edenbrooke", "Julianne Donaldson", 2012)
print(newBook.get_book_title())
# Output: ERROR

