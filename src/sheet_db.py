import gspread
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
    return sheet.get_all_values()


def insert_data(sheet_name, data):
    try:
        sheet = DOC.worksheet(sheet_name)
    except:
        DOC.add_worksheet(sheet_name, 10000, 100)
        sheet = DOC.worksheet(sheet_name)

    clear_data(sheet)
    for row in data:
        sheet.append_row(row)


def clear_data(sheet):
    sheet.clear()
