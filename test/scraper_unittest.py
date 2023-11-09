import unittest

import defines
from scraper import Scraper


# from scraper import Scraper

class TestScraper(unittest.TestCase):

    def setUp(self):
        # Initialize a Scraper object with test arguments
        self.test_args = {
            'number_of_books': 5,
            'genre': 'Classics',
            'filters': ['rating>3', 'availability<20'],
            'sortings': ['price', 'ascending'],
            'description': ['Love', 'Peace'],
            'title': 'Olio',
            'titles': 'titles.json'
        }

        self.books_per_page = 20
        self.scraper = Scraper(self.test_args)

    def test_get_url_list_single_page_and_fill_list_of_books_correctly(self):
        self.scraper.get_url_list(1)
        self.assertEqual(len(self.scraper.url_list), self.books_per_page)

    def test_get_url_list_multiple_genres(self):
        test_args = {'genre': ['Childrens'], 'number_of_books': 7}
        scraper = Scraper(test_args)

        scraper.run()

        self.assertEqual(len(scraper.books), 7)

    def test_run_scraping_and_filtering(self):
        test_args = {'titles': 'titles.json', 'number_of_books': 5}
        scraper = Scraper(test_args)
        scraper.run()

        self.assertEqual(len(scraper.books), 5)

    def test_run_scraping_no_filters(self):
        test_args = None
        scraper = Scraper(test_args)
        scraper.run()

        self.assertTrue(len(scraper.books) > 0)

    def test_run_scraping_empty_genre(self):
        test_args = {'genre': '', 'number_of_books': 2}
        scraper = Scraper(test_args)
        scraper.run()

        self.assertFalse(len(scraper.books) > 0)

    def test_run_scraping_with_sorting_ascending(self):
        test_args = {'sorting': ['price', 'ascending'], 'number_of_books': 5}
        scraper = Scraper(test_args)
        scraper.run()
        print(scraper.books[0].price)
        print(scraper.books[-1].price)
        self.assertTrue(scraper.books[0].price <= scraper.books[-1].price)

    def test_run_scraping_with_sorting(self):
        test_args = {'sorting': ['rating', 'descending'], 'number_of_books': 3}
        scraper = Scraper(test_args)
        scraper.run()
        print(scraper.books[0].rating)
        print(scraper.books[-1].rating)
        self.assertTrue(scraper.books[0].rating >= scraper.books[-1].rating)

    def test_run_scraping_with_keywords(self):
        # Test scraping with keywords in book description
        test_args = {'sorting' : 'Gallery', 'genre': ['Art'], 'number_of_books': 3}
        scraper = Scraper(test_args)
        scraper.run()

        self.assertTrue(len(scraper.books) > 0)


if __name__ == '__main__':
    unittest.main()
