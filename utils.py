import re
class Utils:
    def __init__(self):
        pass

    @staticmethod
    def find_numbers_in_text(text):
        matches = re.findall(r'\d+', text)
        result = int(''.join(matches)) if matches else 0
        return result

    @staticmethod
    def check_for_positive_number(num, msg):
        if num < 0:
            raise ValueError(msg)
        return num

    @staticmethod
    def check_if_exist(obj, msg):
        if not obj:
            raise ValueError(msg)

    @staticmethod
    def check_if_is_instance(obj, class_name):
        if not isinstance(obj, class_name):
            raise TypeError("Invalid data type!")

    @staticmethod
    def check_url_for_single_book_url(url: str):
        return (url.startswith("http://books.toscrape.com/catalogue/page") or
                url.startswith("http://books.toscrape.com/catalogue/category/") or
                url == "http://books.toscrape.com/index.html")
