import unittest
from unittest.mock import patch
from filter import Filter
from book import Book


class TestFilter(unittest.TestCase):

    def setUp(self):
        self.test_args = {
            'number_of_books': 5,
            'genre': 'Classics',
            'filters': ['rating=3'],
            'sorting': ['price', 'ascending'],
            'keywords': ['imagine', 'world'],
            'title': 'A Light in the Attic',
            'titles': '["The Black Maria", "Set Me Free", "Olio", "Security", "The Art Forger"]',
        }
        self.book_to_test = Book()
        self.book_to_test.title = "A Light in the Attic"
        self.book_to_test.genre = 'poetry'
        self.book_to_test.price = 51.77
        self.book_to_test.availability = 22
        self.book_to_test.rating = 3
        self.book_to_test.description = "It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love th It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love that Silverstein. Need proof of his genius? RockabyeRockabye baby, in the treetopDon't you know a treetopIs no safe place to rock?And who put you up there,And your cradle, too?Baby, I think someone down here'sGot it in for you. Shel, you never sounded so good. ...more"

        self.filter_to_test = Filter(self.book_to_test, self.test_args)

    def test_check_t(self):
        self.filter_to_test.check_t(self.test_args['title'])
        self.assertTrue(self.filter_to_test.check_filter, True)
        # checks if it changes the function bool parameter when entered same title

        self.book_to_test.title = "Olio"
        self.filter_to_test.check_t(self.test_args['title'])

        self.assertEqual(self.filter_to_test.check_filter, False)
        # checks if the function changes its bool member if correct title is given

    def test_check_d(self):

        self.filter_to_test.check_d(self.test_args['keywords'])  # check if all the words are present
        self.assertEqual(self.filter_to_test.check_filter, True)

        self.test_args['keywords'] = ["love", 'peace']
        self.filter_to_test.check_d(self.test_args['keywords'])  # check if both words are not present
        self.assertEqual(self.filter_to_test.check_filter, False)

        self.filter_to_test.check_filter = True  # reset value

        self.test_args['keywords'] = ["imagine", "peace"]
        self.filter_to_test.check_d(self.test_args['keywords'])  # check if one of the words is not present, still returns False
        self.assertEqual(self.filter_to_test.check_filter, False)

    def test_check_w(self):

        self.filter_to_test.check_w(self.test_args['titles'])
        self.assertEqual(self.filter_to_test.check_filter, False)  # if the book title not in the list, check_filter is false

        self.filter_to_test.check_filter = True  # reset value

        self.book_to_test.title = "The Black Maria"
        self.filter_to_test.check_w(self.test_args['titles'])
        self.assertEqual(self.filter_to_test.check_filter, True)

    def test_check_current_filter(self):

        self.filter_to_test.check_current_filter(self.test_args['filters'][0])
        self.assertEqual(self.filter_to_test.check_filter, True)  # test with =

        self.test_args['filters'] = ['rating>3']
        self.filter_to_test.check_current_filter(self.test_args['filters'][0])
        self.assertEqual(self.filter_to_test.check_filter, False)  # test with >

        self.test_args['filters'] = ['rating<3']
        self.filter_to_test.check_current_filter(self.test_args['filters'][0])
        self.assertEqual(self.filter_to_test.check_filter, False)  # test with <

        self.test_args['filters'] = ['rating>=3']
        self.filter_to_test.check_current_filter(self.test_args['filters'][0])
        self.assertEqual(self.filter_to_test.check_filter, True)  # test with >=

        self.test_args['filters'] = ['rating<=3']
        self.filter_to_test.check_current_filter(self.test_args['filters'][0])
        self.assertEqual(self.filter_to_test.check_filter, True)  # test with <=

        self.test_args['filters'] = ['rating<=3', "price=51.77"]
        self.filter_to_test.check_current_filter(self.test_args['filters'][0])
        self.assertEqual(self.filter_to_test.check_filter, True)  # check with two filters

    def test_check_f(self):
        def mock_check_current_filter(string):
            return True

        self.test_args['filters'] = ["price < 10"]

        self.filter_to_test.check_current_filter = mock_check_current_filter
        self.filter_to_test.check_f()
        self.assertTrue(self.filter_to_test.check_filter)

    @patch.object(Filter, 'check_t')
    def test_check_key_title(self, mock_check_t):
        mock_check_t.return_value = True

        self.filter_to_test.check_key("title", self.test_args["title"])
        mock_check_t.assert_called_once_with(self.test_args["title"])

    @patch.object(Filter, 'check_w')
    def test_check_key_titles(self, mock_check_w):
        mock_check_w.return_value = True

        self.filter_to_test.check_key("titles", self.test_args["titles"])
        mock_check_w.assert_called_once_with(self.test_args["titles"])

    @patch.object(Filter, 'check_d')
    def test_check_key_keywords(self, mock_check_d):
        mock_check_d.return_value = True

        self.filter_to_test.check_key("keywords", self.test_args["keywords"])
        mock_check_d.assert_called_once_with(self.test_args["keywords"])

    @patch.object(Filter, 'check_f')
    def test_check_key_filters(self, mock_check_f):
        mock_check_f.return_value = True

        self.filter_to_test.check_key("filters", self.test_args["filters"])
        mock_check_f.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()