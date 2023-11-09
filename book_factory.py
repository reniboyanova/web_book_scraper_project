from bs4 import BeautifulSoup as bs
import re
import urllib.request
import defines as de
from book import Book
from utils import Utils as u


class BookFactory:
    """
        The BookFactory is responsible for creating an instance of the Book class and extracting information
        from the provided link based on the attributes of the Book class.
    """

    def __init__(self):
        self.book = Book()
        self.page = None
        self.soup = None
        self.url = ""

    def create_soup(self):
        """
        Initialize the soup object for accessing the book data
        """
        if "catalogue/" not in self.url:
            self.url = "catalogue/" + self.url

        self.book.url = de.BASIC_URL + '/' + self.url
        self.page = urllib.request.urlopen(self.book.url)
        self.soup = bs(self.page, features="html.parser")

    def scrape_book_details(self):
        """
        Extract our book object's title, description, price,
        availability and rating data from the site.
        """

        self.book.title = self.soup.body.h1.text

        book_descr = self.soup.body.find('div', id=de.PRODUCT_DESCRIPTION)

        if book_descr is not None:
            for i in range(6):
                book_descr = book_descr.next_element
            self.book.description = book_descr.text
        else:
            self.book.description = "None"

        self.book.price = float(self.soup.body.find(string=re.compile(de.POUND_SIGN))[1::])
        self.book.num_of_reviews = int(
            self.soup.body.find(string=re.compile(de.NUMBER_OF_REVIEWS)).next_element.next_element.text)

        availability = self.soup.body.find(string=re.compile(de.AVAILABILITY)).next_element.next_element.text
        self.book.availability = u.find_numbers_in_text(availability)

        rating = self.soup.body.find_all('p')
        rating = rating[2].get('class')[1]
        self.book.rating = de.STAR_RATING[rating]

        genre = self.soup.find("ul", class_="breadcrumb").find_all("li")[2].text.strip()
        self.book.genre = genre

    def create_book(self, url):
        """
        Creates and returns a book object after getting it's data from an URL
        """
        self.url = url
        self.create_soup()
        self.scrape_book_details()
        return self.book
