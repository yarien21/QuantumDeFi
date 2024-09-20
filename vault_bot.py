class VaultBot:
    def __init__(self, initial_balance=10000, risk_per_trade=0.01):
        self.balance = initial_balance
        self.risk_per_trade = risk_per_trade
        self.portfolio = {}
        self.max_loss = initial_balance * risk_per_trade
        self.position = None

    def calculate_position_size(self, asset, stop_loss):
        # Calculate how much of the asset to buy based on stop-loss and risk
        risk_amount = self.balance * self.risk_per_trade
        position_size = risk_amount / stop_loss
        return position_size

    def set_stop_loss(self, asset, stop_price):
        # Implement stop-loss logic to limit losses
        self.portfolio[asset] = {"stop_loss": stop_price}

    def trade(self, asset, price, stop_loss):
        position_size = self.calculate_position_size(asset, stop_loss)
        # Implement the logic to buy/sell with risk management
        if position_size * price <= self.balance:
            self.balance -= position_size * price
            self.set_stop_loss(asset, stop_loss)
            print(f"Bought {position_size} of {asset} at {price} with stop-loss at {stop_loss}")
        else:
            print("Insufficient balance.")
