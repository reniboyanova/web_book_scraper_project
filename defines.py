""" defines.py holds all literals, constants and main prints """

# Basic URL:
BASIC_URL = "https://books.toscrape.com"

# Max number of books for selection
MAX = 1000
MAX_NUMBER_OF_BOOKS_PER_PAGE = 20

# Searching Attributes in HTML:
PRODUCT_DESCRIPTION = "product_description"
POUND_SIGN = '£'
NUMBER_OF_REVIEWS = 'Number of reviews'
AVAILABILITY = 'Availability'

# Database (Json files):
BOOKS_DB = 'books_DB.json'

# Constant Dictionaries:
STAR_RATING = {
    'Zero': 0,
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
}

# Menu prints:
CHOOSE_NUMBER_OF_BOOKS = "Choose number of books to scrape: "
INVALID_MENU = "Invalid input!"
DO_YOU_WANT_TO_PRINT = "Do you want to print the info abut books?\nAnswer: "
NUMBER_OF_BOOKS_FOUND = "Number of founded books: "
ASKING_FOR_IMPORT_TO_GOOGLE_SHEETS = "Do you want to export data to GSheet? (y/n): "

# Error messages:
UNABLE_TO_OPEN_PAGE = "Error: Unable to retrieve the page."
NO_NEXT_PAGE = "No next page available!"
NO_VALUES_OR_MORE_VALUES_ERROR = "List of criteria need to be of 2 elements [criteria_name, criteria_value]"
INVALID_CRITERIA_VALUES_FOR_SORTING = ("Invalid criteria name or value! Names must be - 'rating', 'price', 'availability'!"
                         "\nCriteria value must be ascending or descending!")
EMPTY_LIST_ERROR = "List is empty. List must contain any books to be: "
URL_OPEN_ERROR = "Can not open URL!"
CAN_NOT_SCRAPE_BOOKS = "Can't scrape books!"
NOT_FOUND_ANY_BOOKS = "Not found any books!"
NOT_NEGATIVE_NUMBER = "Number of books must be a positive number!"
NOT_ANY_VALUE_BEFORE_CLI_ERROR = "No arguments provided! Must provide at least one filter to use Book Scraper!"
VALUE_MUST_BE_A_POSITIVE_NUMBER = "Value must be a positive number!"

# Default parameters:
DEFAULT_INDENT = 4
DEFAULT_HTML_PARSER = "html.parser"

# Categories filters name / literals:
TITLE = 'title'
GENRE = 'genre'
DESCRIPTION = 'description'
FILTERS = 'filters'
RATING = 'rating'
SPLIT_SIGN = ','
PRICE = 'price'
SORT = 'sort'
LIST_OF_BOOKS = 'list_of_books'
FUNCTION = " function."

ASCENDING = 'ascending'
DESCENDING = 'descending'

VALID_SORTING_VALUE = ["rating", "price", "availability"]
VALID_ORDER_VALUE = ["ascending", "descending"]

# Info For Google Sheets Importer:
CREDENTIALS = 'credentials.json'
NAME_OF_SHEET = "Book Scraper"

# Genre Links Dict:
#
# GENRE_DICT = {
#     'Travel': 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html',
#     'Mystery': 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
#     'Historical Fiction': 'https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
#     'Sequential Art': 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
#     'Classics': 'https://books.toscrape.com/catalogue/category/books/classics_6/index.html',
#     'Philosophy': 'https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
#     'Romance': 'https://books.toscrape.com/catalogue/category/books/romance_8/index.html',
#     'Womens Fiction': 'https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
#     'Fiction': 'https://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
#     'Childrens': 'https://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
#     'Religion': 'https://books.toscrape.com/catalogue/category/books/religion_12/index.html',
#     'Nonfiction': 'https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
#     'Music': 'https://books.toscrape.com/catalogue/category/books/music_14/index.html',
#     'Default': 'https://books.toscrape.com/catalogue/category/books/default_15/index.html',
#     'Science Fiction': 'https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
#     'Sports and Games': 'https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
#     'Add a comment': 'https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
#     'Fantasy': 'https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
#     'New Adult': 'https://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
#     'Young Adult': 'https://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
#     'Science': 'https://books.toscrape.com/catalogue/category/books/science_22/index.html',
#     'Poetry': 'https://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
#     'Paranormal': 'https://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
#     'Art': 'https://books.toscrape.com/catalogue/category/books/art_25/index.html',
#     'Psychology': 'https://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
#     'Autobiography': 'https://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
#     'Parenting': 'https://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
#     'Adult Fiction': 'https://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
#     'Humor': 'https://books.toscrape.com/catalogue/category/books/humor_30/index.html',
#     'Horror': 'https://books.toscrape.com/catalogue/category/books/horror_31/index.html',
#     'History': 'https://books.toscrape.com/catalogue/category/books/history_32/index.html',
#     'Food and Drink': 'https://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
#     'Christian Fiction': 'https://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html',
#     'Business': 'https://books.toscrape.com/catalogue/category/books/business_35/index.html',
#     'Biography': 'https://books.toscrape.com/catalogue/category/books/biography_36/index.html',
#     'Thriller': 'https://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
#     'Contemporary': 'https://books.toscrape.com/catalogue/category/books/contemporary_38/index.html',
#     'Spirituality': 'https://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
#     'Academic': 'https://books.toscrape.com/catalogue/category/books/academic_40/index.html',
#     'Self Help': 'https://books.toscrape.com/catalogue/category/books/self-help_41/index.html',
#     'Historical': 'https://books.toscrape.com/catalogue/category/books/historical_42/index.html',
#     'Christian': 'https://books.toscrape.com/catalogue/category/books/christian_43/index.html',
#     'Suspense': 'https://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
#     'Short Stories': 'https://books.toscrape.com/catalogue/category/books/short-stories_45/index.html',
#     'Novels': 'https://books.toscrape.com/catalogue/category/books/novels_46/index.html',
#     'Health': 'https://books.toscrape.com/catalogue/category/books/health_47/index.html',
#     'Politics': 'https://books.toscrape.com/catalogue/category/books/politics_48/index.html',
#     'Cultural': 'https://books.toscrape.com/catalogue/category/books/cultural_49/index.html',
#     'Erotica': 'https://books.toscrape.com/catalogue/category/books/erotica_50/index.html',
#     'Crime': 'https://books.toscrape.com/catalogue/category/books/crime_51/index.html'}

GENRE_DICT_ALL_LINKS = {
    'Travel': ['https://books.toscrape.com/catalogue/category/books/travel_2/index.html'],
    'Mystery': ['https://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
                'https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html'],
    'Historical Fiction': ['https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
                           'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-2.html'],
    'Sequential Art': ['https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
                       'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html',
                       'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html',
                       'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html'],
    'Classics': ['https://books.toscrape.com/catalogue/category/books/classics_6/index.html'],
    'Philosophy': ['https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html'],
    'Romance': ['https://books.toscrape.com/catalogue/category/books/romance_8/index.html',
                'http://books.toscrape.com/catalogue/category/books/romance_8/page-2.html'],
    'Womens Fiction': ['https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html'],
    'Fiction': ['https://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
                'http://books.toscrape.com/catalogue/category/books/fiction_10/page-2.html',
                'http://books.toscrape.com/catalogue/category/books/fiction_10/page-3.html',
                'http://books.toscrape.com/catalogue/category/books/fiction_10/page-4.html'],
    'Childrens': ['https://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
                  'http://books.toscrape.com/catalogue/category/books/childrens_11/page-2.html'],
    'Religion': ['https://books.toscrape.com/catalogue/category/books/religion_12/index.html'],
    'Nonfiction': ['https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
                   'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html',
                   'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html',
                   'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html',
                   'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html',
                   'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-6.html'
                   ],
    'Music': ['https://books.toscrape.com/catalogue/category/books/music_14/index.html'],
    'Default': ['https://books.toscrape.com/catalogue/category/books/default_15/index.html',
                'http://books.toscrape.com/catalogue/category/books/default_15/page-2.html',
                'http://books.toscrape.com/catalogue/category/books/default_15/page-3.html',
                'http://books.toscrape.com/catalogue/category/books/default_15/page-4.html',
                'http://books.toscrape.com/catalogue/category/books/default_15/page-5.html',
                'http://books.toscrape.com/catalogue/category/books/default_15/page-6.html',
                'http://books.toscrape.com/catalogue/category/books/default_15/page-7.html',
                'http://books.toscrape.com/catalogue/category/books/default_15/page-8.html'
                ],
    'Science Fiction': ['https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html'],
    'Sports and Games': ['https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html'],
    'Add a comment': ['https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
                      'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-2.html',
                      'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-3.html',
                      'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-4.html'
                      ],
    'Fantasy': ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
                'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-2.html',
                'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-3.html'],
    'New Adult': ['https://books.toscrape.com/catalogue/category/books/new-adult_20/index.html'],
    'Young Adult': ['https://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
                    'http://books.toscrape.com/catalogue/category/books/young-adult_21/page-2.html',
                    'http://books.toscrape.com/catalogue/category/books/young-adult_21/page-3.html'],
    'Science': ['https://books.toscrape.com/catalogue/category/books/science_22/index.html'],
    'Poetry': ['https://books.toscrape.com/catalogue/category/books/poetry_23/index.html'],
    'Paranormal': ['https://books.toscrape.com/catalogue/category/books/paranormal_24/index.html'],
    'Art': ['https://books.toscrape.com/catalogue/category/books/art_25/index.html'],
    'Psychology': ['https://books.toscrape.com/catalogue/category/books/psychology_26/index.html'],
    'Autobiography': ['https://books.toscrape.com/catalogue/category/books/autobiography_27/index.html'],
    'Parenting': ['https://books.toscrape.com/catalogue/category/books/parenting_28/index.html'],
    'Adult Fiction': ['https://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html'],
    'Humor': ['https://books.toscrape.com/catalogue/category/books/humor_30/index.html'],
    'Horror': ['https://books.toscrape.com/catalogue/category/books/horror_31/index.html'],
    'History': ['https://books.toscrape.com/catalogue/category/books/history_32/index.html'],
    'Food and Drink': ['https://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
                       'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/page-2.html'],
    'Christian Fiction': ['https://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html'],
    'Business': ['https://books.toscrape.com/catalogue/category/books/business_35/index.html'],
    'Biography': ['https://books.toscrape.com/catalogue/category/books/biography_36/index.html'],
    'Thriller': ['https://books.toscrape.com/catalogue/category/books/thriller_37/index.html'],
    'Contemporary': ['https://books.toscrape.com/catalogue/category/books/contemporary_38/index.html'],
    'Spirituality': ['https://books.toscrape.com/catalogue/category/books/spirituality_39/index.html'],
    'Academic': ['https://books.toscrape.com/catalogue/category/books/academic_40/index.html'],
    'Self Help': ['https://books.toscrape.com/catalogue/category/books/self-help_41/index.html'],
    'Historical': ['https://books.toscrape.com/catalogue/category/books/historical_42/index.html'],
    'Christian': ['https://books.toscrape.com/catalogue/category/books/christian_43/index.html'],
    'Suspense': ['https://books.toscrape.com/catalogue/category/books/suspense_44/index.html'],
    'Short Stories': ['https://books.toscrape.com/catalogue/category/books/short-stories_45/index.html'],
    'Novels': ['https://books.toscrape.com/catalogue/category/books/novels_46/index.html'],
    'Health': ['https://books.toscrape.com/catalogue/category/books/health_47/index.html'],
    'Politics': ['https://books.toscrape.com/catalogue/category/books/politics_48/index.html'],
    'Cultural': ['https://books.toscrape.com/catalogue/category/books/cultural_49/index.html'],
    'Erotica': ['https://books.toscrape.com/catalogue/category/books/erotica_50/index.html'],
    'Crime': ['https://books.toscrape.com/catalogue/category/books/crime_51/index.html'],
}


GENRE_NUMBER_OF_BOOKS_DICT = {
    'Travel': 11,
    'Mystery': 32,
    'Historical Fiction': 26,
    'Sequential Art': 75,
    'Classics': 19,
    'Philosophy': 11,
    'Romance': 35,
    'Womens Fiction': 17,
    'Fiction': 65,
    'Childrens': 29,
    'Religion': 7,
    'Nonfiction': 110,
    'Music': 13,
    'Default': 152,
    'Science Fiction': 16,
    'Sports and Games': 5,
    'Add a comment': 67,
    'Fantasy': 48,
    'New Adult': 6,
    'Young Adult': 54,
    'Science': 14,
    'Poetry': 19,
    'Paranormal': 1,
    'Art': 8,
    'Psychology': 7,
    'Autobiography': 9,
    'Parenting': 1,
    'Adult Fiction': 1,
    'Humor': 10,
    'Horror': 17,
    'History': 18,
    'Food and Drink': 30,
    'Christian Fiction': 6,
    'Business': 12,
    'Biography': 5,
    'Thriller': 11,
    'Contemporary': 3,
    'Spirituality': 6,
    'Academic': 1,
    'Self Help': 5,
    'Historical': 2,
    'Christian': 3,
    'Suspense': 1,
    'Short Stories': 1,
    'Novels': 1,
    'Health': 4,
    'Politics': 3,
    'Cultural': 1,
    'Erotica': 1,
    'Crime': 1}

