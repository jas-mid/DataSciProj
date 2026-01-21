import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly"
]

# Use your credentials file
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

# Replace with your sheet and worksheet names
sheet = client.open("Importance of Council Metrics (Responses)").worksheet("Form responses 1")

# Print all rows
print(sheet.get_all_values())
