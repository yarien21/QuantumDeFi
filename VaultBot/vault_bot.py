import requests
import numpy as np

class VaultBot:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.position = None
        self.trades_executed = 0
        self.trading_pair = 'bitcoin'

    def trade(self, action):
        current_price = self.get_real_price(self.trading_pair)
        if current_price is None:
            print("Error fetching price. Trade aborted.")
            return

        if action == "buy" and self.position is None:
            self.position = current_price
            print(f"Real buy of {self.trading_pair} at {current_price} USD")
        elif action == "sell" and self.position is not None:
            profit = current_price - self.position
            print(f"Real sell of {self.trading_pair} at {current_price} USD. Profit: {profit} USD")
            self.position = None
            self.trades_executed += 1
        else:
            print("Invalid action or no position to sell.")

    def get_real_price(self, trading_pair):

        # Fetch real-time price using the CoinGecko API
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={trading_pair}&vs_currencies=usd"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            price_data = response.json()
            return price_data[trading_pair]['usd']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching real price: {e}")
            return None

    def execute_trade(self):
        print("Running VaultBot Real Trading...")
        self.trade("buy")
        self.trade("sell")
        print(f"Trading complete. Total trades: {self.trades_executed}")
