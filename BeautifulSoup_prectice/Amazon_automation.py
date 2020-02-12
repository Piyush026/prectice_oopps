import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
cred= ServiceAccountCredentials.from_json_keyfile_name('AmazonAutomation.json',scope)

client = gspread.authorize(cred)