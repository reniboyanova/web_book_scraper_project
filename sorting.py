import defines as de


class Sorting:
    """
    class Sorting does sorting of a book list by its given criteria
    """

    def __init__(self, list_with_criteria, book_list):
        """
        :param list_with_criteria: [type_of_criteria_, direction(ascending, descending)]
        :param book_list: list with instance from class Book()
        """
        self.list_with_criteria = list_with_criteria
        self.book_list = book_list
        self.keep_sorting_values = {
            de.RATING: None,
            de.AVAILABILITY.lower(): None,
            de.PRICE: None
        }

    def sort_books_based_on_criteria(self):
        """
        Sort books after an unpacking list of criteria
        :return:
        """
        name_of_criteria, value_of_criteria = self.list_with_criteria[0], self.list_with_criteria[1]
        if name_of_criteria in self.keep_sorting_values.keys():
            if name_of_criteria in self.keep_sorting_values.keys():
                self.keep_sorting_values[name_of_criteria] = value_of_criteria
            for key, value in self.keep_sorting_values.items():
                if self.keep_sorting_values[key] is not None:
                    self.sort_books_by_key(key)

    def sort_books_by_key(self, key):
        """
        Sorting, by a criteria name and criteria value if a book list is not empty
        :param key:
        :return:
        """
        print(key)
        if not self.book_list:
            return de.EMPTY_LIST_ERROR + self.sort_books_by_key.__name__ + de.FUNCTION

        if key.lower() == de.RATING:
            self.book_list.sort(key=lambda book: book.rating)
            print([book.rating for book in self.book_list])

        if key.lower() == de.PRICE:
            self.book_list.sort(key=lambda book: book.price)

        elif key.lower() == de.AVAILABILITY.lower():
            self.book_list.sort(key=lambda book: book.availability)

        if self.keep_sorting_values[key] == de.DESCENDING:
            self.book_list = self.book_list[::-1]

    def process_sorting(self):
        self.sort_books_based_on_criteria()
        return self.book_list
