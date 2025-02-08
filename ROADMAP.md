# Roadmap

## Week 1

- [ ] Everyone gets a env working
- [ ] Decide on what data to use
- [ ] Data Exploration

### Data Exploration

**Datasets:**

- `data/raw/yf_stock_prices/[Ticker].csv` (Historical Stock Prices)
- `data/raw/yf_fundamental_data/[Ticker]/balance_sheet.csv` (Balance Sheet)
- `data/raw/yf_fundamental_data/[Ticker]/cashflow.csv` (Cash Flow Statement)
- `data/raw/yf_fundamental_data/[Ticker]/income_statement.csv` (Income Statement)

**Libraries to Use:**

- `pandas` (for data loading and manipulation)
- `numpy` (for numerical operations)
- `matplotlib` and `seaborn` (for data visualization)
- `statsmodels` (for time series analysis)
- `yfinance` (for reference, if needed)

**Notebook Structure (Sections):**

1. **Introduction:**
    - Briefly describe the purpose of this notebook and the datasets being analyzed.
    - State the stock ticker(s) being analyzed.
2. **Data Loading:**
    - Load each CSV file into a pandas DataFrame.
    - Print the shape of each DataFrame.
    - Display the first 5 rows (`.head()`) of each DataFrame to get a sense of the data structure.
3. **Stock Price Data Exploration:**
    - **Column Information:**
        - Use `.info()` to display the data types and non-null counts for each column.
        - Check for any unexpected data types.
    - **Descriptive Statistics:**
        - Use `.describe()` to calculate summary statistics (mean, std, min, max, quartiles) for numerical columns.
        - Analyze the statistics for any unusual or unexpected values.
    - **Missing Value Analysis:**
        - Calculate the percentage of missing values in each column.
        - Visualize the missing data pattern using a heatmap (using `seaborn`).
        - Document potential reasons for missing values (e.g., data not available for certain periods).
        - Discuss possible strategies for handling missing data (e.g., imputation, removal).
    - **Outlier Analysis:**
        - Create box plots for the `Open`, `High`, `Low`, `Close`, `Adj Close`, and `Volume` columns to identify potential outliers.
        - Investigate any identified outliers. Are they genuine data points or errors?
        - Discuss possible strategies for handling outliers (e.g., winsorizing, transformation).
    - **Time Series Visualization:**
        - Plot the `Adj Close` price over time.
        - Plot the `Volume` over time.
        - Identify any trends, seasonality, or volatility.
        - Mark major events (e.g., earnings announcements, product launches) on the price chart (if known).
    - **Return Analysis:**
        - Calculate daily returns: `returns = df['Adj Close'].pct_change()`
        - Plot the distribution of returns using a histogram.
        - Calculate and print the mean and standard deviation of returns.
        - Check for normality using a Q-Q plot or statistical test (Shapiro-Wilk or Kolmogorov-Smirnov).
    - **Autocorrelation Analysis:**
        - Plot the autocorrelation function (ACF) and partial autocorrelation function (PACF) for the `Adj Close` price and returns using `statsmodels`.
        - Interpret the ACF and PACF plots to identify potential patterns in the data.
    - **Stationarity Testing:**
        - Perform the Augmented Dickey-Fuller (ADF) test to check for stationarity of the `Adj Close` price.
        - Report the ADF statistic and p-value.
        - Discuss whether the time series is stationary and, if not, what transformations might be needed to make it stationary.
4. **Fundamental Data Exploration (Balance Sheet, Cash Flow Statement, Income Statement):**
    - **Column Information:**
        - Use `.info()` to display the data types and non-null counts for each column.
        - Check for any unexpected data types.
    - **Data Transposition:**
        - Fundamental data is often structured with dates as columns. You will need to transpose the data.
    - **Missing Value Analysis:**
        - Calculate the percentage of missing values in each column.
        - Document potential reasons for missing values.
        - Discuss possible strategies for handling missing data.
    - **Trend Analysis:**
        - Identify key financial metrics from each statement (e.g., Revenue, Net Income, Total Assets, Total Liabilities, Cash Flow from Operations).
        - Plot these metrics over time to identify trends.
        - Look for any significant changes or anomalies.
    - **Ratio Analysis (Calculate and analyze the following ratios):**
        - Profitability Ratios:
            - Gross Profit Margin: (Revenue - Cost of Goods Sold) / Revenue
            - Operating Profit Margin: Operating Income / Revenue
            - Net Profit Margin: Net Income / Revenue
        - Liquidity Ratios:
            - Current Ratio: Current Assets / Current Liabilities
            - Quick Ratio: (Current Assets - Inventory) / Current Liabilities
        - Solvency Ratios:
            - Debt-to-Equity Ratio: Total Debt / Total Equity
            - Interest Coverage Ratio: EBIT / Interest Expense
        - Efficiency Ratios:
            - Asset Turnover Ratio: Revenue / Total Assets
            - Inventory Turnover Ratio: Cost of Goods Sold / Inventory
        - Valuation Ratios:
            - Price-to-Earnings Ratio (P/E): Market Price per Share / Earnings per Share
            - Price-to-Book Ratio (P/B): Market Price per Share / Book Value per Share
    - **Consistency Checks:**
        - Verify that the financial statements are consistent with each other (e.g., that the ending cash balance in the cash flow statement matches the cash balance in the balance sheet).
5. **Relationship between Stock Prices and Fundamentals (Initial Investigation):**
    - Merge the stock price data with the fundamental data (using the date as the common index).  You'll need to carefully consider the frequency and alignment of the data.  Fundamental data is generally released with a lag, so you may need to shift the fundamental data backwards in time.
    - Calculate the correlation between the `Adj Close` price and key fundamental metrics (e.g., Revenue, Net Income, Earnings per Share).
    - Create scatter plots to visualize the relationship between the `Adj Close` price and key fundamental metrics.
    - Discuss any observed relationships (or lack thereof).
6. **Summary of Findings and Next Steps:**
    - Summarize the key findings from the data exploration process.
    - Highlight any data quality issues that need to be addressed.
    - Outline the next steps in the data preparation process, including data cleaning, feature engineering, and target variable creation.
    - Suggest specific features to engineer based on the data exploration.
7. **Recommendations for Data Handling:**
    - Based on data quality issues, suggest specific methods for treating outliers or missing data.
    - Suggest scaling methods to improve the model.
