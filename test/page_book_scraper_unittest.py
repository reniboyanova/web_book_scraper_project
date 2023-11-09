import re
import unittest
import urllib.request

from bs4 import BeautifulSoup as bs
from page_book_scraper import PageBookScraper


def get_soup(url):
    page = urllib.request.urlopen(url)
    return bs(page, features="html.parser")

def str_to_bs4(url):
        html_soup = bs(url, 'html.parser')
        html_tags = html_soup.find_all('li')
        return html_tags


class TestPageBookScraper(unittest.TestCase):

    def setUp(self):
        self.test_real_book_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
        self.test_fail_book_url = "https://books.catalogue/a-light-in-the-attic/index.html"
        self.test_genre_url = "http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html"
        self.test_second_page_url = "http://books.toscrape.com/catalogue/page-2.html"
        self.basic_url = "https://books.toscrape.com/"
        self.test_scraper = PageBookScraper(self.basic_url)

    def test_make_instance_of_page_book_scraper(self):
        scraper = PageBookScraper(self.test_real_book_url)
        self.assertIsInstance(scraper, PageBookScraper)

    def test_get_correct_url_as_parameter(self):
        expected = "https://books.toscrape.com/"
        self.assertEqual(expected, self.test_scraper.url)

    def test_incorrect_url_as_parameter(self):
        test_url = "https://books.toscrape"
        self.assertNotEqual(test_url, self.test_scraper.url)

    def test_has_at_least_one_link_in_book_links(self):
        self.test_scraper.book_links.append(self.test_real_book_url)

        one_book_link = len(self.test_scraper.book_links)
        result = one_book_link == 1

        self.assertTrue(result)
        self.assertGreater(result, 0)

    def test_empty_book_links(self):
        self.test_scraper.book_links = []

        result = self.test_scraper.book_links
        self.assertTrue(not result, "List of links is empty!")

    def test_correct_url_with_regex(self):  # make this check in utils
        regex_pattern = r"https://books\.toscrape\.com/catalogue/[a-zA-Z\/_\-1-90]*\.html"

        match = re.match(regex_pattern, self.test_real_book_url)
        self.assertTrue(match, "Correct url match!")

    def test_incorrect_url_with_regex(self):  # make this check in utils
        regex_pattern = r"https://books\.toscrape\.com/catalogue/[a-zA-Z\/_\-1-90]*\.html"

        match = re.match(regex_pattern, self.test_fail_book_url)
        self.assertFalse(match, "Incorrect url match!")

    def test_have_links_in_book_list(self):
        scraper = PageBookScraper(self.test_second_page_url)
        scraper.page_scraper()
        expected_links = 20
        real_result = len(scraper.book_links)

        self.assertEqual(expected_links, real_result)

    def test_has_next_page(self):
        soup = get_soup(self.basic_url)
        result = self.test_scraper.has_next_page(soup)

        self.assertTrue(result)

    def test_has_not_next_page(self):
        last_page = "https://books.toscrape.com/catalogue/page-50.html"
        soup = get_soup(last_page)
        result = self.test_scraper.has_next_page(soup)

        self.assertFalse(result)

    def test_get_and_set_urls_from_genre_link(self):
        scraper = PageBookScraper(self.test_genre_url)
        scraper.page_scraper()
        expected_links = 11
        real_result = len(scraper.book_links)

        self.assertEqual(expected_links, real_result)

    def test_get_correct_url(self):
        scraper = PageBookScraper(self.basic_url)
        scraper.page_scraper(1)
        expected_url_mock = "catalogue/a-light-in-the-attic_1000/index.html"
        self.assertEqual(scraper.book_links[0], expected_url_mock)

    def test_get_incorrect_url(self):
        scraper = PageBookScraper(self.basic_url)
        scraper.page_scraper(3)
        expected_url_mock = "catalogue/a-light-in-the-attic_1000/index.html"
        self.assertNotEqual(scraper.book_links[1], expected_url_mock)

    def test_assert_raises_for_negative_value(self):
        with self.assertRaises(ValueError):
            self.test_scraper.page_scraper(-1)


if __name__ == '__main__':
    unittest.main()


