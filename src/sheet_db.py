import gspread
import time
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
DOC = GSPREAD_CLIENT.open('recipe_data')


def get_data(sheet):
    sheet = DOC.worksheet(sheet)
    data = sheet.get_all_values()

    result = []
    for row in data:
        kurz = []
        for cell in row:
            if '|||' in cell:
                cell = cell.split('|||')
            kurz.append(cell)

        result.append(kurz)
    return result


def insert_data(sheet_name, data):
    """

    :param sheet_name: worksheet from google
    :param data: i.e. [['asd', ['ingredient 1', 'ingredient 2']]]
    :return: None
    """

    try:
        sheet = DOC.worksheet(sheet_name)
    except Exception as _:
        DOC.add_worksheet(sheet_name, 2000, 10)
        sheet = DOC.worksheet(sheet_name)

    clear_data(sheet)

    # Making it compatible
    data_in_insert = []
    for row in data:
        temp = []
        for cell in row:
            if type(cell) == list:
                cell = '|||'.join(cell)
            temp.append(cell)
        data_in_insert.append(temp)

    # Insert in to sheet
    for row in data_in_insert:
        insert_completed = False

        while not insert_completed:
            try:
                sheet.append_row(row)
                insert_completed = True
            except Exception as _:
                time.sleep(10)


def clear_data(sheet):
    sheet.clear()
