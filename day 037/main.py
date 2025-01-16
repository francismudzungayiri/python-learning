import gspread
from google.oauth2.service_account import Credentials
import os


scopes = [
    'https://www.googleapis.com/auth/spreedsheets'
]

creds = Credentials.from_service_account_file(os.path.expanduser('/Users/mbuluundi/Desktop/python/day 037/credentials.json'), scopes = scopes)
client = gspread.authorize(creds)
sheet_id =  '1PNlnkuSnv5aOzliapnmg7qXPr5CFllFlFG7lRELC8W8'

#open the sheet
sheet = client.open_by_key(sheet_id)

values_list = sheet.sheet1.row_values(1)
print(values_list)