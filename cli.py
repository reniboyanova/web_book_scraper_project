import json

import defines as de
from utils import Utils as u


class Cli:
    """
    The Cli class handles command-line arguments and provides methods for parsing and processing them.

    Attributes:
        filters (list): List of filters for book selection.
        sorting (str): Sorting criteria for the books.
        number_of_books (int): Number of books to be processed.
        title (str): Title of a book.
        titles (str): Path to a JSON file containing book titles.
        genre (str): Genre of books.
        keywords (list): List of keywords for book selection.

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a Cli object with provided keyword arguments.
        :param **kwargs: Keyword arguments to initialize the object.
        """
        self.filters = kwargs.get('f')
        self.sorting = kwargs.get('s')
        self.number_of_books = kwargs.get('b')
        self.title = kwargs.get('t')
        self.titles = kwargs.get('w')
        self.genre = kwargs.get('g')
        self.keywords = kwargs.get('d')
        self.parse_arguments()
        self.dct_with_filters = self.update_dct()

    def parse_arguments(self):
        """
        Parse command-line arguments and delegate parsing to specific methods.
        """
        if self.filters is not None:  # !!! Code repetition !!!
            self.parse_filters()
        if self.titles is not None:
            self.parse_titles()
        if self.keywords is not None:
            self.parse_keywords()
        if self.genre is not None:
            self.parse_genres()
        if self.number_of_books is not None:
            u.check_for_positive_number(self.number_of_books, de.NOT_NEGATIVE_NUMBER)
        if self.sorting is not None:
            self.parse_sorting()
        if self.number_of_books is None:
            self.number_of_books = de.MAX

    def parse_filters(self):  # !!! Code repetition !!!
        """
        Parse command-line arguments and delegate parsing to specific methods.
        :return:
        """
        fil = self.filters[0]
        filters = [filt.strip() for filt in fil.split(',')]
        self.filters = filters

    def parse_keywords(self):  # !!! Code repetition !!!
        """
        Parse filter arguments and store them as a list of strings.
        """
        key = self.keywords[0]
        keywords = [keywords.strip() for keywords in key.split(',')]
        self.keywords = keywords

    def parse_titles(self):
        """
        Parse a JSON file containing book titles and load it into the 'titles' attribute.
        :return:
        """
        try:
            with open(self.titles, "r") as json_file:
                data = json.load(json_file)
                self.titles = data

        except FileNotFoundError:
            print(f"The JSON file '{self.titles}' was not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        if not self.number_of_books:
            self.number_of_books = len(self.titles)

    def update_dct(self):
        """
        Create a dictionary containing non-None attributes of the object.
        :return: dict: A dictionary of attribute names and their corresponding values.
        """
        return {key: value for key, value in self.__dict__.items() if value is not None}

    def parse_genres(self):
        """
        Parse genre arguments and store them as a list of strings.
        :return:
        """
        self.genre = self.genre.split(', ')
        if self.number_of_books is None:
            self.number_of_books = sum(de.GENRE_NUMBER_OF_BOOKS_DICT.get(genre, 0) for genre in self.genre)

    def parse_sorting(self):
        """
        Check if providing data is in valid values
        """
        if (len(self.sorting) != 2 or self.sorting[0] not in de.VALID_SORTING_VALUE
                or self.sorting[1] not in de.VALID_ORDER_VALUE):
            raise ValueError(de.INVALID_CRITERIA_VALUES_FOR_SORTING)
