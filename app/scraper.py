import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os

# Telegram credentials
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_USER_ID = os.getenv("TELEGRAM_USER_ID")

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(os.getenv("GOOGLE_SHEET_ID")).sheet1

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_USER_ID, "text": message}
    requests.post(url, data=data)

def log_to_google_sheets(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp] + data)

def main():
    # Simulated scraped data
    data = ["Demo Supplier", "demo@example.com", "1234567890"]
    message = f"📦 New Lead:
Name: {data[0]}
Email: {data[1]}
Phone: {data[2]}"

    send_telegram_message(message)
    log_to_google_sheets(data)

if __name__ == "__main__":
    main()
