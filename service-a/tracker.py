import time
import requests
import logging
from collections import deque

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%H:%M:%S'
)

MAX_MINUTES = 10
FETCH_INTERVAL = 60  # seconds
AVERAGE_LOG_INTERVAL = 600  # seconds (10 minutes)

class BitcoinPriceTracker:
    def __init__(self):
        self.prices = deque()
        self.last_avg_log_time = 0

    def fetch_price(self):
        try:
            response = requests.get(
                'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
            )
            response.raise_for_status()
            data = response.json()
            return float(data['bitcoin']['usd'])
        except requests.RequestException as e:
            logging.error(f"Error fetching price: {e}")
            return None

    def update_prices(self):
        price = self.fetch_price()
        if price is not None:
            timestamp = time.time()
            self.prices.append((timestamp, price))
            self.remove_old_prices(timestamp)
            self.log_price(price)
            self.log_average(timestamp)

    def remove_old_prices(self, current_time):
        cutoff = current_time - (MAX_MINUTES * 60)
        while self.prices and self.prices[0][0] < cutoff:
            self.prices.popleft()

    def log_price(self, price):
        logging.info(f"Current price: ${price:.2f}")

    def log_average(self, current_time):
        if current_time - self.last_avg_log_time >= AVERAGE_LOG_INTERVAL and self.prices:
            avg = sum(p[1] for p in self.prices) / len(self.prices)
            logging.info(f"10-minute average: ${avg:.2f}")
            self.last_avg_log_time = current_time

    def get_data(self):
        if not self.prices:
            return {"avg": "N/A", "latest": "N/A"}
        avg = sum(p[1] for p in self.prices) / len(self.prices)
        latest = self.prices[-1][1]
        return {"avg": round(avg, 2), "latest": round(latest, 2)}

    def run(self):
        while True:
            self.update_prices()
            time.sleep(FETCH_INTERVAL)
