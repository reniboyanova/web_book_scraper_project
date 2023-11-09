import argparse
from cli import Cli
from scraper import Scraper
from GUI import GUI


def parse_args(parser):
    return parser


def main():
    #

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', type=int, help="Number of books")
    parser.add_argument('-g', type=str, help="List f genres to search through")
    parser.add_argument('-f', type=str, nargs='+', help="List of filters")
    parser.add_argument('-s', nargs=2, type=str, metavar=("what we order", "order"),
                        help="Order something ascending or descending")
    parser.add_argument('-d', type=str, nargs='+',
                        help="List of keywords for searching in the description")
    parser.add_argument('-t', type=str, help="Search for a book title (only one)")
    parser.add_argument('-w', type=str,
                        help="List of wanted book titles to search for "
                             "(from given json containing list of book titles")

    if all(value is None for value in vars(parser.parse_args()).values()):
        gui = GUI()
        gui.open_window()
    else:
        options = {}

        for argument, value in vars(parser.parse_args()).items():
            options[argument] = value

        res = Cli(**options)
        s = Scraper(res.dct_with_filters)
        s.run()


if __name__ == '__main__':
    main()
