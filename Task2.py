import yfinance as yf
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

# Define the ICICI Bank ticker and the time window
ticker = "ICICIBANK.NS"
start_time = datetime.now().replace(hour=11, minute=15, second=0, microsecond=0)
end_time = datetime.now().replace(hour=14, minute=15, second=0, microsecond=0)
interval = timedelta(minutes=15)

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['stock_data']
collection = db['icici_bank']

# Function to log stock data every 15 minutes
def log_stock_data():
    current_time = datetime.now()
    if current_time >= start_time and current_time <= end_time:
        data = yf.download(ticker, period="15m", interval="15m")
        data['Timestamp'] = data.index
        data_dict = data.to_dict(orient='records')
        collection.insert_many(data_dict)
        print(f"Logged data at {current_time}")

# Create a scheduler and add the job
scheduler = BackgroundScheduler()
scheduler.add_job(log_stock_data, 'interval', minutes=15)

# Start the scheduler
scheduler.start()

# Run the program for one week (adjust as needed)
try:
    scheduler.print_jobs()
    for i in range(7):
        input("Press Enter to stop logging data for today...")
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
