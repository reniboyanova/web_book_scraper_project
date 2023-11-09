import json

import defines as de


class DataBase:
    """
    Class DataBase represent a Data Base with using txt file, where to write collected information in using format
    """
    def __init__(self):
        """
        It has as arguments txt files which are hold an info as Data base
        """
        self.books_DB = de.BOOKS_DB  # the file which holds scraped information about books

    @staticmethod
    def append_in_db(json_obj_format, file):
        """
        Append info in dictionary format to txt file
        :param file:
        :param json_obj_format:
        :return:
        """
        file.write(json_obj_format)
        file.write('\n')

    def clean_db(self):
        """
        Cleaning file with scraped books
        :return:
        """
        file = open(self.books_DB, 'w')
        file.close()

    def parse(self, books):
        """
        Parse all collected book info to a string, add the string in the database.
        """
        books_json_list = []

        for book in books:
            obj_dict = vars(book)
            books_json_list.append(obj_dict)

        with open(self.books_DB, 'w') as file:
            json.dump(books_json_list, file, indent=de.DEFAULT_INDENT)