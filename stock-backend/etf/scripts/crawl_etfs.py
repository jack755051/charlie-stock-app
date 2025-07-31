import os
import sys
import django
import pandas as pd
from FinMind.data import DataLoader
from decouple import config
import datetime

# Goal:

# Add the project root directory (stock-backend/) to Python module search path
# so we can import modules like 'backend.settings' and 'etf.models'
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# let this script know where to find the Django settings
# `setdefault` is avoiding overwriting if it already exists > if it does, it will keep the existing value
# `DJANGO_SETTINGS_MODULE` is the environment variable Django uses to find the settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
# django.setup() 是讓你可以在 script 裡使用 Django 的 ORM
django.setup()

# Import the ETF model
from etf.models import ETF
# Import the FINMIND_TOKEN from environment variables
FINMIND_TOKEN = config('FINMIND_TOKEN')
# Define the function to fetch ETF list
def fetch_etf_list():
    # Build a FinMind API client Object
    api = DataLoader()
    # Login using the API token
    api.login_by_token(api_token=FINMIND_TOKEN)
    # Get today's date in YYYY-MM-DD format
    # today = datetime.date.today().strftime("%Y-%m-%d")

    # Fetch the All Taiwan stock info
    etf_list = api.taiwan_stock_info()
    # Filter the DataFrame to only include ETFs
    # etf_list = etf_list[etf_list['type'] == 'ETF']

    print(etf_list.head())
    print(etf_list.columns)
    print(etf_list["type"].unique())

    # Map the DataFrame to the ETF model
    for _, row in etf_list.iterrows():
        # Write or update the ETF in the database
        ETF.objects.update_or_create(
            symbol=row['stock_id'],
            defaults={
                "name": row['stock_name'],
                "category": row.get("industry_category", ""),
                "price": 0
            }
        )

    print(f"已成功寫入 {len(etf_list)} 檔 ETF")

if __name__ == "__main__":
    fetch_etf_list()