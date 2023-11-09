import unittest
from sorting import Sorting
from book import Book
import defines as de

class TestSorting(unittest.TestCase):

    def setUp(self):
        self.book1 = Book()
        self.book1.price = 20
        self.book1.availability = 10
        self.book1.rating = 4

        self.book2 = Book()
        self.book2.price = 25
        self.book2.availability = 16
        self.book2.rating = 3

        self.book3 = Book()
        self.book3.price = 18
        self.book3.availability = 12
        self.book3.rating = 5

        self.book_list = [self.book1, self.book2, self.book3]

    def test_sort_books_by_rating_ascending(self):
        sorting = Sorting([de.RATING, de.ASCENDING], self.book_list)
        result = sorting.process_sorting()
        expected = [self.book2, self.book1, self.book3]
        self.assertEqual(result, expected)

    def test_sort_books_by_rating_descending(self):
        sorting = Sorting([de.RATING, de.DESCENDING], self.book_list)
        result = sorting.process_sorting()
        expected = [self.book3, self.book1, self.book2]
        self.assertEqual(result, expected)

    def test_sort_books_by_price_ascending(self):
        sorting = Sorting([de.PRICE, de.ASCENDING], self.book_list)
        result = sorting.process_sorting()
        expected = [self.book2, self.book1, self.book3]
        self.assertEqual(result, expected)

    def test_sort_books_by_price_descending(self):
        sorting = Sorting([de.PRICE, de.DESCENDING], self.book_list)
        result = sorting.process_sorting()
        expected = [self.book3, self.book1, self.book2]
        self.assertEqual(result, expected)

    def test_sort_books_by_availability_ascending(self):
        sorting = Sorting([de.AVAILABILITY.lower(), de.ASCENDING], self.book_list)
        result = sorting.process_sorting()
        expected = [self.book1, self.book3, self.book2]
        self.assertEqual(result, expected)

    def test_sort_books_by_availability_descending(self):
        sorting = Sorting([de.AVAILABILITY.lower(), de.DESCENDING], self.book_list)
        result = sorting.process_sorting()
        expected = [self.book2, self.book3, self.book1]
        self.assertEqual(result, expected)

    def test_sort_books_invalid_criteria_name(self):
        sorting = Sorting(["Invalid Criteria", de.ASCENDING], self.book_list)
        with self.assertRaises(ValueError):
            sorting.process_sorting()

    def test_sort_books_empty_list(self):
        empty_list = []
        sorting = Sorting([de.RATING, de.ASCENDING], empty_list)
        result = sorting.process_sorting()
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()

