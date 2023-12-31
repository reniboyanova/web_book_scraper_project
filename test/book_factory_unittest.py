import unittest
from book_factory import BookFactory
from book import Book


class test_book_factory(unittest.TestCase):

    def setUp(self):
        self.book_factory = BookFactory()
        self.book_factory.url = "the-black-maria_991/index.html"

    def test_create_soup(self):
        self.assertFalse(self.book_factory.page)
        self.book_factory.create_soup()  # the first time the value is none, after the funcion call it gets a request object
        self.assertTrue(self.book_factory.page)

        self.book_factory.create_soup()
        self.assertEqual(self.book_factory.book.url, "https://books.toscrape.com/catalogue/the-black-maria_991/index.html")

        self.book_factory.url = "catalogue/a-light-in-the-attic_1000/index.html"
        self.book_factory.create_soup()
        self.assertEqual(self.book_factory.book.url, "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")

    def test_scrape_book_details(self):

        self.book_factory.create_soup()
        self.book_factory.scrape_book_details()
        descr = """Praise for Aracelis Girmay:"[Girmay's] every loss—she calls them estrangements—is a yearning for connection across time and place; her every fragment is a bulwark against ruin." — O, The Oprah Magazine "In Aracelis Girmay we have a poet who collects, polishes, and shares stories with such brilliant invention, tenderness, and intellectual liveliness that it is understandabl Praise for Aracelis Girmay:"[Girmay's] every loss—she calls them estrangements—is a yearning for connection across time and place; her every fragment is a bulwark against ruin." — O, The Oprah Magazine "In Aracelis Girmay we have a poet who collects, polishes, and shares stories with such brilliant invention, tenderness, and intellectual liveliness that it is understandable that we think of her as the blessed curator of our collective histories. There is in her art the vulnerability of one who lives inside of the stories that she gathers in this remarkable collection. Her poems set off alarms even as they transform the world she inhabits, showing us, in the process, exactly what she asks of Romare Bearden’s art: ‘…how not to // assign all blackness near the sea / a captivity.’ This is one of the many sweet contradictions in the black maria, which ‘is a black flag / wounding the pastoral.’ I am deeply thankful that we have a poet of her unique and singular talent writing today." —Kwame DawesTaking its name from the moon's dark plains, misidentified as seas by early astronomers, the black maria investigates African diasporic histories, the consequences of racism within American culture, and the question of human identity. Central to this project is a desire to recognize the lives of Eritrean refugees who have been made invisible by years of immigration crisis, refugee status, exile, and resulting statelessness. The recipient of a 2015 Whiting Award for Poetry, Girmay's newest collection elegizes and celebrates life, while wrestling with the humanistic notion of seeing beyond: seeing violence, seeing grace, and seeing each other better."to the sea"great storage house, historyon which we rode, we touchedthe brief pulse of your flutteringpages, spelled with salt & life,your rage, your indifferenceyour gentleness washing our feet,all of you going onwhether or not we live,to you we bring our carnationsyellow & pink, how they floatlike bright sentences atopyour memory's dark hairAracelis Girmay is the author of three poetry collections, the black maria; Kingdom Animalia, which won the Isabella Gardner Award and was a finalist for the NBCC Award; and Teeth. The recipient of a 2015 Whiting Award, she has received grants and fellowships from the Jerome, Cave Canem, and Watson foundations, as well as Civitella Ranieri and the NEA. She currently teaches at Hampshire College's School for Interdisciplinary Arts and in Drew University's low residency MFA program. Originally from Santa Ana, California, she splits her time between New York and Amherst, Massachusetts. ...more"""
        self.assertEqual(self.book_factory.book.title, "The Black Maria")
        self.assertEqual(self.book_factory.book.description, descr)
        self.assertEqual(self.book_factory.book.price, 52.15)
        self.assertEqual(self.book_factory.book.num_of_reviews, 0)
        self.assertEqual(self.book_factory.book.availability, 19)
        self.assertEqual(self.book_factory.book.rating, 1)
        self.assertEqual(self.book_factory.book.genre, "Poetry")

        self.assertIsInstance(self.book_factory.book.price, float)
        self.assertIsInstance(self.book_factory.book.rating, int)

    def test_create_book(self):

        self.book_factory.create_book(self.book_factory.url)
        self.assertIsNotNone(self.book_factory.book)
        self.assertIsInstance(self.book_factory.book, Book)
        self.assertIsNotNone(self.book_factory.create_book(self.book_factory.url))