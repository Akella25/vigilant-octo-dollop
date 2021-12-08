import unittest
import datetime
from TDD import Book

class TestBook(unittest.TestCase):
    def test_add_book(self):
        new_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        self.assertEqual(new_book.title, 'Dune')
        self.assertEqual(new_book.author, 'Frank Herbert')
        self.assertEqual(new_book.published, datetime.date(1965, 8, 1))
    
    def test_book_to_str(self):
        new_book = Book('Dune', '1965, 8, 1', 'Frank Herbert')
        self.assertEqual(str(new_book), 'Frank Herbert\'s Dune')

    def test_books_list(self):
        Book.items = []
        first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        second_book = Book('The Lord of the Rings', datetime.date(1954, 7, 29), 'J. R. R. Tolkien')
        self.assertEqual(len(Book.items), 2)

    def test_find_by_title(self):
        Book.items = []
        first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        second_book = Book('The Lord of the Rings', datetime.date(1954, 7, 29), 'J. R. R. Tolkien')
        book_found = Book.find_by_title('DUNE')
        self.assertEqual(book_found, [first_book])

    def test_find_by_author(self):
        Book.items = []
        first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        second_book = Book('The Lord of the Rings', datetime.date(1954, 7, 29), 'J. R. R. Tolkien')
        book_found = Book.find_by_author('Tolkien')
        self.assertEqual(book_found, [second_book])

    def test_book_comparison(self):
        Book.items = []
        first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        second_book = Book('Dune', datetime.date.today(), 'Frank Herbert')
        third_book = Book('Children of Dune', datetime.date(1976, 4, 1), 'Frank Herbert')
        fourth_book = Book('Dune', datetime.date(1965, 8, 1), 'Brian Herbert')
        self.assertTrue(first_book == second_book)
        self.assertFalse(first_book == third_book)
        self.assertFalse(first_book == fourth_book)

    def test_book_hash(self):
        Book.items = []
        new_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        self.assertEqual(hash(new_book), hash(('Dune', 'Frank Herbert')))

        '''

    def test_published_after(self):
        first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        second_book = Book('The Lord of the Rings', datetime.date(1954, 7, 29), 'J. R. R. Tolkien')
        book_found = Book.published_after(year=1960)
        self.assertEqual(book_found, [first_book])

    def test_add_movie(self):
        new_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        new_movie = Movie('Dune', datetime.date(2021, 9, 3), 'Denis Villeneuve', new_book)
        self.assertEqual(new_movie.name, 'Dune')
        self.assertEqual(new_movie.release_day, datetime.date(2021, 9, 3))
        self.assertEqual(new_movie.directed_by, 'Denis Villeneuve')
        self.assertEqual(new_movie.based_on, new_book)

    def test_list_movies(self):
        first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        first_movie = Movie('Dune', datetime.date(2021, 9, 3), 'Denis Villeneuve', first_book)
        second_book = Book('The Lord of the Rings', datetime.date(1954, 7, 29), 'J. R. R. Tolkien')
        second_movie = Movie('The Lord of the Rings', datetime.date(2001, 12, 10), 
            'Peter Jackson', second_book)
        third_movie = Movie('Dune', datetime.date(1984, 12, 3), 'Raffaella De Laurentiis', first_book)
        self.assertEqual(len(Movie.items), 3)
        self.assertTrue(first_movie in Movie.items)
        self.assertTrue(second_movie in Movie.items)
        self.assertTrue(third_movie in Movie.items)

    def test_sorted_movies(self):
        first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        first_movie = Movie('Dune', datetime.date(2021, 9, 3), 'Denis Villeneuve', first_book)
        other_movie = Movie('Dune', datetime.date(1984, 12, 3), 'Raffaella De Laurentiis', first_book)
        second_book = Book('The Lord of the Rings', datetime.date(1954, 7, 29), 'J. R. R. Tolkien')
        second_movie = Movie('The Lord of the Rings', datetime.date(2001, 12, 10), 
            'Peter Jackson', second_book)
        sorted_movies = Movie.sort_items()
        self.assertEqual(sorted_movies, [other_movie, second_movie, first_movie])

    def test_find_movie_by_book(self):
        first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        first_movie = Movie('Dune', datetime.date(2021, 9, 3), 'Denis Villeneuve', first_book)
        second_book = Book('The Accidental Billionaires', datetime.date(2009, 7, 14), 'Ben Mezrich')
        second_movie = Movie('The Social Network', datetime.date(2010, 9, 24), 
            'David Fincher', second_book)
        movies_for_book = Movie.for_book('Billionaires')
        self.assertEqual(movies_for_book, [second_book])

    def test_recommended_movies(self):
        first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
        first_movie = Movie('Dune', datetime.date(2021, 9, 3), 'Denis Villeneuve', first_book)
        second_book = Book('The Lord of the Rings', datetime.date(1954, 7, 29), 'J. R. R. Tolkien')
        second_movie = Movie('The Lord of the Rings', datetime.date(2001, 12, 10), 
            'Peter Jackson', second_book)
        third_movie = Movie('Dune', datetime.date(1984, 12, 3), 'Raffaella De Laurentiis', first_book)
        self.assertEqual(third_movie.recommendations, [first_movie])
        '''


