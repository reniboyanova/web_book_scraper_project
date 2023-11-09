import re
from utils import Utils as u
import defines as de


class Filter:
    """
    Class Filter, implementing a single book filtration. It checks every single filter, excluding sorting and number of
    book filters
    """
    def __init__(self, book, dictionary_with_filters):
        """
        Takes two arguments in instance initialising
        :param book: instance from class Book()
        :param dictionary_with_filters: dictionary with collected filters from args
        """
        self.book = book
        self.dictionary_with_filters = dictionary_with_filters
        self.check_filter = True

    def check_filters(self):
        """
        Checks all the filters in the dictionary for the book.
        :return: bool: True if the book passes all filters, False otherwise.
        """
        for key, value in self.dictionary_with_filters.items():
            self.check_key(key, value)
            if not self.check_filter:
                break
        return self.check_filter

    def check_key(self, filter_name, filter_value):
        """
        Dispatches the filter check based on the filter name.
        :param filter_name:  (str): The name of the filter.
        :param filter_value: (str or list): The value of the filter.
        :return:
        """
        if filter_name == "title":
            self.check_t(filter_value)
        elif filter_name == "titles":
            self.check_w(filter_value)
        elif filter_name == "keywords":
            self.check_d(filter_value)
        elif filter_name == "filters":
            self.check_f()

    def check_t(self, filter_value):
        """
        Checks if the book's title matches the filter value.
        :param filter_value: (str): The filter value to compare with the book's title.
        :return:
        """
        if filter_value not in self.book.title:
            self.check_filter = False

    def check_d(self, filter_value):
        """
        Checks if all keywords in the filter are present in the book's description.
        :param filter_value: (list): A list of keywords to check against the book's description.
        :return:
        """
        for word in filter_value:
            if word not in self.book.description:
                self.check_filter = False

    def check_w(self, filter_value):
        """
         Checks if the book's title is in the list of titles provided in the filter.
        :param filter_value: (list): A list of book titles to check against the book's title.
        :return:
        """
        if self.book.title not in filter_value:
            self.check_filter = False

    def check_f(self):
        """
        Checks filters for the book's attributes (e.g., price, availability) based on the provided filter conditions.
        :return:
        """
        for string in self.dictionary_with_filters['filters']:  # price > 10 is 'filter'
            self.check_current_filter(string)
            if not self.check_filter:
                break

    def check_current_filter(self, string):
        """
        Checks a specific filter condition for the book's attributes.
        :param string: (str): The filter condition as a string (e.g., 'price > 10').
        :return:
        """
        signs = r'>|<|>=|<=|='
        separated_string = re.split(signs, string)

        u.check_for_positive_number(int(separated_string[1]), de.VALUE_MUST_BE_A_POSITIVE_NUMBER)

        filter_to_check = separated_string[0].strip()
        attibute_to_check = getattr(self.book, filter_to_check)  # can be price / availability / rating

        string = string[len(filter_to_check):].strip()

        if string[0] == '=':
            string = string.replace('=', '==')

        final_string = f"{attibute_to_check}{string}"
        self.check_filter = eval(final_string)
