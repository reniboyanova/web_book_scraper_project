from filter import Filter
from page_book_scraper import PageBookScraper
import defines as de
from database import DataBase
from book_factory import BookFactory
from sorting import Sorting
import google_sheet_importer


class Scraper:
    """
    Scraper class for scraping and processing book data.
    """
    def __init__(self, args) -> None:
        """
        Initializes a Scraper object with the provided command-line arguments.
        :param args:  (dict): A dictionary containing filters and options for the scraping process.
        """
        self.args = args  # dict with filters
        self.books = []
        self.url_list = []
        self.import_to_sheets = False
        self.new_sheet = False
        self.sheetname = ""
        self.gui_active = False

    def get_url_list(self, page_number):
        """
        Gets a list of URLs for scraping book data from genre pages.
        :param page_number:  (int): The page number to start scraping from
        """
        genre_links = []

        if 'genre' in self.args:
            for genre_type in self.args['genre']:
                if genre_type in de.GENRE_DICT_ALL_LINKS:
                    genre_links.extend(de.GENRE_DICT_ALL_LINKS[genre_type])
                    self.args['genre'].remove(genre_type)
        else:
            genre_links.append(f"https://books.toscrape.com/catalogue/page-{page_number}.html")

        for genre_link in genre_links:
            page_scraper = PageBookScraper(genre_link)
            page_scraper.page_scraper(20)
            self.url_list += page_scraper.book_links

    def run(self):
        """
        Executes the scraping and processing of book data based on the provided arguments.
        :return:
        """
        number_books = 0
        current_books_passed = 0
        page_number = 1

        self.get_url_list(page_number)

        while number_books < self.args["number_of_books"]:

            book_factory = BookFactory()
            if self.url_list:
                book = book_factory.create_book(self.url_list[0])
                self.url_list.pop(0)
            else:
                break

            f = Filter(book, self.args)
            if f.check_filters():
                self.books.append(book)
                number_books += 1

            current_books_passed += 1
            if current_books_passed % 20 == 0:
                page_number += 1
                self.get_url_list(page_number)

        if 'sorting' in self.args.keys():
            sorting = Sorting(self.args['sorting'], self.books)
            sorting.sort_books_based_on_criteria()
            self.books = sorting.process_sorting()
        DataBase().parse(self.books)  # add in file
        print(f"Number of book found: {len(self.books)}")

        if not self.gui_active:
            if input(de.ASKING_FOR_IMPORT_TO_GOOGLE_SHEETS).lower() == 'y':
                google_sheet_importer.import_to_google_sheets()

        else:
            if self.import_to_sheets:
                google_sheet_importer.import_to_google_sheets_from_gui(self.sheetname, self.new_sheet)
