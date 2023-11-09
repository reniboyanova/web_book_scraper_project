import unittest
from cli import Cli


class TestCli(unittest.TestCase):

    def setUp(self):
        self.cli_test = Cli()

        self.cli_test.filters = ["rating>10, price>50"]
        self.cli_test.sorting = None
        self.cli_test.number_of_books = 5
        self.cli_test.title = "A Light in the Attic"
        self.cli_test.titles = "titles.json"
        self.cli_test.genre = "History, Music"
        self.cli_test.keywords = ["imagine, world"]
        self.cli_test.dct_with_filters = None

    def test_parse_titles(self):
        self.cli_test.parse_titles()

        self.assertEqual(self.cli_test.number_of_books, 5)  # checks if adds book number correctly
        self.assertEqual(self.cli_test.titles, ["The Black Maria", "Set Me Free", "Olio", "Security", "The Art Forger"])
        # test if sucessfully parses the json file info into list with titles as elements

        self.cli_test.titles = "title.json"

        self.assertTrue(f"The JSON file '{self.cli_test.titles}' was not found.")
        # checks if it catches "file not found error"

    def test_parse_genres(self):
        self.cli_test.parse_genres()

        self.assertEqual(self.cli_test.genre, ["History", "Music"])  # checks correct parsing of genre
        self.assertNotEqual(self.cli_test.genre, ["History, Music"])

    def test_parse_keywords(self):
        self.cli_test.parse_keywords()

        self.assertEqual(self.cli_test.keywords, ["imagine", "world"])  # checks correct parsing of keywords
        self.assertNotEqual(self.cli_test.keywords, ["imagine, world"])

    def test_parse_filters(self):
        self.cli_test.parse_filters()

        self.assertEqual(self.cli_test.filters, ["rating>10", "price>50"])  # checks correct parsing of filters
        self.assertNotEqual(self.cli_test.filters, ["rating>10, price>50"])

    def test_parse_arguments(self):
        self.cli_test.number_of_books = None
        self.cli_test.titles = None
        self.cli_test.parse_arguments()

        self.assertEqual(self.cli_test.number_of_books, 1000)  # checks correct book value if filter missing
        self.assertNotEqual(self.cli_test.number_of_books, None)

        self.cli_test.genre = None
        self.cli_test.parse_arguments()

        self.assertEqual(self.cli_test.genre, None)  # checks entering the if statement if value is None

    def test_update_dct(self):
        self.cli_test.titles = None
        dct_with_console_arguments_wrong_1 = {'b': 5, 'g': 'Default', 'f': ["rating>10, price>50"], 's': None,
                                              'd': ["imagine, world"],
                                              't': "A Light in the Attic", 'w': None}

        dct_with_console_arguments_wrong_2 = {'b': 5, 'g': 'Default', 'f': ["rating>10, price>50"],
                                              'd': ["imagine, world"],
                                              't': "A Light in the Attic"}

        dct_with_console_arguments_right = {'filters': ['rating>10, price>50'], 'number_of_books': 5,
                                            'title': 'A Light in the Attic',
                                            'genre': 'History, Music', 'keywords': ['imagine, world']}
        print(self.cli_test.update_dct())

        # checks if the output of the code would be correct based on the function logic. 2 wrong tests are given
        self.assertEqual(self.cli_test.update_dct(), dct_with_console_arguments_right)
        self.assertNotEqual(self.cli_test.update_dct(), dct_with_console_arguments_wrong_1)
        self.assertNotEqual(self.cli_test.update_dct(), dct_with_console_arguments_wrong_2)