import pandas as pd
import numpy as np

# Load the trade log data from the CSV file
trade_log = pd.read_csv('A://python//trade_log.csv')

# Set initial portfolio value and risk-free interest rate
initial_portfolio_value = 6500
risk_free_rate = 0.05  # 5%

# Calculate the profit/loss for each trade
trade_log['Profit/Loss'] = trade_log['Exit Price'] - trade_log['Entry Price']

# Separate profitable and loss-making trades
profitable_trades = trade_log[trade_log['Profit/Loss'] > 0]
loss_making_trades = trade_log[trade_log['Profit/Loss'] <= 0]

# Calculate parameters
total_trades = len(trade_log)
num_profitable_trades = len(profitable_trades)
num_loss_making_trades = len(loss_making_trades)
win_rate = num_profitable_trades / total_trades

average_profit_per_trade = profitable_trades['Profit/Loss'].mean()
average_loss_per_trade = loss_making_trades['Profit/Loss'].mean()
risk_reward_ratio = average_profit_per_trade / abs(average_loss_per_trade)
loss_rate = 1 - win_rate
expectancy = (win_rate * average_profit_per_trade) - (loss_rate * abs(average_loss_per_trade))

# Calculate portfolio returns
trade_log['Portfolio Value'] = initial_portfolio_value + trade_log['Profit/Loss'].cumsum()

# Calculate daily returns
daily_returns = trade_log['Portfolio Value'].pct_change()
daily_returns[0] = 0  # Set the first return to zero

# Calculate average daily return and daily volatility
average_daily_return = daily_returns.mean()
daily_volatility = daily_returns.std()

# Calculate Sharpe Ratio
sharpe_ratio = (average_daily_return - risk_free_rate) / daily_volatility

# Calculate Max Drawdown and Max Drawdown Percentage
cumulative_returns = (1 + daily_returns).cumprod()
peak = cumulative_returns.expanding().max()
drawdown = (cumulative_returns - peak) / peak
max_drawdown = drawdown.min()
max_drawdown_percentage = max_drawdown * 100

# Calculate CAGR
ending_portfolio_value = trade_log['Portfolio Value'].iloc[-1]
beginning_portfolio_value = initial_portfolio_value
num_periods = len(trade_log)
cagr = (ending_portfolio_value / beginning_portfolio_value) ** (1 / num_periods) - 1

# Calculate Calmar Ratio
calmar_ratio = cagr / abs(max_drawdown)

# Create a DataFrame for the results
results = pd.DataFrame({
    'Parameter': ['Total Trades', 'Profitable Trades', 'Loss-Making Trades', 'Win Rate',
                  'Average Profit per trade', 'Average Loss per trade', 'Risk Reward Ratio', 'Expectancy',
                  'Average ROR per trade', 'Sharpe Ratio', 'Max Drawdown', 'Max Drawdown Percentage', 'CAGR', 'Calmar Ratio'],
    'Value': [total_trades, num_profitable_trades, num_loss_making_trades, win_rate,
              average_profit_per_trade, average_loss_per_trade, risk_reward_ratio, expectancy,
              cagr, sharpe_ratio, max_drawdown, max_drawdown_percentage, cagr, calmar_ratio]
})

# print(results)

# Save results to a CSV file
results.to_csv('results.csv', index=False)
