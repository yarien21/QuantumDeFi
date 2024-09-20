from real_time_data import get_asset_price

class PaperBot:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.portfolio = {}
        self.position = None
        self.simulated_balance = initial_balance
        self.trades_executed = 0
        self.trading_pair = 'bitcoin'  # You can change this to any cryptocurrency

    def simulate_trade(self, action):
        current_price = get_asset_price(self.trading_pair)
        if current_price is None:
            print("Error fetching price. Trade aborted.")
            return
        
        if action == "buy" and self.position is None:
            self.position = current_price
            print(f"Bought {self.trading_pair} at {current_price} USD")
        elif action == "sell" and self.position is not None:
            profit = current_price - self.position
            print(f"Sold {self.trading_pair} at {current_price} USD, Profit: {profit} USD")
            self.position = None
        
        self.trades_executed += 1

# Example usage
if __name__ == "__main__":
    bot = PaperBot()
    bot.simulate_trade('buy')  # Simulate a buy
    bot.simulate_trade('sell') # Simulate a sell

