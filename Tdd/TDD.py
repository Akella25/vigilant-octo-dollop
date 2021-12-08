import datetime


class Book:
    items = []

    def __init__(self, title, published, author):
        self.title = title
        self.author = author
        self.published = published
        Book.items.append(self)

    def __str__(self):
        return f'{self.author}\'s {self.title}'

    def __repr__(self):
        return f'{self.author}\'s {self.title}'

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title

    def __hash__(self):
        return hash((self.title, self.author))

    @classmethod
    def find_by_title(cls, title):
        find_books = []
        for item in cls.items:
            if title.lower() == item.title.lower():
                find_books.append(item)
        return find_books

    @classmethod
    def find_by_author(cls, author):
        find_books = []
        for item in cls.items:
            if author.lower() in item.author.lower():
                find_books.append(item)
        return find_books

    @classmethod
    def published_after(cls, year):
        list_book = []
        for book in Book.items:
            if book.published.year >= year:
                list_book.append(book)
        return list_book




class Movie:
    items = []

    def __init__(self, name, release_day, directed_by, based_on=None):
        self.name = name
        self.release_day = release_day
        self.directed_by = directed_by
        self.based_on = based_on
        Movie.items.append(self)

    def __str__(self):
        return f'{self.release_day}'

    @staticmethod
    def bubble_sort(array, field):
        n = len(array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if getattr(array[j], field) > \
                        getattr(array[j + 1], field):
                    array[j], array[j + 1] = array[j + 1], array[j]

    @staticmethod
    def sort_items():
        sort_items = Movie.items
        Movie.bubble_sort(Movie.items, 'release_day')
        return sort_items

    @staticmethod
    def for_book(books):
        list_mov = []
        for mov in Movie.items:
            if books in mov.based_on.title:
                list_mov.append(mov.based_on)
        return list_mov

    @property
    def recommendations(self):
        empty_list = []
        for movie in Movie.items:
            if self.based_on.title == movie.based_on.title:
                if movie != self:
                    empty_list.append(movie)
        return empty_list


first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
second_book = Book('Dune', datetime.date.today(), 'Frank Herbert')
third_book = Book('Children of Dune', datetime.date(1976, 4, 1), 'Frank Herbert')
fourth_book = Book('Dune', datetime.date(1965, 8, 1), 'Brian Herbert')
print(first_book == second_book)
print(first_book == third_book)
print(first_book == fourth_book)
