import gspread
from google.oauth2.service_account import Credentials

#api adress
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("sheets/Data/fincreds.json", scopes=scopes)
client = gspread.authorize(creds)

#sheets adress
sheets_id = "1KzWfisUpYVOSY9jSZONPRd_ef5nP-AYIseCN_N3VG7E"
sheets = client.open_by_key(sheets_id)

#worksheet adresses
tsla_sheet = sheets.worksheet("tsla")

#data write
tsla_sheet.update_cell( 1 , 1 , '=GOOGLEFINANCE( "TSLA" ; "all"; today()-90 ; today() ; 1 )')

#data read
value = tsla_sheet.acell("B2").value
print(value)