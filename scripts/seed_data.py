import yfinance as yf
import os


def download_stock_price_data(
    ticker: str, start_date: str, end_date: str, raw_data_dir="./data/raw/yf_prices"
):
    # Download stock data from the internet
    file_path = f"{raw_data_dir}/{ticker}.csv"
    
    # if raw_data_dir does not exist, create it
    if not os.path.exists(raw_data_dir):
        os.makedirs(raw_data_dir)

    if not os._exists(raw_data_dir):
        data = yf.download(ticker, start=start_date, end=end_date)
        data.to_csv(file_path)
        print(f"Downloaded {ticker} data to {file_path}")
    else:
        print(f"Data for {ticker} already exists at {file_path}")


def download_stock_fundimental_data(
    ticker: str, raw_data_dir="./data/raw/yf_fundimentals"
):
    # Download stock data from the internet
    file_path = f"{raw_data_dir}/{ticker}/"
    
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    ticker_data = yf.Ticker(ticker)

    balance_sheet = ticker_data.balance_sheet

    if balance_sheet is not None:
        balance_sheet.to_csv(file_path + "balance_sheet.csv")
        print(f"Downloaded {ticker} balance sheet data to {file_path + "balance_sheet.csv"}")
    else:
        print(f"No balance sheet data for {ticker}")

    cash_flow = ticker_data.cashflow

    if cash_flow is not None:
        cash_flow.to_csv(file_path + "cash_flow.csv")
        print(f"Downloaded {ticker} cash flow data to {file_path + "cash_flow.csv"}")
    else:
        print(f"No cash flow data for {ticker}")

    income_statement = ticker_data.income_stmt

    if income_statement is not None:
        income_statement.to_csv(file_path + "income_statement.csv")
        print(f"Downloaded {ticker} income statement data to {file_path}")
    else:
        print(f"No income statement data for {ticker}")


def main():
    ticker_list = [
        "AAPL",
        "MSFT",
        "NVDA",
        "JNJ",
        "PFE",
        "JPM",
        "GS",
        "XOM",
        "CVX",
        "TSLA",
        "AMZN",
        "NEE",
        "CAT",
        "BA",
    ]
    start_date = "2020-01-01"
    end_date = "2025-01-01"

    for ticker in ticker_list:
        #download_stock_price_data(ticker, start_date, end_date)
        download_stock_fundimental_data(ticker)


if __name__ == "__main__":
    main()
