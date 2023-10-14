# BlackBoxAssignment

# Task 1:

## Trading Parameter Calculator

A Python script to calculate various trading parameters based on historical trade log data. It leverages the pandas library to process the data and provides the results in a CSV format. The parameters calculated include total trades, profitable trades, loss-making trades, win rate, average profit per trade, average loss per trade, risk-reward ratio, expectancy, average rate of return per trade, Sharpe ratio, max drawdown, max drawdown percentage, CAGR, and Calmar ratio.

## Requirements

- Python 
- pandas
- numpy

## Usage

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:

   ```
   pip install pandas numpy
   ```

3. Make sure trade log data contains columns like 'Entry Price' and 'Exit Price'.
4. Modify the script to specify the correct file path and column names in the code:

   ```python
   # Load the trade log data from the CSV file
   trade_log = pd.read_csv('trade_log.csv')
   ```

5. Run the script:

   ```
   python trading_parameter_calculator.py
   ```

6. The script will calculate the parameters and save the results in a CSV file named 'results.csv'.

## Parameters Calculated

1. Total Trades
2. Profitable Trades
3. Loss-Making Trades
4. Win Rate
5. Average Profit per trade
6. Average Loss per trade
7. Risk Reward Ratio
8. Expectancy
9. Average ROR per trade
10. Sharpe Ratio
11. Max Drawdown
12. Max Drawdown Percentage
13. CAGR
14. Calmar Ratio



# Task 2:

## Real-Time ICICI Bank Stock Data Logging

This project is designed to help you store 15-minute candle data of ICICI Bank every 15 minutes from 11.15 AM to 2.15 PM daily for a week in a MongoDB database. It utilizes the `yfinance` library to retrieve real-time stock data with a 15-minute delay and the `APScheduler` library to schedule the data logging task.

## Prerequisites

Before you begin, ensure you have the following libraries installed:

- `yfinance`: A library to access Yahoo Finance API.
- `pymongo`: A library for working with MongoDB.
- `APScheduler`: A library for scheduling tasks.

You can install these libraries using `pip`:

```bash
pip install yfinance pymongo apscheduler
```

## Getting Started

1. Clone or download this repository to your local machine.

2. Make sure you have MongoDB installed and running locally. You can download and install MongoDB from the official website: https://www.mongodb.com/try/download/community

3. Open the Python script `Task2.py` in your preferred code editor.

4. Edit the script to match your specific requirements if needed. The script contains the ICICI Bank ticker symbol, time window, and MongoDB connection details.

## Running the Program

To run the program and start logging ICICI Bank's 15-minute candle data:

1. Open a terminal and navigate to the project folder.

2. Run the Python script:

```bash
python Task2.py
```

The program will begin logging data according to the specified time window.

3. To stop logging data, press Enter in the terminal. The program will stop, and you can repeat this process for each day of the week to log data for a full week.

## Data Storage

The program logs the stock data in a MongoDB database. You can access and query this data as needed for your analysis.



