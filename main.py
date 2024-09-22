import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'MintBot')))  # Add MintBot to sys path

from mint_bot import MintBot  # Import MintBot correctly
from vault_bot import VaultBot

class BotPricing:
    def __init__(self):
        self.vaultbot_price = 30  # Assume $30 per month for VaultBot
        self.mintbot_future_price = 28  # Assume $28 per month for MintBot after promo
        self.current_promo = True  # Promo status for MintBot

    def calculate_savings(self):
        # Calculate cost savings by choosing VaultBot over MintBot after promo
        return self.mintbot_future_price - self.vaultbot_price

    def display_pricing_info(self):
        if self.current_promo:
            print("Promo: MintBot is currently FREE for a limited time!")
        print(f"VaultBot Subscription: ${self.vaultbot_price} per month.")
        print(f"MintBot will cost ${self.mintbot_future_price} per month after the promo ends.")
        print(f"Save ${self.calculate_savings()} per month by subscribing to VaultBot now!")


def main():
    pricing = BotPricing()
    
    print("Select Bot:")
    print("1. MintBot (Simulated Trading)")
    print("2. VaultBot (Live Trading)")
    pricing.display_pricing_info()  # Display the pricing info, promo, and savings

    choice = input("Enter choice (1 or 2): ")
    print(f"Choice entered: {choice}")

    if choice == '1':
        if pricing.current_promo:
            print("MintBot is FREE during the promo!")
        bot = MintBot()  # Use MintBot for simulation
        bot.run_simulation()  # Run simulation
    elif choice == '2':
        bot = VaultBot(initial_balance=50000)  # Use VaultBot for live trading
        bot.execute_trade()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()





