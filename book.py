import defines as de


class Book:
    """
    class Book represent a scraped information about a single book from scraped url.
    It's an attributes in __init__ method:
    'title' -> str, 'description' -> str, 'prise' -> float, 'url' -> str, 'num_of_reviews' -> int,
    'availability' -> int, 'star_rating' -> int
    """

    def __init__(self):
        self.title = ''
        self.description = ''
        self.price = 0
        self.url = ''
        self.genre = ''
        self.num_of_reviews = 0
        self.availability = 0
        self.rating = 0

    def __str__(self):
        """
        A string representation of object information.
        Call __str__ method with print(obj)
        :return: A string representation of object attributes
        """

        availability = "In stock (" + str(self.availability) + " available)" if self.availability > 0 \
            else "Not available!"

        return (
                "Title: " + self.title +
                "\nGenre: " + self.genre +
                "\nDescription: " + self.description +
                "\nPrice: " + de.POUND_SIGN + str(self.price) +
                "\nURL: " + self.url +
                "\nNumber of Reviews: " + str(self.num_of_reviews) +
                "\nAvailability: " + availability +
                "\nStar Rating: " + str(self.rating)
        )
