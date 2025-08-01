import os
import sys
import django
import pandas as pd
from FinMind.data import DataLoader
from decouple import config
from typing import Optional, List
import datetime
import argparse

# Goal: 爬取所有台灣股票資訊並儲存到資料庫

# Add the project root directory (stock-backend/) to Python module search path
# so we can import modules like 'backend.settings' and 'etf.models'
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# let this script know where to find the Django settings
# `setdefault` is avoiding overwriting if it already exists > if it does, it will keep the existing value
# `DJANGO_SETTINGS_MODULE` is the environment variable Django uses to find the settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
# django.setup() 是讓你可以在 script 裡使用 Django 的 ORM
django.setup()

# Import the Stock model
from etf.models import Stock,StockPrice
# Import the FINMIND_TOKEN from environment variables
FINMIND_TOKEN = config('FINMIND_TOKEN')


# Define the function to fetch stock list
def fetch_stock_list():
    # Build a FinMind API client Object
    api = DataLoader()
    # Login using the API token
    api.login_by_token(api_token=FINMIND_TOKEN)
    # Get today's date in YYYY-MM-DD format
    # today = datetime.date.today().strftime("%Y-%m-%d")

    # Fetch the All Taiwan stock info
    stock_list = api.taiwan_stock_info()
    # Filter the DataFrame to only include specific types if needed
    # stock_list = stock_list[stock_list['type'] == 'ETF']

    # Map the DataFrame to the Stock model
    for _, row in stock_list.iterrows():
        # Write or update the Stock in the database
        Stock.objects.update_or_create(
            symbol=row['stock_id'],
            defaults={
                "name": row['stock_name'],
                "category": row.get("industry_category", ""),
            }
        )

    print(f"已成功寫入 {len(stock_list)} 檔股票")


# Define single stock price 
def fetch_stock_price(start_date: str, end_date: str, symbols: Optional[List[str]] = None):
    # Build a FinMind API client Object
    api = DataLoader()
    # Login using the API token
    api.login_by_token(api_token=FINMIND_TOKEN)

    # build a map of stock symbols to Stock objects
    stock_map = {s.symbol: s for s in Stock.objects.all()}
    if symbols:
        stock_map = {s: stock_map[s] for s in symbols if s in stock_map}
    for symbol, stock_obj in stock_map.items():
        try:
            data = api.taiwan_stock_daily(
                stock_id=symbol,
                start_date=start_date,
                end_date=end_date
            )
            for _, row in data.iterrows():
                StockPrice.objects.update_or_create(
                    stock=stock_map[symbol],
                    date=row['date'],
                    defaults={
                        "open": row.get("open"),
                        "close": row.get("close"),
                        "high": row.get("max"),
                        "low": row.get("min"),
                        "volume": row.get("Trading_Volume"),
                    }
                )
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")


# Define function to fetch ETF prices specifically
def fetch_etf_prices(start_date: str, end_date: str):
    """
    取得所有 category = 'ETF' 的股票價格
    """
    # Get all ETF symbols from database
    etf_stocks = Stock.objects.filter(category='ETF')
    etf_symbols = [stock.symbol for stock in etf_stocks]
    
    if not etf_symbols:
        print("資料庫中沒有找到任何 ETF 股票")
        return
    
    print(f"找到 {len(etf_symbols)} 檔 ETF：{', '.join(etf_symbols)}")
    
    # Use existing fetch_stock_price function
    fetch_stock_price(start_date=start_date, end_date=end_date, symbols=etf_symbols)
    
    print(f"已完成 {len(etf_symbols)} 檔 ETF 價格更新")


# 指令列介面
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="台股清單與價格爬蟲")
    parser.add_argument('--mode', type=str, choices=['list', 'price', 'etf', 'all'], default='all',
                        help="執行模式：list 只抓股票清單，price 只抓價格，etf 只抓ETF價格，all 全部")
    parser.add_argument('--symbols', type=str,
                    help="指定股票代碼（用逗號分隔），例如：2330,0050,1101", default=None)
    parser.add_argument('--start', type=str, help="起始日期 YYYY-MM-DD", default=None)
    parser.add_argument('--end', type=str, help="結束日期 YYYY-MM-DD", default=None)
    args = parser.parse_args()
    symbol_list = args.symbols.split(",") if args.symbols else None

    if args.mode in ['list', 'all']:
        fetch_stock_list()

    if args.mode in ['price', 'all']:
        # 預設抓最近五天
        today = datetime.date.today()
        start = args.start or (today - datetime.timedelta(days=5)).strftime("%Y-%m-%d")
        end = args.end or today.strftime("%Y-%m-%d")
        fetch_stock_price(start_date=start, end_date=end, symbols=symbol_list)
    
    if args.mode == 'etf':
        # 預設抓最近五天的ETF資料
        today = datetime.date.today()
        start = args.start or (today - datetime.timedelta(days=5)).strftime("%Y-%m-%d")
        end = args.end or today.strftime("%Y-%m-%d")
        fetch_etf_prices(start_date=start, end_date=end)