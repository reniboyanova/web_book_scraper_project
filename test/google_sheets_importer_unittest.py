import unittest
import os

import pygsheets
import defines as de
from google_sheet_importer import import_to_google_sheets


class TestGoogleSheetsImporter(unittest.TestCase):

    def test_import_to_google_sheets_creates_new_sheet(self):
        ask_for_user_choice = de.ASKING_FOR_IMPORT_TO_GOOGLE_SHEETS
        if ask_for_user_choice.lower() == 'y':
            import_to_google_sheets()
            google_client = pygsheets.authorize(service_file=de.CREDENTIALS)
            spreadsheet = google_client.open(de.NAME_OF_SHEET)
            self.assertTrue(spreadsheet.worksheet_by_title(input("New sheet name is: ")) is not None)

    def test_import_to_google_sheets_uses_existing_sheet(self):
        ask_for_user_choice = de.ASKING_FOR_IMPORT_TO_GOOGLE_SHEETS
        if ask_for_user_choice.lower() == 'n':
            import_to_google_sheets()
            google_client = pygsheets.authorize(service_file=de.CREDENTIALS)
            spreadsheet = google_client.open(de.NAME_OF_SHEET)
            worksheet = spreadsheet.worksheet_by_title("Sheet1")
            self.assertTrue(worksheet is not None)

    def test_import_to_google_sheets_clears_existing_sheet(self):
        ask_for_user_choice = de.ASKING_FOR_IMPORT_TO_GOOGLE_SHEETS
        if ask_for_user_choice.lower() == 'y':
            import_to_google_sheets()

            google_client = pygsheets.authorize(service_file=de.CREDENTIALS)
            spreadsheet = google_client.open(de.NAME_OF_SHEET)
            worksheet = spreadsheet.worksheet_by_title("Sheet1")
            data_frame = worksheet.get_as_df()

            self.assertTrue(data_frame.empty)

    def test_import_to_google_sheets_data_imported(self):
        ask_for_user_choice = de.ASKING_FOR_IMPORT_TO_GOOGLE_SHEETS
        if ask_for_user_choice.lower() == 'y':
            import_to_google_sheets()

            google_client = pygsheets.authorize(service_file=de.CREDENTIALS)
            spreadsheet = google_client.open(de.NAME_OF_SHEET)
            worksheet = spreadsheet.worksheet_by_title("Sheet1")
            data_frame = worksheet.get_as_df()

            self.assertFalse(data_frame.empty)

    def test_import_to_google_sheets_invalid_credentials(self):
        invalid_credentials_file = '../credentials.json'

        with self.assertRaises(Exception):
            import_to_google_sheets()
            google_client = pygsheets.authorize(service_file=invalid_credentials_file)

    def test_import_to_google_sheets_empty_json_file(self):
        empty_json_file = 'empty_books_db.json'
        with open(empty_json_file, 'w') as file:
            file.write('{}')

        with self.assertRaises(Exception):
            import_to_google_sheets()

    def test_import_to_google_sheets_invalid_data(self):

        invalid_data_json_file = 'invalid_data_books_db.json'
        with open(invalid_data_json_file, 'w') as file:
            file.write('[{"title": "Book 1"}, {"price": 20.0}]')

        with self.assertRaises(Exception):
            import_to_google_sheets()

    def test_import_to_google_sheets_invalid_worksheet_name(self):
        invalid_name = "%*&&^%@@"
        ask_for_user_choice = de.ASKING_FOR_IMPORT_TO_GOOGLE_SHEETS
        if ask_for_user_choice.lower() == 'y':
            import_to_google_sheets()
            google_client = pygsheets.authorize(service_file=de.CREDENTIALS)
            spreadsheet = google_client.open(de.NAME_OF_SHEET)
            self.assertIsNone(spreadsheet.worksheet_by_title(invalid_name))


if __name__ == '__main__':
    unittest.main()

