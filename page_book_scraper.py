from bs4 import BeautifulSoup as bs
import urllib.request
import defines as de
from utils import Utils as u


class PageBookScraper:
    """
    PageBookScraper class for scraping book links from a web page.
    """

    def __init__(self, url):
        """
         Initializes a PageBookScraper object with the provided URL.
        :param url: (str): The URL of the web page to scrape book links from.
        """
        self.url = url
        self.book_links = []
        self.num_of_books = 0
        self.book_links_acquired = 0

    def has_next_page(self, soup) -> bool:
        """
        Checks if there is a next page link in the provided soup object.
        :param soup: (BeautifulSoup): The BeautifulSoup object representing the current page.
        :return: bool: True if a next page exists, False otherwise.
        """

        next_page = soup.find("li", class_="next")

        if next_page is not None and next_page.text == "next":
            self.url = self.get_next_page_url(next_page)
            return True
        return False

    @staticmethod
    def get_next_page_url(next_page):
        """
        Extracts the URL of the next page from the "next_page" element.
        :param next_page: (Tag): The "next_page" element in the current page's HTML.
        :return: str: The URL of the next page.
        """

        added_url = next_page.a.get('href')

        if "catalogue/" not in added_url:
            added_url = "catalogue/" + added_url
        next_page_link = de.BASIC_URL + '/' + added_url

        return next_page_link

    def page_scraper(self, num_of_books=de.MAX_NUMBER_OF_BOOKS_PER_PAGE):
        """
        Scrapes book links from the web page.
        :param num_of_books: (int): The maximum number of book links to scrape (optional).
        :return:
        """

        self.num_of_books = u.check_for_positive_number(num_of_books, de.NOT_NEGATIVE_NUMBER)

        page = urllib.request.urlopen(self.url)
        soup = bs(page, features=de.DEFAULT_HTML_PARSER)
        book_links = soup.body.ol.select('a', href=True)

        for link in book_links:
            if link.text != '':
                link = link.get('href').replace('../../../', '')
                self.book_links.append(link)
                self.book_links_acquired += 1
                if self.book_links_acquired == self.num_of_books:
                    return

        if self.has_next_page(soup):
            self.page_scraper(self.num_of_books)

