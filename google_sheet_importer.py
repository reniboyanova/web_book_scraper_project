import pandas as pd
import json
import pygsheets
import defines as de


def import_to_google_sheets():
    """
    Imports data from a JSON file into a Google Sheets spreadsheet using the pygsheets library.

    This function prompts the user for input to determine whether to create a new sheet or use an existing one.
    It then clears the existing sheet if necessary and populates it with data from the JSON file.

    Requires 'credentials.json' for Google Sheets authorization.

    google_client - authorize the Google Sheets client using 'credentials.json'
    spreadsheet - open the target spreadsheet (named "Book Scraper")
    result - a dictionary to store the data columns
    """

    google_client = pygsheets.authorize(service_file=de.CREDENTIALS)

    spreadsheet = google_client.open(de.NAME_OF_SHEET)

    # Ask the user whether to open a new sheet or use an existing one
    work_sheet = spreadsheet[0] if input("Do you want to open new sheet? (y/n) ").lower() == 'n' \
        else spreadsheet.add_worksheet(input("Input the name of sheet, please: "))

    # Clear the existing sheet if it's the first sheet in the spreadsheet
    if work_sheet == spreadsheet[0]:
        work_sheet.clear()

    with open(de.BOOKS_DB, "r") as json_file:
        data = json.load(json_file)

    result = {
        "Title": [],
        "Price": [],
        "URL": [],
        "Genre": [],
        "Num of Reviews": [],
        "Availability": [],
        "Star Rating": [],
    }

    for book in data:
        result["Title"].append(book.get("title", ""))
        result["Price"].append(book.get("price", ""))
        result["URL"].append(book.get("url", ""))
        result["Genre"].append(book.get("genre", ""))
        result["Num of Reviews"].append(book.get("num_of_reviews", ""))
        result["Availability"].append(book.get("availability", ""))
        result["Star Rating"].append(book.get("rating", ""))

    work_sheet.set_dataframe(pd.DataFrame(result), 'A1')

def import_to_google_sheets_from_gui(sheetname, new_sheet):
    """
    Imports data from a JSON file into a Google Sheets spreadsheet using the pygsheets library.

    This function prompts the user for input to determine whether to create a new sheet or use an existing one.
    It then clears the existing sheet if necessary and populates it with data from the JSON file.

    Requires 'credentials.json' for Google Sheets authorization.

    google_client - authorize the Google Sheets client using 'credentials.json'
    spreadsheet - open the target spreadsheet (named "Book Scraper")
    result - a dictionary to store the data columns
    """

    google_client = pygsheets.authorize(service_file=de.CREDENTIALS)

    spreadsheet = google_client.open(de.NAME_OF_SHEET)

    work_sheet = spreadsheet[0] if not new_sheet\
        else spreadsheet.add_worksheet(sheetname)

    # Clear the existing sheet if it's the first sheet in the spreadsheet
    if work_sheet == spreadsheet[0]:
        work_sheet.clear()

    with open(de.BOOKS_DB, "r") as json_file:
        data = json.load(json_file)

    result = {
        "Title": [],
        "Price": [],
        "URL": [],
        "Genre": [],
        "Num of Reviews": [],
        "Availability": [],
        "Star Rating": [],
    }

    for book in data:
        result["Title"].append(book.get("title", ""))
        result["Price"].append(book.get("price", ""))
        result["URL"].append(book.get("url", ""))
        result["Genre"].append(book.get("genre", ""))
        result["Num of Reviews"].append(book.get("num_of_reviews", ""))
        result["Availability"].append(book.get("availability", ""))
        result["Star Rating"].append(book.get("star_rating", ""))

    work_sheet.set_dataframe(pd.DataFrame(result), 'A1')

