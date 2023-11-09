import unittest
from defines import POUND_SIGN
from book import Book
from utils import Utils as u

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book()

    def test_default_values(self):
        self.assertEqual(self.book.title, '')
        self.assertEqual(self.book.description, '')
        self.assertEqual(self.book.price, 0)
        self.assertEqual(self.book.url, '')
        self.assertEqual(self.book.genre, '')
        self.assertEqual(self.book.num_of_reviews, 0)
        self.assertEqual(self.book.availability, 0)
        self.assertEqual(self.book.rating, 0)

    def test_string_representation(self):
        self.book.title = 'Princess Between Worlds (Wide-Awake Princess #5)'
        self.book.description = ('Just as Annie and Liam are busy making plans to travel the world, a witch '
                                 'shows up and gives them a collection...')
        self.book.price = 13.34
        self.book.url = 'http://books.toscrape.com/catalogue/princess-between-worlds-wide-awake-princess-5_919/index.html'
        self.book.genre = 'Fiction'
        self.book.num_of_reviews = 25
        self.book.availability = 10
        self.book.rating = 4
        expected_string = (
            "Title: Princess Between Worlds (Wide-Awake Princess #5)\n"
            "Genre: Fiction\n"
            "Description: Just as Annie and Liam are busy making plans to travel the world,"
            " a witch shows up and gives them a collection...\n"
            "Price: " + POUND_SIGN + "13.34\n"
            "URL: http://books.toscrape.com/catalogue/princess-between-worlds-wide-awake-princess-5_919/index.html\n"
            "Number of Reviews: 25\n"
            "Availability: In stock (10 available)\n"
            "Star Rating: 4"
        )
        self.assertEqual(str(self.book), expected_string)

    def test_string_representation_partial_fields(self):
        self.book.title = 'Booked'
        self.book.price = 17.49
        self.book.availability = 5
        expected_string = (
            "Title: Booked\n"
            "Genre: \n"
            "Description: \n"
            "Price: " + POUND_SIGN + "17.49\n"
            "URL: \n"
            "Number of Reviews: 0\n"
            "Availability: In stock (5 available)\n"
            "Star Rating: 0"
        )
        self.assertEqual(str(self.book), expected_string)

    def test_string_representation_missing_description(self):
        self.book.title = 'Wall and Piece'
        self.book.price = 44.18
        self.book.url = 'http://books.toscrape.com/catalogue/wall-and-piece_971/index.html'
        self.book.genre = 'Biography'
        self.book.num_of_reviews = 0
        self.book.availability = 18
        self.book.rating = 4
        expected_string = (
            "Title: Wall and Piece\n"
            "Genre: Biography\n"
            "Description: \n"
            "Price: " + POUND_SIGN + "44.18\n"
            "URL: http://books.toscrape.com/catalogue/wall-and-piece_971/index.html\n"
            "Number of Reviews: 0\n"
            "Availability: In stock (18 available)\n"
            "Star Rating: 4"
        )
        self.assertEqual(str(self.book), expected_string)

    def test_is_instance(self):
        self.assertIsInstance(self.book, Book)

    def test_invalid_rating_value(self):
        max_rating = 5
        self.book.rating = max_rating
        test_rating = 6

        self.assertNotEqual(self.book.rating, test_rating)

        min_rating = 0
        self.book.rating = min_rating
        test_rating = -1

        self.assertGreaterEqual(self.book.rating, min_rating)
        self.assertNotEqual(self.book.rating, test_rating)
        self.assertLess(test_rating, min_rating)

    def test_negative_availability_value(self):
        real_availability = 0
        self.book.availability = real_availability
        test_availability = -10

        self.assertNotEqual(self.book.availability, test_availability)
        self.assertLess(test_availability, self.book.availability)
        self.assertGreaterEqual(self.book.availability, 0)

    def test_valid_book_url(self):
        self.book.url = 'http://books.toscrape.com/catalogue/masks-and-shadows_909/index.html'
        self.assertTrue(not u.check_url_for_single_book_url(self.book.url))

    def test_invalid_book_url(self):
        self.book.url = 'http://books.toscrape.com/catalogue/princess-between-worlds-widehtml'
        self.assertFalse(u.check_url_for_single_book_url(self.book.url))

    def test_title(self):
        self.book.title = ''
        self.assertIs(self.book.title, '')

        self.assertIsInstance(self.book.title, str)

        self.book.title = 123
        self.assertNotIsInstance(self.book.title, str)

    def test_invalid_num_of_reviews(self):
        num_of_reviews = 0
        self.book.num_of_reviews = num_of_reviews
        test_num_of_reviews = -1

        self.assertGreaterEqual(self.book.num_of_reviews, num_of_reviews)
        self.assertNotEqual(self.book.num_of_reviews, test_num_of_reviews)
        self.assertLess(test_num_of_reviews, num_of_reviews)


if __name__ == '__main__':
    unittest.main()
